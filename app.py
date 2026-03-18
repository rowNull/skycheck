from flask import Flask, flash, render_template, request
from skycheck.weather import get_weather

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city'].strip()  # gets the city from the form

    try:
        if(city):
            data = get_weather(city)
            return render_template('result.html', data=data)
        else:
            return render_template('index.html', error = "City name cannot be empty. Please try again.")
        
    except ValueError as e:
       return render_template('index.html', error = str(e))

if __name__ == "__main__":
    app.run(debug=True)