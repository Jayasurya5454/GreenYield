from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Define the path to the models directory
MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')

# Load the trained Naive Bayes model from the pickle file in the models directory
MODEL_FILE_PATH = os.path.join(MODELS_DIR, 'naive_bayes_model.pkl')
with open(MODEL_FILE_PATH, 'rb') as model_file:
    nb_classifier = pickle.load(model_file)

# Define the label mapping
LABEL_MAPPING = {'Apple': 0, 'Banana': 1, 'Blackgram': 2, 'Chickpea': 3, 'Coconut': 4, 'Coffee': 5, 'Cotton': 6,
                 'Grapes': 7, 'Jute': 8, 'Kidneybeans': 9, 'Lentil': 10, 'Maize': 11, 'Mango': 12, 'Mothbeans': 13,
                 'Mungbean': 14, 'Muskmelon': 15, 'Orange': 16, 'Papaya': 17, 'Pigeonpeas': 18, 'Pomegranate': 19,
                 'Rice': 20, 'Watermelon': 21}

# Define a function to preprocess user input and make predictions
def predict_crop(attributes):
    attributes = [float(attr) for attr in attributes]
    prediction = nb_classifier.predict([attributes])
    predicted_crop_index = prediction[0]
    
    # Convert numerical prediction to crop name using the label mapping
    predicted_crop_name = next(plant for plant, index in LABEL_MAPPING.items() if index == predicted_crop_index)
    
    return predicted_crop_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    user_input = request.form.to_dict()
    attributes = [user_input[key] for key in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    
    # Make predictions using the pre-trained model
    predicted_crop = predict_crop(attributes)

    return render_template('result.html', attributes=attributes, predicted_crop=predicted_crop)

if __name__ == '__main__':
    app.run(debug=True)
