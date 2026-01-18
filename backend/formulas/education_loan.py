def calculate_education_loan_score(data):
    score = 0

    # 1️⃣ Institute Quality (25%)
    college_tier_weight = {
        "Tier 1": 25,
        "Tier 2": 18,
        "Tier 3": 12   # ⬅️ thoda boost
    }
    score += college_tier_weight.get(data.get("college_tier"), 10)

    # 2️⃣ Course Employability (20%) ✅ FIXED
    course_employability = {
        "Professional": 20,
        "General": 12
    }
    score += course_employability.get(data.get("course_type"), 10)

    # 3️⃣ Degree Level (10%)
    degree_weight = {
        "PhD": 10,
        "Postgraduate": 8,
        "Undergraduate": 6   # ⬅️ boost
    }
    score += degree_weight.get(data.get("degree_level"), 5)

    # 4️⃣ Affordability Ratio (20%) ✅ softened
    fees = max(1, int(data.get("annual_fees", 1)))
    income = max(1, int(data.get("family_income", 1)))
    ratio = fees / income

    if ratio <= 0.5:
        score += 20
    elif ratio <= 0.8:
        score += 15
    elif ratio <= 1.2:
        score += 10
    else:
        score -= 5   # ⬅️ earlier -10

    # 5️⃣ Co‑Applicant (10%) ✅ less penalty
    if data.get("co_applicant") == "Yes":
        score += 10
    else:
        score -= 5   # ⬅️ earlier -15

    # 6️⃣ Co‑Applicant Credit (15%)
    credit_score = int(data.get("co_applicant_credit_score", 0))

    if credit_score >= 800:
        score += 15
    elif credit_score >= 750:
        score += 12
    elif credit_score >= 700:
        score += 9
    elif credit_score >= 650:
        score += 6
    elif credit_score >= 600:
        score += 3
    else:
        score -= 5   # ⬅️ softened

    return max(0, min(100, round(score)))

