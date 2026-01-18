def get_education_loan_schemes(score):
    """
    Returns suitable education loan schemes based on approval score
    """

    # 🔥 80–100 : Strong Profile
    if score >= 80:
        return {
            "profile_strength": "Strong Education Profile",
            "ui_label": "Bank loan likely — excellent approval odds",
            "schemes": [
                {
                    "provider": "State Bank of India (SBI)",
                    "scheme_name": "SBI Education Loan",
                    "amount": "Up to ₹1 Cr",
                    "interest_rate": "8.15% – 11.15% p.a",
                    "tenure": "Up to 15 years",
                    "best_for": "Top colleges, abroad or India",
                    "notes": "Covers tuition, living expenses & travel",
                    "link": "https://sbi.co.in/web/personal-banking/loans/education-loans",
                    "ui_label": "Low‑interest long‑term loan"
                },
                {
                    "provider": "Punjab National Bank (PNB)",
                    "scheme_name": "PNB Education Loan",
                    "amount": "Up to ₹1 Cr",
                    "interest_rate": "8.90% – 11.50% p.a",
                    "tenure": "Up to 15 years",
                    "best_for": "Undergrad & Postgrad abroad/India",
                    "notes": "PSU bank loan with flexible terms",
                    "link": "https://www.pnbindia.in/en/personaloan/education-loan",
                    "ui_label": "PSU bank loan — strong approval"
                }
            ]
        }

    # 👍 60–79 : Moderate Profile
    elif score >= 60:
        return {
            "profile_strength": "Moderate Education Profile",
            "ui_label": "Bank/NBFC loan possible with conditions",
            "schemes": [
                {
                    "provider": "Canara Bank",
                    "scheme_name": "Canara Bank Education Loan",
                    "amount": "Up to ₹75 Lakh",
                    "interest_rate": "8.50% – 12.00% p.a",
                    "tenure": "Up to 15 years",
                    "best_for": "Co‑applicant/Collateral cases",
                    "notes": "Traditional bank loan option",
                    "link": "https://www.canarabank.in/english/personal-banking/loans/education-loans",
                    "ui_label": "Bank loan — co‑applicant helps"
                },
                {
                    "provider": "Tata Capital",
                    "scheme_name": "Tata Capital Education Loan",
                    "amount": "₹50,000 – ₹50 Lakh",
                    "interest_rate": "9.50% – 18.00% p.a",
                    "tenure": "Up to 10 years",
                    "best_for": "Fast processing, flexible docs",
                    "notes": "NBFC loan with quicker approvals",
                    "link": "https://www.tatacapital.com/education-loan.html",
                    "ui_label": "NBFC loan — quick & flexible"
                }
            ]
        }

    # ⚠️ 40–59 : Fair Profile
    elif score >= 40:
        return {
            "profile_strength": "Fair Education Profile",
            "ui_label": "Alternate lender options",
            "schemes": [
                {
                    "provider": "HDFC Credila",
                    "scheme_name": "Credila Education Loan",
                    "amount": "Up to ₹75 Lakh",
                    "interest_rate": "11.25%+ p.a",
                    "tenure": "Medium term",
                    "best_for": "Abroad & India studies",
                    "notes": "NBFC education loan, flexible eligibility",
                    "link": "https://www.credila.com",
                    "ui_label": "NBFC/alternate loan"
                },
                {
                    "provider": "Auxilo",
                    "scheme_name": "Auxilo Education Loan",
                    "amount": "Up to ₹1 Cr",
                    "interest_rate": "12.00%+ p.a",
                    "tenure": "Up to 15 years",
                    "best_for": "India & foreign universities",
                    "notes": "Flexible for partially secured cases",
                    "link": "https://www.auxilo.com",
                    "ui_label": "Alternative lender loan"
                }
            ]
        }

    # ❌ <40 : Low Profile
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
                    "notes": "Work on income/credit to become eligible",
                    "link": "#",
                    "ui_label": "Improve profile to unlock loans"
                }
            ]
        }
