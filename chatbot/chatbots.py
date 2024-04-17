import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thanks for asking!", "Feeling great!", "All good, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."]
}

def chatbot_response(input_text):
    # Convert input to lowercase for case-insensitive matching
    input_text = input_text.lower()
    
    # Check if input is in responses
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        return random.choice(responses["default"])

def main():
    print("Welcome to the Chatbot!")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
