from flask import Flask, request, jsonify
import util as ut

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    try:
        locations = ut.get_location_names()
          
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error in get_location_name: {e}")
        return jsonify({
            'error': str(e)
        })

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        
      
        response = jsonify({
            'estimated_price' : ut.get_estimated_price(total_sqft,location, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == "__main__":
    ut.load_saved_artifacts()
    print("Starting python flask server for Home price prediction")
    app.run(debug=True)
