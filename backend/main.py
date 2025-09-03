# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum
import uuid

# --- Create the FastAPI App ---
app = FastAPI(
    title="Subscription Tracker API",
    description="An API to track your monthly and yearly subscriptions.",
    version="1.0.0",
)

# --- In-Memory Database (A simple dictionary) ---
# In a real app, this would be a real database (e.g., PostgreSQL with SQLAlchemy)
db = {}

# --- Pydantic Models (Data Schemas) ---
class BillingCycle(str, Enum):
    monthly = "monthly"
    yearly = "yearly"

class SubscriptionBase(BaseModel):
    name: str
    price: float
    currency: str = "USD"
    billing_cycle: BillingCycle
    start_date: date

class SubscriptionCreate(SubscriptionBase):
    pass # No new fields needed for creation

class Subscription(SubscriptionBase):
    id: uuid.UUID
    # In a real app, you would add a user_id here

# --- API Routes ---

# Health Check Route
@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "API is running"}

# Create a new subscription
@app.post("/subscriptions/", response_model=Subscription, status_code=201, tags=["Subscriptions"])
def create_subscription(subscription: SubscriptionCreate):
    """
    Adds a new subscription to your tracker.
    """
    new_id = uuid.uuid4()
    new_subscription = Subscription(id=new_id, **subscription.dict())
    db[new_id] = new_subscription
    return new_subscription

# Get all subscriptions
@app.get("/subscriptions/", response_model=List[Subscription], tags=["Subscriptions"])
def get_all_subscriptions():
    """
    Retrieves a list of all your subscriptions.
    """
    return list(db.values())

# Get a single subscription by its ID
@app.get("/subscriptions/{subscription_id}", response_model=Subscription, tags=["Subscriptions"])
def get_subscription(subscription_id: uuid.UUID):
    """
    Retrieves the details of a specific subscription.
    """
    if subscription_id not in db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db[subscription_id]

# Update a subscription
@app.put("/subscriptions/{subscription_id}", response_model=Subscription, tags=["Subscriptions"])
def update_subscription(subscription_id: uuid.UUID, updated_info: SubscriptionCreate):
    """
    Updates the details of an existing subscription.
    """
    if subscription_id not in db:
        raise HTTPException(status_code=404, detail="Subscription not found")

    # Update the existing subscription object
    subscription = db[subscription_id]
    for key, value in updated_info.dict().items():
        setattr(subscription, key, value)
    
    return subscription

# Delete a subscription
@app.delete("/subscriptions/{subscription_id}", status_code=204, tags=["Subscriptions"])
def delete_subscription(subscription_id: uuid.UUID):
    """
    Deletes a subscription from your tracker.
    """
    if subscription_id not in db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    del db[subscription_id]
    return # Return nothing on 204 No Content