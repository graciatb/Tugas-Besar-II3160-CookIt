# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


# Create User
def create(user: schemas.User, db: Session = Depends(get_db)):
    print(user)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password 
    
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get User
def get(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id: {id} does not exist")
    
    return user

# Delete User
def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User dengan id {id} tidak ditemukan")
    user.delete(synchronize_session=False)
    db.commit()
    return {"Message": f"User dengan id {id} telah berhasil dihapus"}