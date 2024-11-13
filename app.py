from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/data', methods=['GET'])
def get_data():
    # Data JSON yang sesuai dengan struktur yang diminta
    data = {
        "suhumax": 36,
        "suhumin": 21,
        "suhurata": 28.35,
        "nilai_suhu_max_humid_max": [
            {
                "idx": 101,
                "suhun": 36,
                "humid": 36,
                "kecerahan": 25,
                "timestamp": "2010-09-18 07:23:48"
            },
            {
                "idx": 266,
                "suhun": 36,
                "humid": 36,
                "kecerahan": 27,
                "timestamp": "2011-05-02 12:29:34"
            }
        ],
        "month_year_max": [
            {"month_year": "9-2010"},
            {"month_year": "5-2011"}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
