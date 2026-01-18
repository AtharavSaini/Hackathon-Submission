from formulas.personal_loan import calculate_personal_loan_score
from utils.meter_mapper import generate_meter
from utils.insight_generator import personal_loan_insights
from schemes.personal_scheme import get_personal_loan_schemes


def process_personal_loan(data):

    # ===== HARD CAST + FAIL-SAFE (SAME AS MEDICAL) =====
    clean_data = {
        "employment_type": data.get("employment_type") or "Unknown",
        "monthly_income": int(data.get("monthly_income") or 1),
        "experience_years": int(data.get("experience_years") or 0),
        "monthly_emi": int(data.get("monthly_emi") or 0),
        "credit_score": int(data.get("credit_score") or 0),
        "age": int(data.get("age") or 18)
    }

    # ✅ SINGLE SOURCE OF TRUTH
    raw_score = calculate_personal_loan_score(clean_data)

    # ✅ meter ALWAYS from raw_score
    meter = generate_meter(raw_score)

    insights = personal_loan_insights(clean_data, raw_score)

    print("🔥 PERSONAL RAW SCORE:", raw_score)
    print("🔥 PERSONAL METER SCORE:", meter["approval_percentage"])

    # ✅ schemes based on approval_percentage (NOT raw score)
    schemes = get_personal_loan_schemes(meter["approval_percentage"])

    return {
        "loan_type": "Personal Loan",
        "raw_score": raw_score,              # debug / parity with medical
        **meter,                             # approval_percentage
        "insights": insights,
        "recommended_schemes": schemes
    }




