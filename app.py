from model import get_response,predict_intent,model,words,data

from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/', methods=['GET'])
def get_bot_response():
    user_input = request.json['query']
    intents_list = predict_intent(user_input, model, words)
    response = get_response(intents_list, data)
    return jsonify({'response': response})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
