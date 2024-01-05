
# Chatbot Project

## Overview
This project includes a chatbot built using TensorFlow and Flask. The chatbot is trained on a predefined set of intents and can respond to user queries accordingly.

## Structure
- `model.py`: Contains the chatbot model and utility functions.
- `app.py`: Flask application for serving the chatbot model.
- `chatbot_model.h5`: Pre-trained chatbot model.
- `intents.json`: Definitions of intents and responses.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the Flask server: `python3 api/app.py`

## Usage
Send POST requests to the Flask server with a JSON payload containing the user query. The chatbot will respond with the appropriate message.

## Note
Ensure all the necessary files are in place and the model is correctly loaded before starting the server.

