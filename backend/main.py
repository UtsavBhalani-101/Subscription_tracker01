# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date, timedelta, datetime
from enum import Enum
import uuid

# --- Security and Authentication Imports ---
from passlib.context import CryptContext
from jose import JWTError, jwt

# =================================================================
# 1. SECURITY AND CONFIGURATION
# =================================================================

# --- Password Hashing Setup ---
# We use bcrypt for hashing. It's a strong, widely-used algorithm.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- JWT Configuration ---
# These should be in a .env file in a real application!
SECRET_KEY = "YOUR_SUPER_SECRET_KEY_THAT_IS_VERY_LONG_AND_COMPLEX" # Change this!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 scheme for token handling
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# =================================================================
# 2. IN-MEMORY DATABASE SIMULATION
# =================================================================

# In a real app, this would be a real database (e.g., PostgreSQL with SQLAlchemy)
users_db = {}
subscriptions_db = {}

# =================================================================
# 3. PYDANTIC MODELS (DATA SCHEMAS)
# =================================================================

# --- User Models ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: uuid.UUID
    is_active: bool = True

class UserInDB(User):
    hashed_password: str

# --- Token Models ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- Subscription Models ---
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
    owner_id: uuid.UUID

# =================================================================
# 4. HELPER & DEPENDENCY FUNCTIONS
# =================================================================

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, email: str):
    for user_id, user in db.items():
        if user.email == email:
            return user
    return None

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- The core dependency to get the current user ---
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = get_user(users_db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# =================================================================
# 5. API APPLICATION AND ROUTES
# =================================================================

app = FastAPI(
    title="Subscription Tracker API",
    description="An API to track your monthly and yearly subscriptions.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows your frontend (e.g., http://localhost:3000) to talk to this backend.
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- AUTHENTICATION ROUTES ---

@app.post("/register", response_model=User)
def register_user(user: UserCreate):
    """
    Create a new user account. Passwords are hashed before storing.
    """
    if get_user(users_db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_id = uuid.uuid4()
    new_user = UserInDB(id=user_id, email=user.email, hashed_password=hashed_password)
    users_db[user_id] = new_user
    return new_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Logs a user in and returns a JWT access token.
    The frontend should send form data with 'username' (which is the email) and 'password'.
    """
    user = get_user(users_db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# --- USER ROUTES ---

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    Get the profile information of the currently logged-in user.
    """
    return current_user


# --- SUBSCRIPTION ROUTES (PROTECTED) ---

@app.post("/subscriptions/", response_model=Subscription, status_code=status.HTTP_201_CREATED)
def create_subscription(
    subscription: SubscriptionCreate,
    current_user: User = Depends(get_current_active_user)
):
    """
    Adds a new subscription for the currently logged-in user.
    """
    new_id = uuid.uuid4()
    # Link the new subscription to the current user
    new_subscription = Subscription(id=new_id, owner_id=current_user.id, **subscription.dict())
    subscriptions_db[new_id] = new_subscription
    return new_subscription

@app.get("/subscriptions/", response_model=List[Subscription])
def get_all_subscriptions(current_user: User = Depends(get_current_active_user)):
    """
    Retrieves a list of all subscriptions belonging to the current user.
    """
    user_subscriptions = [
        sub for sub in subscriptions_db.values() if sub.owner_id == current_user.id
    ]
    return user_subscriptions

@app.get("/subscriptions/{subscription_id}", response_model=Subscription)
def get_subscription(
    subscription_id: uuid.UUID,
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieves the details of a specific subscription, checking for ownership.
    """
    if subscription_id not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription = subscriptions_db[subscription_id]
    if subscription.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this subscription")
        
    return subscription

@app.put("/subscriptions/{subscription_id}", response_model=Subscription)
def update_subscription(
    subscription_id: uuid.UUID,
    updated_info: SubscriptionCreate,
    current_user: User = Depends(get_current_active_user)
):
    """
    Updates a subscription, checking for ownership first.
    """
    if subscription_id not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")

    subscription = subscriptions_db[subscription_id]
    if subscription.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this subscription")
    
    for key, value in updated_info.dict().items():
        setattr(subscription, key, value)
    
    return subscription

@app.delete("/subscriptions/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscription(
    subscription_id: uuid.UUID,
    current_user: User = Depends(get_current_active_user)
):
    """
    Deletes a subscription, checking for ownership first.
    """
    if subscription_id not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")
        
    subscription = subscriptions_db[subscription_id]
    if subscription.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this subscription")
        
    del subscriptions_db[subscription_id]
    return # Return nothing on 204 No Content

# --- Health Check Route ---
@app.get("/")
def read_root():
    return {"status": "Subscription Tracker API is running"}