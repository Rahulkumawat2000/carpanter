from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Create User Schema (used in registration)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str

# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UpdateUserProfile(BaseModel):
    name: Optional[str]
    mob_number: Optional[str]  # ✅ email की जगह mobile number


# Update Password Schema
class UpdatePassword(BaseModel):
    new_password: str = Field(min_length=6)
    confirm_password: str = Field(min_length=6)

# Response Schema (used in API responses)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    mob_number: str
    role: str

    class Config:
        from_attributes = True
