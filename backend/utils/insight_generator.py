def education_loan_insights(data, score):
    insights = []

    if data.get("college_tier") == "Tier 3":
        insights.append({
            "issue": "College reputation is low",
            "impact": "Banks prefer reputed institutes",
            "improvement": "Choose better institute or add strong co‑applicant"
        })

    fees = data.get("annual_fees", 1)
    income = data.get("family_income", 1)

    if fees / income > 0.7:
        insights.append({
            "issue": "High fee to income ratio",
            "impact": "High repayment stress",
            "improvement": "Reduce loan or increase co‑applicant income"
        })

    if data.get("co_applicant") == "No":
        insights.append({
            "issue": "No co‑applicant",
            "impact": "Higher risk for banks",
            "improvement": "Add parent or guardian"
        })

    return {
        "overall_score": score,
        "summary": (
            "Strong profile"
            if score >= 75
            else "Moderate profile"
            if score >= 50
            else "High risk profile"
        ),
        "insights": insights
    }



def personal_loan_insights(data, score):
    insights = []

    # Credit Score
    cs = data.get("credit_score", 0)
    if cs < 700:
        insights.append({
            "issue": "Low credit score",
            "impact": "Banks consider past repayment behavior risky",
            "improvement": "Pay EMIs on time and reduce credit card utilization"
        })

    # Income
    income = data.get("monthly_income", 0)
    if income < 30000:
        insights.append({
            "issue": "Low monthly income",
            "impact": "Limited repayment capacity",
            "improvement": "Increase income proof or apply with a co-applicant"
        })

    # FOIR
    emis = data.get("existing_emis", 0)
    income_safe = max(1, income)
    foir = emis / income_safe

    if foir > 0.5:
        insights.append({
            "issue": "High EMI burden",
            "impact": "Most income already committed to liabilities",
            "improvement": "Close existing loans or reduce loan amount"
        })

    # Job Stability
    if data.get("job_experience", 0) < 2:
        insights.append({
            "issue": "Low job stability",
            "impact": "Banks prefer stable income history",
            "improvement": "Gain more work experience before applying"
        })

    # Age Risk
    age = data.get("age", 0)
    if age < 21 or age > 55:
        insights.append({
            "issue": "Age outside preferred lending range",
            "impact": "Higher default probability perceived by banks",
            "improvement": "Apply with a co-applicant within ideal age range"
        })

    return {
        "overall_score": score,
        "summary": "Strong borrower profile" if score >= 75 else "Average borrower profile" if score >= 50 else "High risk borrower profile",
        "insights": insights
    }


def business_loan_insights(data, score):
    insights = []

    if data.get("startup_stage") in ["Idea", "MVP"]:
        insights.append({
            "issue": "Startup is at an early stage",
            "impact": "Most investors prefer validated traction",
            "improvement": "Build MVP users or early revenue before pitching"
        })

    if data.get("monthly_revenue", 0) == 0:
        insights.append({
            "issue": "No revenue yet",
            "impact": "Revenue validates market demand",
            "improvement": "Focus on monetization or pilot customers"
        })

    if data.get("user_growth_rate", 0) < 5:
        insights.append({
            "issue": "Low user growth",
            "impact": "Growth indicates scalability",
            "improvement": "Improve acquisition channels and retention"
        })

    if data.get("founder_experience") == "No":
        insights.append({
            "issue": "Founders lack prior experience",
            "impact": "Execution risk increases",
            "improvement": "Add experienced advisors or co-founders"
        })

    return {
        "overall_score": score,
        "summary": (
            "High investor interest"
            if score >= 75
            else "Moderate investor interest"
            if score >= 50
            else "Low investor interest"
        ),
        "insights": insights
    }
def business_loan_insights(data, score):
    insights = []

    # 1️⃣ Business Age
    age = data.get("business_age", 0)
    if age < 3:
        insights.append({
            "issue": "Business is relatively new",
            "impact": "Banks prefer businesses with stable operating history",
            "improvement": "Complete at least 3 years of operations or apply via NBFC/government schemes"
        })

    # 2️⃣ Cash Flow Health
    revenue = data.get("annual_revenue", 0) / 12
    expenses = data.get("monthly_expenses", 0)
    cash_flow = revenue - expenses

    if cash_flow < 20000:
        insights.append({
            "issue": "Weak monthly cash flow",
            "impact": "Low surplus reduces repayment confidence",
            "improvement": "Reduce operating expenses or improve revenue consistency"
        })

    # 3️⃣ Revenue Scale
    if revenue < 200000:
        insights.append({
            "issue": "Business revenue is on the lower side",
            "impact": "Lower scale businesses face tighter lending limits",
            "improvement": "Show growth trend, GST returns, or future contracts"
        })

    # 4️⃣ Credit Score
    cs = data.get("credit_score", 0)
    if cs < 700:
        insights.append({
            "issue": "Business owner credit score is low",
            "impact": "Credit history strongly affects loan approval",
            "improvement": "Clear pending dues and improve credit utilization"
        })

    # 5️⃣ Debt Burden (FOIR)
    emis = data.get("existing_emis", 0)
    foir = emis / max(1, cash_flow)

    if foir > 0.5:
        insights.append({
            "issue": "High existing EMI burden",
            "impact": "Most cash flow already committed to liabilities",
            "improvement": "Reduce EMIs or opt for longer tenure / lower loan amount"
        })

    return {
        "overall_score": score,
        "summary": (
            "Strong business profile"
            if score >= 75
            else "Moderate business risk"
            if score >= 50
            else "High risk business profile"
        ),
        "insights": insights
    }


