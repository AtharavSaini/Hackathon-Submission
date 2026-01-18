from formulas.education_loan import calculate_education_loan_score
from utils.meter_mapper import generate_meter
from utils.insight_generator import education_loan_insights
from schemes.education_scheme import get_education_loan_schemes


def process_education_loan(data):

    # ===== HARD CAST + FAIL-SAFE (VERY IMPORTANT) =====
    clean_data = {
        "course_type": data.get("course_type") or "General",
        "college_type": data.get("college_type") or "Other",
        "course_fee": int(data.get("course_fee") or 1),
        "family_income": int(data.get("family_income") or 1),
        "credit_score": int(data.get("credit_score") or 0),
        "co_applicant": data.get("co_applicant") or "No",
        "collateral": data.get("collateral") or "No"
    }

    # ✅ SINGLE SOURCE OF TRUTH
    raw_score = calculate_education_loan_score(clean_data)

    # ✅ meter ALWAYS derived from raw_score
    meter = generate_meter(raw_score)

    # ✅ insights based on clean data + raw_score
    insights = education_loan_insights(clean_data, raw_score)

    print("🎓 RAW SCORE:", raw_score)
    print("🎓 METER SCORE:", meter["approval_percentage"])

    # ✅ schemes ALWAYS from meter score (NOT raw_score directly)
    schemes = get_education_loan_schemes(meter["approval_percentage"])

    return {
        "loan_type": "Education Loan",
        "raw_score": raw_score,              # debug / analytics
        **meter,                             # approval_percentage, label
        "insights": insights,
        "recommended_schemes": schemes
    }

