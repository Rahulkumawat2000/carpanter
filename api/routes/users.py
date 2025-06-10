from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.models.user import User
from api.database.schemas.user import UserResponse, UpdateUserProfile, UpdatePassword
from api.token import get_current_user
from passlib.context import CryptContext
from typing import List

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Get profile of currently logged-in user
@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


# Update user profile
@router.put("/update-profile", response_model=UserResponse)
def update_profile(
    data: UpdateUserProfile,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.name:
        current_user.name = data.name
    if data.mob_number:
        current_user.mob_number = data.mob_number
    db.commit()
    db.refresh(current_user)
    return current_user


# Update password
@router.put("/update-password")
def update_password(
    data: UpdatePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    hashed_password = pwd_context.hash(data.new_password)
    current_user.password = hashed_password
    db.commit()
    return {"message": "Password updated successfully"}


# ✅ Get all users
@router.get("/all", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# ✅ Get user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ✅ Delete user by ID
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
