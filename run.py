from flask_cors import CORS
from backend import app

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True, host='0.0.0.0', port=8080)
