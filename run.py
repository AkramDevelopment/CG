#from flask_cors import CORS
from backend import app

if __name__ == '__main__':
    #Commented out due to issues with installing flask_cors on windows machine, uncomment out during production
    #CORS(app, supports_credentials=True)
    app.run(debug=True, host='0.0.0.0', port=8080)
