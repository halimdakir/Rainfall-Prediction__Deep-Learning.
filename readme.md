***Dataset***

*link to dataset:*

`https://www.kaggle.com/datasets/arunavakrchakraborty/australia-weather-data?select=Weather+Test+Data.csv`


***Building the Docker Image***

*Navigate to the directory containing Dockerfile and run the following command to build the Docker image:*

`docker build -t weather-prediction-app .`

*Run the Docker container using the following command:*

`docker run -d -p 5000:5000 --name weather-prediction-app weather-prediction-app
`


***Test the endpoint***

*These PowerShell commands send a POST request to the Flask endpoint which is running on http://127.0.0.1:5000, with the JSON payload containing weather data that the model is expected to predict as rain tomorrow.*




`Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -ContentType 'application/json' -Body '{"data": [{"Location": "Albury", "MinTemp": 22.5, "MaxTemp": 30.0, "Rainfall": 5.0, "Evaporation": 2.0, "Sunshine": 3.0, "WindGustDir": "N", "WindGustSpeed": 55, "WindDir9am": "N", "WindDir3pm": "N", "WindSpeed9am": 30, "WindSpeed3pm": 35, "Humidity9am": 85, "Humidity3pm": 90, "Pressure9am": 1005.0, "Pressure3pm": 1003.0, "Cloud9am": 8, "Cloud3pm": 8, "Temp9am": 24.0, "Temp3pm": 27.0, "RainToday": "Yes"}]}'
`

**Expected Output**

`{
  "prediction": ["Yes Rain Tomorrow"]
}`



`Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -ContentType 'application/json' -Body '{"data": [{"Location": "Albury", "MinTemp": 12.9, "MaxTemp": 25.7, "Rainfall": 0.0, "Evaporation": 5.461319645520799, "Sunshine": 7.615090327400943, "WindGustDir": "WSW", "WindGustSpeed": 46, "WindDir9am": "W", "WindDir3pm": "WSW", "WindSpeed9am": 19, "WindSpeed3pm": 26, "Humidity9am": 38, "Humidity3pm": 30, "Pressure9am": 1007.6, "Pressure3pm": 1008.7, "Cloud9am": 4, "Cloud3pm": 2, "Temp9am": 21.0, "Temp3pm": 23.2, "RainToday": "No"}]}'
`

**Expected Output**

`{
  "prediction": ["No Rain Tomorrow"]
}`