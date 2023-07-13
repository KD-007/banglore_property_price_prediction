from flask import Flask , request , jsonify , render_template
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app)

@app.route('/' , methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/getlocations" , methods=["GET"])
def getlocations():
    response = jsonify({
        "locations": utils.get_location_names()
    })
    return response

@app.route("/predict" , methods=["POST","GET"])
def predict():
    
    total_sqft = float(request.get_json()['total_sqft'])
    location = request.get_json()['location']
    bhk = int(request.get_json()['bhk'])
    bath = int(request.get_json()['bath'])

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location,total_sqft,bhk,bath)
    })

    return response 
if __name__ == '__main__':
    print("app is running")
    utils.load_all_data()
    app.run()