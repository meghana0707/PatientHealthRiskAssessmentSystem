
from flask import Flask, render_template, request
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)

# Load saved model and preprocessing encoders
MODEL_PATH = Path(__file__).resolve().parent / "patient_health_risk_model.pkl"

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
encoders = saved_data["encoders"]
FEATURE_COLUMNS = saved_data["columns"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get patient details from the form
        age = int(request.form["age"])
        gender_text = request.form["gender"]
        blood_pressure = float(request.form["blood_pressure"])
        glucose = float(request.form["glucose"])
        bmi = float(request.form["bmi"])
        cholesterol = float(request.form["cholesterol"])
        smoking_text = request.form["smoking"]
        activity_text = request.form["activity"]

        # Validate input values
        if not 1 <= age <= 120:
            raise ValueError("Age must be between 1 and 120.")

        if min(blood_pressure, glucose, bmi, cholesterol) <= 0:
            raise ValueError("Health measurements must be positive.")

        # Use the same encoders as the trained model
        gender = encoders["Gender"].transform([gender_text])[0]
        smoking = encoders["Smoking"].transform([smoking_text])[0]
        activity = encoders["Physical Activity"].transform(
            [activity_text]
        )[0]

        # Prepare patient data in training column order
        patient_values = {
            "Age": age,
            "Gender": gender,
            "Blood Pressure": blood_pressure,
            "Blood Glucose": glucose,
            "BMI": bmi,
            "Cholesterol": cholesterol,
            "Smoking": smoking,
            "Physical Activity": activity
        }

        patient = pd.DataFrame(
            [[patient_values[col] for col in FEATURE_COLUMNS]],
            columns=FEATURE_COLUMNS
        )

        # Predict health risk
        prediction = model.predict(patient)[0]

        risk = encoders["Health Risk"].inverse_transform(
            [prediction]
        )[0]

        return render_template(
            "result.html",
            risk=risk,
            age=age
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "index.html",
            error=str(error)
        ), 400

    except Exception:
        app.logger.exception("Prediction error")
        return render_template(
            "index.html",
            error="Prediction failed. Please check the model and input data."
        ), 500


if __name__ == "__main__":
    app.run(debug=True)
