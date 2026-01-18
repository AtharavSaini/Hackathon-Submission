def get_personal_loan_schemes(score):
    """
    Returns suitable personal loan options
    based on approval probability score
    """

    # 🔥 80–100 : Strong Personal Loan Profile
    if score >= 80:
        return {
            "profile_strength": "Strong Personal Loan Profile",
            "ui_label": "Low-interest personal loan – best fit for your score",
            "schemes": [
                {
                    "provider": "HDFC Bank",
                    "scheme_name": "HDFC Personal Loan",
                    "amount": "Up to ₹40L",
                    "interest_rate": "10.5% – 15% p.a",
                    "tenure": "Up to 6 years",
                    "best_for": "High credit score & stable salaried income",
                    "notes": "Fast digital approval",
                    "link": "https://www.hdfcbank.com/personal/borrow/popular-loans/personal-loan",
                    "ui_tag": "Low-interest personal loan – best fit for your score"
                },
                {
                    "provider": "ICICI Bank",
                    "scheme_name": "ICICI Personal Loan",
                    "amount": "Up to ₹50L",
                    "interest_rate": "10.85%+ p.a",
                    "tenure": "Flexible",
                    "best_for": "Premium salaried profiles",
                    "notes": "Instant approval for eligible users",
                    "link": "https://www.icicibank.com/personal-banking/loans/personal-loan",
                    "ui_tag": "Premium bank personal loan"
                }
            ]
        }

    # 🟡 60–79 : Moderate Profile
    elif score >= 60:
        return {
            "profile_strength": "Moderate Personal Loan Profile",
            "ui_label": "Bank / NBFC loan possible with conditions",
            "schemes": [
                {
                    "provider": "Axis Bank",
                    "scheme_name": "Axis Bank Personal Loan",
                    "amount": "Up to ₹40L",
                    "interest_rate": "11% – 20% p.a",
                    "tenure": "Up to 6 years",
                    "best_for": "Decent credit with moderate FOIR",
                    "notes": "Eligibility flexible",
                    "link": "https://www.axisbank.com/retail/loans/personal-loan",
                    "ui_tag": "Bank loan possible with conditions"
                },
                {
                    "provider": "Tata Capital",
                    "scheme_name": "Tata Capital Personal Loan",
                    "amount": "₹75k – ₹35L",
                    "interest_rate": "12% – 20% p.a",
                    "tenure": "Flexible",
                    "best_for": "Users needing faster approval",
                    "notes": "Quicker processing than banks",
                    "link": "https://www.tatacapital.com/personal-loan.html",
                    "ui_tag": "NBFC personal loan – quicker processing"
                }
            ]
        }

    # 🟠 40–59 : Weak but Possible
    elif score >= 40:
        return {
            "profile_strength": "Weak but Possible Personal Loan Profile",
            "ui_label": "High-cost but accessible personal loan",
            "schemes": [
                {
                    "provider": "Bajaj Finserv",
                    "scheme_name": "Bajaj Finserv Personal Loan",
                    "amount": "₹20k – ₹50L",
                    "interest_rate": "13% – 24% p.a",
                    "tenure": "Short to medium",
                    "best_for": "Lower credit or self-employed users",
                    "notes": "Very fast disbursal",
                    "link": "https://www.bajajfinserv.in/personal-loan",
                    "ui_tag": "High-cost but accessible personal loan"
                },
                {
                    "provider": "MoneyTap / PaySense",
                    "scheme_name": "Fintech Credit Line / Personal Loan",
                    "amount": "Small to medium",
                    "interest_rate": "Higher (risk-based)",
                    "tenure": "Short-term",
                    "best_for": "Emergency needs",
                    "notes": "Use cautiously due to higher cost",
                    "link": "https://www.moneytap.com",
                    "ui_tag": "Fintech option – use cautiously"
                }
            ]
        }

    # 🔴 <40 : High Risk
    else:
        return {
            "profile_strength": "High Risk Profile",
            "ui_label": "No loans available for this score",
            "schemes": [
            {
                "provider": "No Eligible Loans",
                "scheme_name": "Currently Not Eligible",
                "amount": "--",
                "interest_rate": "--",
                "tenure": "--",
                "best_for": "Improve profile to unlock loans",
                "notes": "Increase income, reduce EMIs or improve credit score",
                "link": "#",
                "ui_label": "Improve profile to unlock loans"
            }
        ]
        }
