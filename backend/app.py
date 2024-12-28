from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

# initializes a Flask application instance in a Python script
# 1. Flask Class Initialization:
# - Creates instance of Flask class
# 2. __name__ argument:
# - __name__ special variable that holds the name of the module being executed
# - Passing __name__ allows Flask to locate resources (eg. templates and static files) relative to the application's location
# 3. "app" object:
# - app object is the main entry point for the Flask application.
# - used to define routes (URLs) and attach functions (views) to handle requests

app = Flask(__name__)

CORS(app) # enable CORS for all routes

# load flask file
MechE_df = pd.read_csv('data\\MechE_Test.csv')
AeroE_df = pd.read_csv('data\\AeroE_Test.csv')

# "route decorator"
# defines a URL endpoint for your Flask application
@app.route('/api/courses/Mechanical-Engineering', methods=['GET'])

# view function that will be called when "/api/courses" route is accessed
# - name is arbitrary (used for clarity)
def get_meche_courses():
    # convert pandas dataframe to JSON-like structure
    courses = MechE_df.to_dict(orient='records')              # convert df into a list of dictionaries
    return jsonify(courses)                             # convert python data into JSON response

@app.route('/api/courses/Aerospace-Engineering', methods=['GET'])
def get_aeroe_courses():
    # convert pandas dataframe to JSON-like structure
    courses = AeroE_df.to_dict(orient='records')              # convert df into a list of dictionaries
    return jsonify(courses)  


# checks if the script is being run directly (as opposed to being imported as a module)
# if TRUE, the script is executed as the main program
if __name__ == '__main__':
    app.run(debug=True)         # starts the Flask development server (listens to incoming requests and serves responses)
                                # debug=True -> automatically restarts server on change to code and provides error messages