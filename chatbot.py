# Simple Chatbot using Python

def get_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "what is your name": "I don't have a name, but you can call me a Chatbot.",
        "bye": "Bye! Have a great day!",
    }
    
    user_input = user_input.lower()
    
    return responses.get(user_input, "Sorry, I didn't understand that.")

def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Bye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
