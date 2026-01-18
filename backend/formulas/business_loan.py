def calculate_business_loan_score(data):
    score = 0

    # 1️⃣ Business Age
    age = data.get("business_age", 0)
    if age >= 5: score += 20
    elif age >= 3: score += 14
    elif age >= 1: score += 8
    else: score -= 10

    # 2️⃣ Net Cash Flow
    revenue = data.get("annual_revenue", 0) / 12
    expenses = data.get("monthly_expenses", 0)
    cash_flow = revenue - expenses

    if cash_flow >= 100000: score += 25
    elif cash_flow >= 50000: score += 18
    elif cash_flow >= 20000: score += 10
    else: score -= 10

    # 3️⃣ Revenue Scale
    if revenue >= 500000: score += 20
    elif revenue >= 200000: score += 14
    else: score += 6

    # 4️⃣ Credit Score
    cs = data.get("credit_score", 0)
    if cs >= 750: score += 20
    elif cs >= 700: score += 14
    elif cs >= 650: score += 8
    else: score -= 10

    # 5️⃣ Debt Burden
    emis = data.get("existing_emis", 0)
    foir = emis / max(1, cash_flow)

    if foir <= 0.3: score += 15
    elif foir <= 0.5: score += 8
    else: score -= 10

    return max(0, min(100, round(score)))
