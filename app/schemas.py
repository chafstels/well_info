from pydantic import BaseModel

class Lease(BaseModel):
    OIL_GAS_CODE: str
    DISTRICT_NO: str
    LEASE_NO: str
    CYCLE_YEAR: int
    CYCLE_MONTH: int
    LEASE_OIL_PROD_VOL: float

    class Config:
        from_attributes = True

class Well(BaseModel):
    OIL_GAS_CODE: str
    DISTRICT_NO: str
    LEASE_NO: str
    WELL_NO: str

    class Config:
        from_attributes = True



class WellQuery(BaseModel):
    api_number: str

class WellResponse(BaseModel):
    OIL_GAS_CODE: str
    DISTRICT_NO: str
    LEASE_NO: str
    WELL_NO: str
    API_COUNTY_CODE: str
    API_UNIQUE_NO: str
    COUNTY_NAME: str
    DISTRICT_NAME: str
    # Добавьте другие поля по необходимости

    class Config:
        from_attributes = True


class ProductionData(BaseModel):
    CYCLE_YEAR: int
    CYCLE_MONTH: int
    LEASE_OIL_PROD_VOL: float
    LEASE_GAS_PROD_VOL: float
    LEASE_COND_PROD_VOL: float
    LEASE_NAME: str

    class Config:
        from_attributes = True