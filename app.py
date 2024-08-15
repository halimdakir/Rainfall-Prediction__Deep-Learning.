from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf
import joblib
import traceback

app = Flask(__name__)

# Load the model & preprocessor
model_path = 'best_model.h5'
preprocessor_path = 'preprocessor.pkl'

# Attempt to load model and preprocessor
try:
    model = tf.keras.models.load_model(model_path)
    preprocessor = joblib.load(preprocessor_path)
    print("Model loaded successfully")
    print(model.summary())
except Exception as e:
    print("Failed to load model or preprocessor:", str(e))
    model = None  # Server won't run


@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model is not loaded'}), 500

    try:
        data = request.get_json(force=True)
        input_data = pd.DataFrame(data['data'])

        # Define expected columns
        expected_columns = [
            'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustDir',
            'WindGustSpeed', 'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm',
            'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
            'Temp9am', 'Temp3pm', 'RainToday'
        ]
        input_data = input_data.reindex(columns=expected_columns)

        processed_data = preprocessor.transform(input_data)
        if hasattr(processed_data, "toarray"):
            processed_data = processed_data.toarray()

        prediction = model.predict(processed_data)
        prediction = (prediction > 0.5).astype(int)
        prediction_text = ["Yes Rain Tomorrow" if pred == 1 else "No Rain Tomorrow" for pred in prediction.flatten()]
        return jsonify({'prediction': prediction_text})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

