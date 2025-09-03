# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum
import uuid

# NEW: Import the CORS middleware
from fastapi.middleware.cors import CORSMiddleware

# --- Create the FastAPI App ---
app = FastAPI(
    title="Subscription Tracker API",
    description="An API to track your monthly and yearly subscriptions.",
    version="1.0.0",
)

# --- NEW: Set up CORS ---
# This list contains the origins that are allowed to make requests to your API.
# For development, you might allow all origins with "*"
# Or be more specific, e.g., for a React app running on port 3000
origins = [
    "http://localhost",
    "http://localhost:3000", # For React dev server
    "http://127.0.0.1:5500", # For VS Code Live Server
    # Add the origin of your deployed frontend here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# --- In-Memory Database (A simple dictionary) ---
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
    pass

class Subscription(SubscriptionBase):
    id: uuid.UUID

# --- API Routes (Your existing routes go here) ---
# ... (paste all your @app.get, @app.post, etc. routes here) ...

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "API is running"}

@app.post("/subscriptions/", response_model=Subscription, status_code=201, tags=["Subscriptions"])
def create_subscription(subscription: SubscriptionCreate):
    new_id = uuid.uuid4()
    new_subscription = Subscription(id=new_id, **subscription.dict())
    db[new_id] = new_subscription
    return new_subscription

@app.get("/subscriptions/", response_model=List[Subscription], tags=["Subscriptions"])
def get_all_subscriptions():
    return list(db.values())

# ... and so on for your other routes