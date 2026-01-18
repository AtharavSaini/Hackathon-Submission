from flask import Flask, request, jsonify
from flask_cors import CORS

# ===== Engines Imports =====
from engines.education_engine import process_education_loan
from engines.personal_engine import process_personal_loan
from engines.business_engine import process_business_loan
from engines.medical_engine import process_medical_loan
from engines.investment_engine import process_investment

app = Flask(__name__)
CORS(app)

# ================= HEALTH CHECK =================
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "Backend running successfully",
        "available_types": [
            "education",
            "personal",
            "business",
            "medical",
            "investment"
        ]
    })

# ================= MAIN ANALYZE ROUTE =================
@app.route("/analyze", methods=["POST", "OPTIONS"])
def analyze():

    # ✅ CORS PREFLIGHT FIX
    if request.method == "OPTIONS":
        return jsonify({"status": "OK"}), 200

    data = request.get_json(silent=True, force=True)

    if not data:
        return jsonify({"error": "Request body missing"}), 400

    if "type" not in data:
        return jsonify({"error": "type field missing"}), 400

    loan_type = data["type"].lower()

    try:
        if loan_type == "education":
            result = process_education_loan(data)
        elif loan_type == "personal":
            result = process_personal_loan(data)
        elif loan_type == "business":
            result = process_business_loan(data)
        elif loan_type == "medical":
            result = process_medical_loan(data)
        elif loan_type == "investment":
            result = process_investment(data)
        else:
            return jsonify({"error": "Invalid loan / investment type"}), 400

        return jsonify(result)

    except Exception as e:
        print("🔥 ANALYZE ERROR DATA:", data)
        return jsonify({
            "error": "Internal processing error",
            "details": str(e)
        }), 500


# ================= FRONTEND COMPATIBILITY ROUTE =================
@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():

    # ✅ CORS PREFLIGHT FIX
    if request.method == "OPTIONS":
        return jsonify({"status": "OK"}), 200

    data = request.get_json(silent=True, force=True)

    if not data:
        return jsonify({"error": "Request body missing"}), 400

    # frontend sends loan_type, backend expects type
    if "loan_type" in data and "type" not in data:
        data["type"] = data["loan_type"]

    if "type" not in data:
        return jsonify({"error": "loan type missing"}), 400

    loan_type = data["type"].lower()

    try:
        if loan_type == "education":
            result = process_education_loan(data)
        elif loan_type == "personal":
            result = process_personal_loan(data)
        elif loan_type == "business":
            result = process_business_loan(data)
        elif loan_type == "medical":
            result = process_medical_loan(data)
        elif loan_type == "investment":
            result = process_investment(data)
        else:
            return jsonify({"error": "Invalid loan / investment type"}), 400

        return jsonify(result)

    except Exception as e:
        print("🔥 PREDICT ERROR DATA:", data)
        return jsonify({
            "error": "Internal processing error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)







