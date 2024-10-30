from flask import Flask, request, jsonify
import pandas as pd
from models.machine_learning.model import HealthModel

app = Flask(__name__)
health_model = HealthModel()

@app.route('/health', methods=['POST'])
def health_data():
    data = request.json
    df = pd.DataFrame(data)
    recommendations = generate_recommendations(df)
    return jsonify(recommendations)

def generate_recommendations(df):
    return {
        'average_steps': df['steps'].mean(),
        'average_sleep': df['sleep'].mean(),
    }

if __name__ == '__main__':
    app.run(debug=True)
