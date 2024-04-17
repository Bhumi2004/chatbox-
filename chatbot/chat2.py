from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot("MyChatBot")

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Define a route for receiving messages and returning responses
@app.route("/chat", methods=["POST"])
def chat():
    # Get the incoming message from the request
    incoming_message = request.json["message"]

    # Get the chatbot's response to the incoming message
    response = chatbot.get_response(incoming_message)

    # Return the response as JSON
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
