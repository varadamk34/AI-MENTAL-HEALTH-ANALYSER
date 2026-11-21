from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    text = request.form['text']

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        result = "Mental State: Happy/Normal 😊"

    elif analysis.sentiment.polarity < 0:
        result = "Mental State: Stress or Depression 😔"

    else:
        result = "Mental State: Neutral 😐"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)