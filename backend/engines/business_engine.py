from formulas.business_loan import calculate_business_loan_score
from utils.meter_mapper import generate_meter
from utils.insight_generator import business_loan_insights
from schemes.business_scheme import get_business_loan_schemes


def process_business_loan(data):

    # ===== HARD CAST + FAIL SAFE (CRITICAL) =====
    clean_data = {
        "business_age": int(data.get("business_age") or 0),
        "annual_revenue": int(data.get("annual_revenue") or 0),
        "monthly_expenses": int(data.get("monthly_expenses") or 0),
        "credit_score": int(data.get("credit_score") or 0),
        "existing_emis": int(data.get("existing_emis") or 0)
    }

    # ✅ SINGLE SOURCE OF TRUTH
    raw_score = calculate_business_loan_score(clean_data)

    # ✅ meter always derived from raw_score
    meter = generate_meter(raw_score)

    insights = business_loan_insights(clean_data, raw_score)

    schemes = get_business_loan_schemes(meter["approval_percentage"])

    return {
        "loan_type": "Business Loan",
        "raw_score": raw_score,          # debug / consistency
        **meter,                         # approval_percentage
        "insights": insights,
        "recommended_schemes": schemes
    }

