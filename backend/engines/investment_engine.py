from formulas.investment_loan import calculate_investment_score
from utils.meter_mapper import generate_meter
from utils.insight_generator import investment_insights
from schemes.investment_scheme import get_investment_schemes


def normalize_text(val: str):
    if not val:
        return ""
    return (
        val.replace("‑", "-")   # 🔥 unicode dash
           .replace("–", "-")
           .strip()
    )


def sanitize_investment_data(data: dict):

    stage = normalize_text(data.get("startup_stage", "Idea"))
    industry = normalize_text(data.get("industry", "Other"))

    revenue = float(data.get("monthly_revenue") or 0)

    growth = float(data.get("growth_rate") or 0)
    # 🔥 HARD CLAMP BEFORE FORMULA
    if growth > 300:
        growth = 300
    if growth < 0:
        growth = 0

    experience = normalize_text(data.get("founder_experience", "No"))

    funding_map = {
        "₹0 - ₹50 Lakh": 50,
        "₹50 Lakh - ₹1 Crore": 100,
        "₹1 - ₹5 Crore": 300,
        "₹5+ Crore": 500
    }

    funding_raw = normalize_text(data.get("funding_required", ""))
    funding = funding_map.get(funding_raw, 100)

    return {
        "startup_stage": stage,
        "industry": industry,
        "monthly_revenue": revenue,
        "growth_rate": growth,
        "founder_experience": experience,
        "funding_required": funding
    }


def process_investment(data):
    try:
        safe_data = sanitize_investment_data(data)

        score = calculate_investment_score(safe_data)
        score = max(0, min(100, score))

        meter = generate_meter(score)
        insights = investment_insights(safe_data, score)
        schemes = get_investment_schemes(score)

        return {
            "loan_type": "Startup Investment",
            "score": score,
            **meter,
            "insights": insights,
            "recommended_schemes": schemes
        }

    except Exception as e:
        print("🔥 INVESTMENT ENGINE ERROR:", e)

        # 🔥 FAIL‑SAFE RESPONSE (NO 500)
        return {
            "loan_type": "Startup Investment",
            "score": 45,
            "meter_label": "Moderate",
            "meter_color": "orange",
            "insights": [
                {
                    "issue": "Insufficient investment data",
                    "impact": "Score generated using safe defaults",
                    "improvement": "Refine inputs for accurate analysis"
                }
            ],
            "recommended_schemes": []
        }



