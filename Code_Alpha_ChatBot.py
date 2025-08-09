def chatbot():
    print("Chatbot: Hello! Write something to chat with me or type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Predefined responses
        elif user_input.lower() == "hello":
            print("Chatbot: Hi there! How can I assist you today?")
        elif user_input.lower() == "how are you?":
            print("Chatbot: I am fine thank you!")
        elif user_input.lower() == "bye!":
            print("Chatbot: Goodbye!")
            break
        
        # For unrecognized inputs, ask if user wants to continue
        else:
            print("Chatbot: I am sorry, I don't understand that")
            choice = input("Do you want to continue chatting? (y/n): ")
            if choice.lower() != 'y':
                print("Chatbot: Goodbye!")
                break

# Start the chatbot
chatbot()
