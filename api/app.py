from model import get_response,predict_intent,model,words,data

from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])
def get_bot_response():
    user_input = request.json['query']
    intents_list = predict_intent(user_input, model, words)
    print(len(intents_list))
    response = get_response(intents_list, data)
    return jsonify({'response': response})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=15527)
