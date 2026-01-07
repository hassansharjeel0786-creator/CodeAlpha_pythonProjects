def get_response(message):
    """
    Process the user message and return an appropriate response based on predefined rules.
    """
    # Normalize the input to lowercase for case-insensitive matching
    message = message.lower()
    
    # Check for specific greetings and questions
    if message == "hello":
        return "Hi! Nice to meet you."
    elif message == "hi":
        return "Hi! Nice to meet you."
    elif message == "how are you":
        return "I'm fine, thanks for asking!"
    elif message == "what is your name":
        return "My name is SimpleBot."
    elif message == "bye":
        return "Goodbye! Have a great day."
    else:
        # Handle unrecognized input politely
        return "Sorry, I didn't understand that."

# Main program loop
def main():
    """
    Run the chatbot in a loop, accepting user input until 'bye' is typed.
    """
    print("Welcome to SimpleBot! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "bye":
            print("SimpleBot: Goodbye! Have a great day.")
            break
        
        # Get the response from the function
        response = get_response(user_input)
        
        # Print the chatbot's response
        print("SimpleBot: " + response)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
