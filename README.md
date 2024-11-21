# README

## GitHub Repository Management Project

This project is a Python tool that allows you to create and manage GitHub repositories automatically. It uses an LLM (Large Language Model) to generate the content for the README.md.

### Features

- Creation of a new repository on GitHub
- Initialization of a new local repository with the proper configuration
- Update an existing repository with changes made

### Requirements

- Python 3.x
- Ollama (an LLM model)
- Git and a GitHub account
- Basic knowledge of Git and GitHub

### Usage

1. Clone the local repository.
2. Run `python main.py` to start the tool.

### Super Important Note on Running Ollama Models

Ollama models by default only have 2048 tokens for their context window, even for large models that could easily handle more. This is not a large enough window to handle the Bolt.new/oTToDev prompt! You need to create a version of any model you want to use where you specify a larger context window. Fortunately, it's very easy to do this.

All you need to do is:

1. Create a file called `Modelfile` (no file extension) anywhere on your computer.
2. Add the following two lines:

   ```
   FROM [Ollama model ID such as qwen2.5-coder:7b]
   PARAMETER num_ctx 32768
   ```

3. Run the command:

   ```
   ollama create -f Modelfile [your new model ID, can be anything you want (e.g., qwen2.5-coder-extra-ctx:7b)]
   ```

Now you have a new Ollama model that isn't as heavily limited in context length as Ollama models are by default for some reason. You'll see this new model in the list of Ollama models along with all the others you've pulled!

### Contributors

Contributors are expected to follow these guidelines:

- Use the existing directory and file structure in the project.
- Provide an `.env` file with the necessary environment variables.
- Verify that the `verify_and_generate_readme` function runs correctly before initializing the repository.

### Files and Directories

- `.env`: Configuration file with the required environment variables.
- `gitignore_manager.py`: Manages the files to be ignored in Git.
- `github_manager.py`: Handles the creation and updating of repositories on GitHub.
- `main.py`: Main project file that calls the necessary functions to initialize or update a repository.
- `ollama_manager.py`: Uses the Ollama LLM to generate the content for the README.md.

### Terms of Use

- The tool only works with the current version of the Ollama LLM model. It does not apply automatic updates to the model, so you need to download and install it manually.
- The use of the tool must be authorized through a GitHub account. Changes to the project require confirmation from an administrator.