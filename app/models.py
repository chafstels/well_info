from sqlalchemy import Column, Integer, String, Numeric, CHAR
from .database import Base

class OGLeaseCycle(Base):
    __tablename__ = "OG_LEASE_CYCLE"

    # Создаем искусственный первичный ключ
    id = Column(Integer, primary_key=True, autoincrement=True)

    OIL_GAS_CODE = Column(CHAR(1), nullable=False)
    DISTRICT_NO = Column(CHAR(2), nullable=False)
    LEASE_NO = Column(String(6), nullable=False)
    CYCLE_YEAR = Column(CHAR(4), nullable=False)
    CYCLE_MONTH = Column(CHAR(2), nullable=False)
    CYCLE_YEAR_MONTH = Column(String(6))
    LEASE_NO_DISTRICT_NO = Column(Numeric(10, 0))
    OPERATOR_NO = Column(String(6))
    FIELD_NO = Column(String(8))
    FIELD_TYPE = Column(CHAR(2))
    GAS_WELL_NO = Column(String(6))
    PROD_REPORT_FILED_FLAG = Column(CHAR(1))
    LEASE_OIL_PROD_VOL = Column(Numeric(9, 0))
    LEASE_OIL_ALLOW = Column(Numeric(9, 0))
    LEASE_OIL_ENDING_BAL = Column(Numeric(9, 0))
    LEASE_GAS_PROD_VOL = Column(Numeric(9, 0))
    LEASE_GAS_ALLOW = Column(Numeric(9, 0))
    LEASE_GAS_LIFT_INJ_VOL = Column(Numeric(9, 0))
    LEASE_COND_PROD_VOL = Column(Numeric(9, 0))
    LEASE_COND_LIMIT = Column(Numeric(9, 0))
    LEASE_COND_ENDING_BAL = Column(Numeric(9, 0))
    LEASE_CSGD_PROD_VOL = Column(Numeric(9, 0))
    LEASE_CSGD_LIMIT = Column(Numeric(9, 0))
    LEASE_CSGD_GAS_LIFT = Column(Numeric(9, 0))
    LEASE_OIL_TOT_DISP = Column(Numeric(9, 0))
    LEASE_GAS_TOT_DISP = Column(Numeric(9, 0))
    LEASE_COND_TOT_DISP = Column(Numeric(9, 0))
    LEASE_CSGD_TOT_DISP = Column(Numeric(9, 0))
    DISTRICT_NAME = Column(CHAR(2))
    LEASE_NAME = Column(String(255))  # Увеличена длина до 255 символов
    OPERATOR_NAME = Column(String(50))
    FIELD_NAME = Column(String(32))

class OGWellCompletion(Base):
    __tablename__ = "OG_WELL_COMPLETION"

    # Создаем искусственный первичный ключ
    id = Column(Integer, primary_key=True, autoincrement=True)

    OIL_GAS_CODE = Column(CHAR(1), nullable=False)
    DISTRICT_NO = Column(CHAR(2), nullable=False)
    LEASE_NO = Column(String(6), nullable=False)
    WELL_NO = Column(String(6), nullable=False)
    API_COUNTY_CODE = Column(CHAR(3), nullable=False)
    API_UNIQUE_NO = Column(String(5), nullable=False)
    ONSHORE_ASSC_CNTY = Column(CHAR(3))
    DISTRICT_NAME = Column(CHAR(2))
    COUNTY_NAME = Column(String(50))
    OIL_WELL_UNIT_NO = Column(String(6))
    WELL_ROOT_NO = Column(String(8))
    WELLBORE_SHUTIN_DT = Column(String(6))
    WELL_SHUTIN_DT = Column(String(6))
    WELL_14B2_STATUS_CODE = Column(CHAR(1))
    WELL_SUBJECT_14B2_FLAG = Column(CHAR(1))
    WELLBORE_LOCATION_CODE = Column(CHAR(1))
