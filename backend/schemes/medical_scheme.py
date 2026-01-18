def get_medical_loan_schemes(score):
    """
    Returns suitable medical loan / healthcare financing options
    based on approval score
    """

    # 🔥 80–100 : Strong Medical Profile
    if score >= 80:
        return {
            "profile_strength": "Strong Medical Profile",
            "ui_label": "Bank loan possible – strong repayment profile",
            "schemes": [
                {
                    "provider": "State Bank of India (SBI)",
                    "scheme_name": "SBI Medical / Personal Loan",
                    "amount": "₹50,000 – ₹20,00,000",
                    "interest_rate": "10% – 14% p.a",
                    "tenure": "1 – 6 years",
                    "best_for": "Planned or high-value treatments",
                    "notes": "Suitable for strong income and manageable EMIs",
                    "link": "https://sbi.co.in/web/personal-banking/loans/personal-loans",
                    "ui_label": "Bank loan possible – strong repayment profile"
                },
                {
                    "provider": "HDFC Bank",
                    "scheme_name": "HDFC Medical / Personal Loan",
                    "amount": "Up to ₹40,00,000",
                    "interest_rate": "10.5%+ p.a",
                    "tenure": "Flexible",
                    "best_for": "Fast approval, strong credit profile",
                    "notes": "Low-risk medical financing option",
                    "link": "https://www.hdfcbank.com/personal/borrow/popular-loans/personal-loan",
                    "ui_label": "Low-risk medical financing option"
                }
            ]
        }

    # 🟡 60–79 : Moderate Profile
    elif score >= 60:
        return {
            "profile_strength": "Moderate Medical Profile",
            "ui_label": "NBFC medical loan – fast & flexible",
            "schemes": [
                {
                    "provider": "Bajaj Finserv",
                    "scheme_name": "Bajaj Finserv Medical Loan",
                    "amount": "₹25,000 – ₹50,00,000",
                    "interest_rate": "11% – 18% p.a",
                    "tenure": "Short to medium",
                    "best_for": "Emergency medical needs",
                    "notes": "Very fast disbursal",
                    "link": "https://www.bajajfinserv.in/medical-loan",
                    "ui_label": "NBFC medical loan – fast & flexible"
                },
                {
                    "provider": "Tata Capital",
                    "scheme_name": "Tata Capital Healthcare Finance",
                    "amount": "Varies",
                    "interest_rate": "12% – 18% p.a",
                    "tenure": "Flexible",
                    "best_for": "Partial insurance coverage cases",
                    "notes": "Works when bank approval is uncertain",
                    "link": "https://www.tatacapital.com/medical-loans.html",
                    "ui_label": "Works when bank approval is uncertain"
                }
            ]
        }

    # 🟠 40–59 : Weak but Possible
    elif score >= 40:
        return {
            "profile_strength": "Weak but Possible Profile",
            "ui_label": "Emergency relief options – higher cost",
            "schemes": [
                {
                    "provider": "Care Health Insurance",
                    "scheme_name": "Insurance EMI / Cashless Tie-ups",
                    "amount": "Depends on policy",
                    "interest_rate": "Insurance based",
                    "tenure": "As per insurer",
                    "best_for": "Hospital cashless + EMI combos",
                    "notes": "Not a pure loan, but emergency relief",
                    "link": "https://www.careinsurance.com",
                    "ui_label": "Insurance-based EMI relief"
                },
                {
                    "provider": "MediBuddy / Rupeek",
                    "scheme_name": "Short-term / Gold-backed Funding",
                    "amount": "Varies",
                    "interest_rate": "Higher than banks",
                    "tenure": "Short-term",
                    "best_for": "Immediate emergency funding",
                    "notes": "Use cautiously",
                    "link": "https://www.medibuddy.in",
                    "ui_label": "Emergency relief options – higher cost"
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
