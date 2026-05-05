import joblib
import numpy as np

def load_artifacts():
    model = joblib.load("rf_disease_model.pkl")
    encoder = joblib.load("disease_label_encoder.pkl")
    symptom_cols = joblib.load("symptom_columns.pkl")
    return model, encoder, symptom_cols


def predict_disease(selected_symptoms, symptom_cols, model, encoder):

    input_data = np.zeros(len(symptom_cols))


    for symptom in selected_symptoms:
        if symptom in symptom_cols:
            index = symptom_cols.index(symptom)
            input_data[index] = 1


    input_data = input_data.reshape(1, -1)


    prediction_encoded = model.predict(input_data)[0]


    prediction = encoder.inverse_transform([prediction_encoded])[0]

    return prediction

