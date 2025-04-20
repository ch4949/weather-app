from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return jsonify({'error': 'API key missing'}), 500
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Weather data fetch failed'}), response.status_code
    data = response.json()
    return jsonify({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
        'humidity': data['main']['humidity']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)