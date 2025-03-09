from flask import Flask, request, render_template, jsonify
from chatbot import get_news_response
from fetch_news import fetch_news
from database import save_news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news', methods=['GET'])
def get_news():
    query = request.args.get('query', '')
    response = get_news_response(query)
    return jsonify({"response": response})

@app.route('/update_news', methods=['GET'])
def update_news():
    news_list = fetch_news()
    save_news(news_list)
    return jsonify({"message": "News updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
