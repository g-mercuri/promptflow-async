# Asynchronous Interactive Chatbot

This project is an asynchronous interactive chatbot that uses the Azure OpenAI GPT-3.5 Turbo model to generate responses based on user input. The project was created using the documentation available on [PromptFlow Core](https://microsoft.github.io/promptflow/reference/python-library-reference/promptflow-core/promptflow.core.html).

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Configuration

Make sure to set the following environment variables in the [`.env`] file with your Azure OpenAI credentials:

```env
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
```

## Usage

Run the program to start the interactive chat:

```bash
python asyncflow.py
```

## Modifying the Prompt

You can modify the prompt used by the model in the [`async.prompty`] file. Here is an example of the file content:

```yaml
---
...
---
system:
You're a helpful assistant, reply to user based on the input text: "{{text}}"
```

## Documentation

This project was created using the documentation available on [PromptFlow Core](https://microsoft.github.io/promptflow/reference/python-library-reference/promptflow-core/promptflow.core.html).

## Available additional modules

- `flow.py`: Available without asynchronous functionality.
- `flowhistory.py`: Includes an additional chat history function.

## Contributions

If you wish to contribute to the project, please open an issue or submit a pull request.

## License

This project is released under the MIT license.