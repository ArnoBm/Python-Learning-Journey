print("🤖 Mini AI: Hello! I am your simple AI. Type 'bye' to exit.\n")

# Dictionary of known responses
responses = {
    "hi": "Hello there!",
    "hello": "Hi! How can I help you?",
    "how are you": "I'm just code, but I feel great!",
    "what is your name": "I'm Mini AI.",
    "bye": "Goodbye! Have a nice day!",
    "help": "You can ask me things like 'how are you', 'what is your name', etc."
}

while True:
    user_input = input("You: ").lower()

    if user_input == 'bye':
        print("Mini AI: Goodbye! 👋")
        break
    elif user_input in responses:
        print("Mini AI:", responses[user_input])
    else:
        print("Mini AI: Sorry, I don't understand that yet.")
