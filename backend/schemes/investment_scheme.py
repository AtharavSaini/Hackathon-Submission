def get_investment_schemes(score):
    """
    Returns startup / investment options based on profile score
    """

    if score >= 80:
        return [
            {
                "name": "VC / Angel Network",
                "ui_tag": "High-growth startup – strong investor interest",
                "description": "Top VCs, Angel investors, institutional funding",
                "examples": ["Sequoia", "Accel", "Lightspeed", "Indian Angel Network"]
            },
            {
                "name": "SIDBI / Govt Startup Funds",
                "ui_tag": "Government-backed growth capital",
                "description": "Lower risk institutional funding",
                "link": "https://www.sidbi.in"
            }
        ]

    elif score >= 60:
        return [
            {
                "name": "Angel Investors",
                "ui_tag": "Early-stage investment possible",
                "description": "Angel networks & early VCs",
                "examples": ["AngelList", "Indian Angel Network"]
            },
            {
                "name": "Startup India Seed Fund",
                "ui_tag": "Government seed support",
                "description": "Seed capital + mentoring",
                "link": "https://www.startupindia.gov.in"
            }
        ]

    elif score >= 40:
        return [
            {
                "name": "Bootstrapping + Grants",
                "ui_tag": "Equity funding risky at this stage",
                "description": "Grants, incubators, accelerators"
            },
            {
                "name": "Incubators / Accelerators",
                "ui_tag": "Mentorship-first funding",
                "examples": ["T-Hub", "NSRCEL IIMB", "Atal Incubation Centres"]
            }
        ]

    else:
        return [
            {
                "name": "Profile Improvement Stage",
                "ui_tag": "Investment not advised currently",
                "description": "Focus on traction, revenue & validation"
            }
        ]
