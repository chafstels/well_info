from fastapi import APIRouter, Request, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import get_db
from app import crud, schemas

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/well/search", response_class=HTMLResponse)
async def form_well_search(request: Request):
    return templates.TemplateResponse("well_search.html", {"request": request})


@router.post("/well/search", response_class=HTMLResponse)
async def handle_well_search(request: Request, api_number: str = Form(...), db: Session = Depends(get_db)):
    api_county_code = api_number[:3]
    api_unique_no = api_number[3:]

    well = crud.get_well_by_api(db, api_county_code=api_county_code, api_unique_no=api_unique_no)
    if well is None:
        return templates.TemplateResponse("well_search.html", {"request": request, "error": "Well not found"})

    production_data = crud.get_production_data(db, lease_no=well.LEASE_NO, district_no=well.DISTRICT_NO)
    production_summary = crud.get_production_summary(db, lease_no=well.LEASE_NO, district_no=well.DISTRICT_NO,
                                                     oil_gas_code=well.OIL_GAS_CODE)
    related_apis = crud.get_related_apis(db, lease_no=well.LEASE_NO, district_no=well.DISTRICT_NO)

    # Проверьте, что возвращает production_data
    if production_data:
        production_data = [schemas.ProductionData(
            CYCLE_YEAR=data.CYCLE_YEAR,
            CYCLE_MONTH=data.CYCLE_MONTH,
            LEASE_OIL_PROD_VOL=data.LEASE_OIL_PROD_VOL,
            LEASE_GAS_PROD_VOL=data.LEASE_GAS_PROD_VOL,
            LEASE_COND_PROD_VOL=data.LEASE_COND_PROD_VOL,
            LEASE_NAME=data.LEASE_NAME,
        ) for data in production_data]

    return templates.TemplateResponse("well_result.html", {
        "request": request,
        "well": well,
        "production_data": production_data,
        "production_summary": production_summary,
        "related_apis": related_apis,
    })

