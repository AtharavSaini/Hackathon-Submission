def get_business_loan_schemes(score):
    """
    Returns suitable business / SME loan options
    based on approval score
    """

    # 🔥 80–100 : Strong Business Profile
    if score >= 80:
        return {
            "profile_strength": "Strong Business Profile",
            "ui_label": "Low-risk bank business loan",
            "schemes": [
                {
                    "provider": "State Bank of India (SBI)",
                    "scheme_name": "SBI SME / Business Loan",
                    "amount": "₹10L – ₹5 Cr",
                    "interest_rate": "9% – 12% p.a",
                    "tenure": "1 – 10 years",
                    "best_for": "Established MSMEs with strong cash flow",
                    "notes": "Best suited for old businesses with good credit",
                    "link": "https://sbi.co.in/web/business/sme/sme-loans",
                    "ui_tag": "Low-risk bank business loan"
                },
                {
                    "provider": "HDFC Bank",
                    "scheme_name": "HDFC Business Loan",
                    "amount": "Up to ₹75L",
                    "interest_rate": "10.5%+ p.a",
                    "tenure": "Flexible",
                    "best_for": "Businesses with strong turnover",
                    "notes": "Faster than PSU banks",
                    "link": "https://www.hdfcbank.com/sme/borrow/loans/business-loan",
                    "ui_tag": "Private bank – strong cash flow fit"
                }
            ]
        }

    # 🟡 60–79 : Moderate Business Profile
    elif score >= 60:
        return {
            "profile_strength": "Moderate Business Profile",
            "ui_label": "NBFC loan – growth-stage businesses",
            "schemes": [
                {
                    "provider": "Tata Capital",
                    "scheme_name": "Tata Capital Business Loan",
                    "amount": "₹5L – ₹2 Cr",
                    "interest_rate": "12% – 18% p.a",
                    "tenure": "Flexible",
                    "best_for": "Growing businesses",
                    "notes": "Flexible eligibility criteria",
                    "link": "https://www.tatacapital.com/business-loan.html",
                    "ui_tag": "NBFC loan – growth-stage businesses"
                },
                {
                    "provider": "Bajaj Finserv",
                    "scheme_name": "Bajaj Finserv Business Finance",
                    "amount": "Up to ₹50L",
                    "interest_rate": "13% – 18% p.a",
                    "tenure": "Short to medium",
                    "best_for": "Working capital needs",
                    "notes": "Fast approval & disbursal",
                    "link": "https://www.bajajfinserv.in/business-loan",
                    "ui_tag": "Fast NBFC funding option"
                }
            ]
        }

    # 🟠 40–59 : Weak but Possible
    elif score >= 40:
        return {
            "profile_strength": "Weak but Possible Business Profile",
            "ui_label": "Government & fintech support options",
            "schemes": [
                {
                    "provider": "Government of India",
                    "scheme_name": "Mudra Loan (PMMY)",
                    "amount": "Up to ₹10L",
                    "interest_rate": "As per bank",
                    "tenure": "Flexible",
                    "best_for": "Small & micro businesses",
                    "notes": "Government-backed MSME support",
                    "link": "https://www.mudra.org.in",
                    "ui_tag": "Government MSME support loan"
                },
                {
                    "provider": "Lendingkart",
                    "scheme_name": "Lendingkart Business Loan",
                    "amount": "₹50,000 – ₹2 Cr",
                    "interest_rate": "Higher (risk-based)",
                    "tenure": "Short-term",
                    "best_for": "Young businesses with limited credit",
                    "notes": "Minimal paperwork, faster approval",
                    "link": "https://www.lendingkart.com",
                    "ui_tag": "Fintech loan – easier but costly"
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
