from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate, UpdateUserProfile
from datetime import datetime
from api.security import hash_password


# Function to create a new user in the database
def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        mob_number=user.mob_number,
        role="customer",
        created_at=datetime.utcnow(),
        updated_at=None
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Get user by mobile number
def get_user_by_mobile(db: Session, mob_number: str):
    return db.query(User).filter(User.mob_number == mob_number).first()


# ✅ Update user profile (name, mob_number)
def update_user_profile(db: Session, user: User, data: UpdateUserProfile):
    if data.name:
        user.name = data.name
    if data.mob_number:
        user.mob_number = data.mob_number
    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user



# ✅ Update user password
def update_user_password(db: Session, user: User, new_password: str):
    user.password = hash_password(new_password)
    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user
