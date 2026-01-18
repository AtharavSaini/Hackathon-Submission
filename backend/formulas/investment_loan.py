def calculate_startup_investment_score(data):
    score = 0

    stage = data.get("startup_stage")
    if stage == "Scaling":
        score += 20
    elif stage == "Revenue":
        score += 16
    elif stage == "MVP":
        score += 10
    else:
        score += 5

    revenue = data.get("monthly_revenue", 0)
    if revenue >= 500000:
        score += 25
    elif revenue >= 100000:
        score += 18
    elif revenue > 0:
        score += 10
    else:
        score += 5

    growth = data.get("growth_rate", 0)
    if growth >= 20:
        score += 20
    elif growth >= 10:
        score += 14
    elif growth >= 5:
        score += 8
    else:
        score += 3

    if data.get("founder_experience") == "Yes":
        score += 20
    else:
        score += 8

    ask = data.get("funding_required", 1)
    ask_ratio = ask / max(1, revenue * 12)

    if ask_ratio <= 3:
        score += 15
    elif ask_ratio <= 5:
        score += 10
    else:
        score += 4

    return max(0, min(100, round(score)))


# 🔥 YE LINE ADD KAR — THIS IS THE KEY
calculate_investment_score = calculate_startup_investment_score

