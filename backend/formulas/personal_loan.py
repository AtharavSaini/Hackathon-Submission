def calculate_personal_loan_score(data):
    score = 0

    # ===== SAFE TYPE CASTING + KEY FIX =====
    cs = int(data.get("credit_score", 0))
    income = int(data.get("monthly_income", 0))
    emis = int(data.get("monthly_emi", 0))          # FIXED KEY
    experience = int(data.get("experience_years", 0))  # FIXED KEY
    age = int(data.get("age", 0))

    # 1️⃣ Credit Score (30%)
    if cs >= 800:
        score += 30
    elif cs >= 750:
        score += 25
    elif cs >= 700:
        score += 18
    elif cs >= 650:
        score += 10
    else:
        score -= 15

    # 2️⃣ Monthly Income (25%)
    if income >= 100000:
        score += 25
    elif income >= 60000:
        score += 18
    elif income >= 30000:
        score += 10
    else:
        score -= 10

    # 3️⃣ FOIR (20%)
    income_safe = max(1, income)
    foir = emis / income_safe

    if foir <= 0.3:
        score += 20
    elif foir <= 0.5:
        score += 12
    elif foir <= 0.65:
        score += 5
    else:
        score -= 15

    # 4️⃣ Job Stability (15%)
    if experience >= 5:
        score += 15
    elif experience >= 2:
        score += 10
    else:
        score += 3

    # 5️⃣ Age Factor (10%)
    if 23 <= age <= 55:
        score += 10
    else:
        score -= 5

    # 🎯 Final normalize
    final_score = max(0, min(100, round(score)))
    return final_score


