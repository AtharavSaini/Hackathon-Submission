def generate_meter(score):
    probability = int(max(0, min(100, score)))

    if probability < 40:
        zone = "Red"
        label = "Low Approval Chance"
    elif probability < 60:
        zone = "Orange"
        label = "Below Average Chance"
    elif probability < 80:
        zone = "Yellow-Green"
        label = "Good Approval Chance"
    else:
        zone = "Green"
        label = "Very High Approval Chance"

    return {
        "approval_percentage": probability,
        "meter_zone": zone,
        "message": label
    }
