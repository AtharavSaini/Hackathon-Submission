def calculate_medical_loan_score(data):
    score = 0

    cost = max(1, int(data.get("treatment_cost", 1)))
    income = max(1, int(data.get("monthly_income", 1)))
    emis = max(0, int(data.get("existing_emis", 0)))
    cs = int(data.get("credit_score", 0))
    insurance = data.get("insurance", "No")

    # ===== COST vs INCOME (MAX 25) =====
    ratio = cost / (income * 12)
    if ratio <= 0.4:
        score += 25
    elif ratio <= 0.8:
        score += 15
    else:
        score += 5

    # ===== CREDIT SCORE (MAX 25) =====
    if cs >= 780:
        score += 25
    elif cs >= 720:
        score += 18
    elif cs >= 660:
        score += 10
    else:
        score += 0

    # ===== INSURANCE (MAX 10) =====
    if insurance == "Yes":
        score += 10

    # ===== FOIR (MAX 20) =====
    foir = emis / income
    if foir <= 0.25:
        score += 20
    elif foir <= 0.45:
        score += 10
    else:
        score += 0

    # 🔥 NO EMERGENCY BONUS
    return max(0, min(100, round(score)))







