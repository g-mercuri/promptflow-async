import os
import asyncio
from promptflow.core import AsyncPrompty
from promptflow.core import AzureOpenAIModelConfiguration
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Asynchronous function to run the AsyncPrompty model with user input
async def run_async_prompty(user_input):
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

    # Load the AsyncPrompty model with the specified configuration
    prompty = AsyncPrompty.load(source="./example.prompty", model=model_config)

    # Send the request to the model and await the response
    result = await prompty(text=user_input)
    return result

# Asynchronous function to handle the interactive chat
async def chat():
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
            response = await run_async_prompty(context)
            print("Chatbot:", response)

            # Add the chatbot's response to the conversation history
            conversation_history.append(f"Chatbot: {response}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    # Run the chat function using asyncio
    asyncio.run(chat())