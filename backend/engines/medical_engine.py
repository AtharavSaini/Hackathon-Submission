from formulas.medical_loan import calculate_medical_loan_score
from utils.meter_mapper import generate_meter
from utils.insight_generator import medical_loan_insights
from schemes.medical_scheme import get_medical_loan_schemes

def process_medical_loan(data):

    # ===== HARD CAST + FAIL-SAFE =====
    clean_data = {
        "treatment_cost": int(data.get("treatment_cost") or 1),
        "monthly_income": int(data.get("monthly_income") or 1),
        "credit_score": int(data.get("credit_score") or 0),
        "existing_emis": int(data.get("existing_emis") or 0),
        "insurance": data.get("insurance") or "No"
    }

    # ✅ SINGLE SOURCE OF TRUTH
    raw_score = calculate_medical_loan_score(clean_data)

    # ✅ meter always derived from raw_score
    meter = generate_meter(raw_score)

    insights = medical_loan_insights(clean_data, raw_score)

    print("🔥 RAW SCORE:", raw_score)
    print("🔥 METER SCORE:", meter["approval_percentage"])
    schemes = get_medical_loan_schemes(meter["approval_percentage"])



    return {
        "loan_type": "Medical Loan",
        "raw_score": raw_score,                  # debug / future use
        **meter,                                 # approval_percentage
        "insights": insights,
        "recommended_schemes": schemes
    }




