from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.get("/lease/{lease_no}", response_model=schemas.Lease)
def read_lease(lease_no: str, db: Session = Depends(get_db)):
    db_lease = crud.get_lease_by_number(db, lease_no=lease_no)
    if db_lease is None:
        raise HTTPException(status_code=404, detail="Lease not found")
    return db_lease