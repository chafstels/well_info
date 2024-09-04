from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models

def get_well_by_api(db: Session, api_county_code: str, api_unique_no: str):
    return db.query(models.OGWellCompletion).filter(
        models.OGWellCompletion.API_COUNTY_CODE == api_county_code,
        models.OGWellCompletion.API_UNIQUE_NO == api_unique_no
    ).first()


def get_production_data(db: Session, lease_no: str, district_no: str):
    return db.query(
        models.OGLeaseCycle.LEASE_NO,
        models.OGLeaseCycle.DISTRICT_NO,
        models.OGLeaseCycle.CYCLE_YEAR,
        models.OGLeaseCycle.CYCLE_MONTH,
        models.OGLeaseCycle.LEASE_OIL_PROD_VOL,
        models.OGLeaseCycle.LEASE_GAS_PROD_VOL,
        models.OGLeaseCycle.LEASE_COND_PROD_VOL,
        models.OGLeaseCycle.LEASE_NAME,
    ).filter(
        models.OGLeaseCycle.LEASE_NO == lease_no,
        models.OGLeaseCycle.DISTRICT_NO == district_no
    ).order_by(
        models.OGLeaseCycle.CYCLE_YEAR.desc(),
        models.OGLeaseCycle.CYCLE_MONTH.desc()
    ).all()



def get_production_summary(db: Session, lease_no: str, district_no: str, oil_gas_code: str):
    # Определение поля для газа в зависимости от типа скважины
    gas_field = "LEASE_CSGD_TOT_DISP" if oil_gas_code == "O" else "LEASE_GAS_PROD_VOL"

    # Сумма за первый месяц
    first_month = db.execute(
        text(f"""
        SELECT
            SUM("LEASE_OIL_PROD_VOL") AS total_oil,
            SUM("{gas_field}") AS total_gas,
            SUM("LEASE_COND_PROD_VOL") AS total_condensate
        FROM "OG_LEASE_CYCLE"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no
        AND "CYCLE_YEAR_MONTH" = (
            SELECT MIN("CYCLE_YEAR_MONTH")
            FROM "OG_LEASE_CYCLE"
            WHERE "LEASE_NO" = :lease_no
            AND "DISTRICT_NO" = :district_no
        );
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchone()

    # Сумма за первые 3 месяца
    first_3_months = db.execute(
        text(f"""
        SELECT
            SUM("LEASE_OIL_PROD_VOL") AS total_oil,
            SUM("{gas_field}") AS total_gas,
            SUM("LEASE_COND_PROD_VOL") AS total_condensate
        FROM "OG_LEASE_CYCLE"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no
        AND to_date("CYCLE_YEAR_MONTH", 'YYYYMM') <= (
            SELECT to_date(MIN("CYCLE_YEAR_MONTH"), 'YYYYMM') + INTERVAL '2 months'
            FROM "OG_LEASE_CYCLE"
            WHERE "LEASE_NO" = :lease_no
            AND "DISTRICT_NO" = :district_no
        );
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchone()

    # Сумма за первые 6 месяцев
    first_6_months = db.execute(
        text(f"""
        SELECT
            SUM("LEASE_OIL_PROD_VOL") AS total_oil,
            SUM("{gas_field}") AS total_gas,
            SUM("LEASE_COND_PROD_VOL") AS total_condensate
        FROM "OG_LEASE_CYCLE"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no
        AND to_date("CYCLE_YEAR_MONTH", 'YYYYMM') <= (
            SELECT to_date(MIN("CYCLE_YEAR_MONTH"), 'YYYYMM') + INTERVAL '5 months'
            FROM "OG_LEASE_CYCLE"
            WHERE "LEASE_NO" = :lease_no
            AND "DISTRICT_NO" = :district_no
        );
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchone()

    # Сумма за первые 12 месяцев
    first_12_months = db.execute(
        text(f"""
        SELECT
            SUM("LEASE_OIL_PROD_VOL") AS total_oil,
            SUM("{gas_field}") AS total_gas,
            SUM("LEASE_COND_PROD_VOL") AS total_condensate
        FROM "OG_LEASE_CYCLE"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no
        AND to_date("CYCLE_YEAR_MONTH", 'YYYYMM') <= (
            SELECT to_date(MIN("CYCLE_YEAR_MONTH"), 'YYYYMM') + INTERVAL '11 months'
            FROM "OG_LEASE_CYCLE"
            WHERE "LEASE_NO" = :lease_no
            AND "DISTRICT_NO" = :district_no
        );
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchone()

    # Сумма за всё время работы скважины
    all_time = db.execute(
        text(f"""
        SELECT
            SUM("LEASE_OIL_PROD_VOL") AS total_oil,
            SUM("{gas_field}") AS total_gas,
            SUM("LEASE_COND_PROD_VOL") AS total_condensate
        FROM "OG_LEASE_CYCLE"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no;
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchone()

    return {
        "first_month": first_month,
        "first_3_months": first_3_months,
        "first_6_months": first_6_months,
        "first_12_months": first_12_months,
        "all_time": all_time
    }


def get_related_apis(db: Session, lease_no: str, district_no: str):
    return db.execute(
        text("""
        SELECT DISTINCT "API_COUNTY_CODE", "API_UNIQUE_NO"
        FROM "OG_WELL_COMPLETION"
        WHERE "LEASE_NO" = :lease_no
        AND "DISTRICT_NO" = :district_no;
        """), {'lease_no': lease_no, 'district_no': district_no}).fetchall()
