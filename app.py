from flask import Flask, request, send_from_directory, render_template
import os
import pickle

MEMBER_FOLDER = os.path.join('static', 'assets')

# Create flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():

    # Get data and convert into numeric value
    age = int(request.form.get("inputAge"))
    time = float(request.form.get('inputTime'))
    number_of_warts = int(request.form.get('numberOfWarts'))
    surface_area = int(request.form.get('surfaceArea'))
    wart_type = int(request.form.get('gridRadios'))
    gender = int(request.form.get('gender'))

    # Make prediction using model loaded from disk as per the data.
    features = [age, time, number_of_warts, surface_area, wart_type, gender]

    # Predict the output
    prediction = model.predict([features])

    # Take the first value of prediction
    output = prediction[0]
    if(output == 1):
        output = 'The level of cancer are Benign'
    else:
        output = 'The level of cancer are Malignant'
    return render_template('index.html', prediction_text='{}'.format(output))
    

@app.route('/naive_bayes')
def show_naive_bayes():
    return render_template('naive_bayes.html')

@app.route('/about')
def server_error():
    return render_template('about.html')

# Load image in about us page
@app.route('/<filename>')
def display_image(filename):
    return send_from_directory(MEMBER_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)