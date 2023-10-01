from chatbot import train_model, send_message  # Import your custom functions
import traceback
# Function to start the chatbot and perform custom training
def start_chatbot():
    train_model("Learn all the context that I will be putting here. The user will ask you questions about the same. This chatbot operates in a read-only mode and does not accept user-provided updates to its knowledge base.")
    print("Custom training completed. You can now start a conversation with the chatbot.")

# Function to handle the interactive conversation
def interactive_conversation():
    while True:
        user_input = input("You: ")  # Read user input from the terminal
        if user_input.lower() == 'exit':
            break  # Exit the loop if the user enters 'exit'
        
        # Print a message to inform the user that updates are not accepted
        
        
        response = send_message(user_input)
        
        # Print the response from the chatbot
        print("Chatbot:", response)

if __name__ == "__main__":
    try:
         # Perform initial training and setup only once
        start_chatbot() 
        
        # Engage in an interactive conversation
        interactive_conversation()
        
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {str(e)}")
