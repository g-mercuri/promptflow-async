import os
from promptflow.core import Prompty
from promptflow.core import AzureOpenAIModelConfiguration
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Function to run the Prompty model with user input
def run_prompty(user_input):
    # Configuration for the Azure OpenAI model
    model_config = {
        "api": "chat",
        "configuration": AzureOpenAIModelConfiguration(
            azure_deployment="gpt-35-turbo",  # Specify the Azure deployment model
            api_key=os.environ["AZURE_OPENAI_API_KEY"],  # API key from environment variables
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],  # API version from environment variables
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]  # Azure endpoint from environment variables
        ),
        "parameters": {
            "max_tokens": 512  # Maximum number of tokens for the response
        }
    }

    # Load the Prompty model with the specified configuration
    prompty = Prompty.load(source="./example.prompty", model=model_config)

    # Send the request to the model and get the response
    result = prompty(text=user_input)
    return result

# Function to handle the interactive chat
def chat():
    print("Welcome to the interactive chat! Type 'exit' to leave.")
    
    # List to store the conversation history
    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the chat...")
            break
        
        # Add the user's input to the conversation history
        conversation_history.append(f"You: {user_input}")

        try:
            # Combine the conversation history into a single string
            context = "\n".join(conversation_history)
            response = run_prompty(context)
            print("Chatbot:", response)

            # Add the chatbot's response to the conversation history
            conversation_history.append(f"{response}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    chat()