def medical_loan_insights(data, score):
    insights = []

    # 1️⃣ Treatment Cost vs Income
    cost = data.get("treatment_cost", 0)
    income = data.get("monthly_income", 1)
    ratio = cost / (income * 12)

    if ratio > 1:
        insights.append({
            "issue": "Treatment cost is very high compared to income",
            "impact": "Repayment may cause financial stress",
            "improvement": "Use insurance, reduce loan amount, or opt for longer tenure"
        })
    elif ratio > 0.5:
        insights.append({
            "issue": "Treatment cost is moderately high",
            "impact": "Banks may reduce approved amount",
            "improvement": "Add co-applicant income or partial insurance coverage"
        })

    # 2️⃣ Credit Score
    cs = data.get("credit_score", 0)
    if cs < 700:
        insights.append({
            "issue": "Credit score is below preferred range",
            "impact": "Higher interest rate or rejection risk",
            "improvement": "Clear past dues and avoid new credit before applying"
        })

    # 3️⃣ Insurance Coverage
    if data.get("insurance") != "Yes":
        insights.append({
            "issue": "No medical insurance coverage",
            "impact": "Entire treatment cost depends on borrowing",
            "improvement": "Check hospital EMI plans or government health schemes"
        })

    # 4️⃣ EMI Burden (FOIR)
    emis = data.get("existing_emis", 0)
    foir = emis / max(1, income)

    if foir > 0.5:
        insights.append({
            "issue": "High existing EMI burden",
            "impact": "Limited monthly repayment capacity",
            "improvement": "Close or reduce existing loans before taking a medical loan"
        })

    return {
        "overall_score": score,
        "summary": (
            "Strong medical loan profile"
            if score >= 75
            else "Moderate medical loan risk"
            if score >= 50
            else "High risk medical loan profile"
        ),
        "insights": insights
    }

def investment_insights(data, score):
    insights = []

    # 1️⃣ Startup Stage
    stage = data.get("startup_stage")
    if stage in ["Idea", "MVP"]:
        insights.append({
            "issue": "Startup is at an early stage",
            "impact": "Most VCs prefer revenue or strong traction before investing",
            "improvement": "Focus on achieving product-market fit and early users"
        })

    # 2️⃣ Revenue
    revenue = data.get("monthly_revenue", 0)
    if revenue == 0:
        insights.append({
            "issue": "No revenue yet",
            "impact": "Revenue validates demand and reduces investor risk",
            "improvement": "Introduce monetization or pilot customers"
        })
    elif revenue < 100000:
        insights.append({
            "issue": "Low monthly revenue",
            "impact": "Limits valuation and VC interest",
            "improvement": "Improve sales funnel and customer acquisition"
        })

    # 3️⃣ User Growth
    growth = data.get("user_growth_rate", 0)
    if growth < 5:
        insights.append({
            "issue": "Slow user growth",
            "impact": "Low scalability signal for investors",
            "improvement": "Strengthen marketing channels and retention strategy"
        })

    # 4️⃣ Founder Experience
    if data.get("founder_experience") == "No":
        insights.append({
            "issue": "Founders lack prior startup experience",
            "impact": "Execution risk appears higher to investors",
            "improvement": "Add experienced co-founders or advisors"
        })

    # 5️⃣ Funding Ask vs Revenue
    ask = data.get("funding_required", 0)
    revenue_safe = max(1, revenue)
    ask_ratio = ask / (revenue_safe * 12)

    if ask_ratio > 5:
        insights.append({
            "issue": "Funding ask is high compared to revenue",
            "impact": "Unrealistic ask can reduce investor confidence",
            "improvement": "Lower ask or justify with strong growth projections"
        })

    return {
        "overall_score": score,
        "summary": (
            "High investor interest"
            if score >= 75
            else "Moderate investor interest"
            if score >= 50
            else "Low investor interest"
        ),
        "insights": insights
    }
