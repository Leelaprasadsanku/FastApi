from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import schemas, database
from ..database import get_db
from ..repository import user
from .. import oauth2

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)