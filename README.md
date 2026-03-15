# 🤖 Local LLM Git Reviewer

A lightweight Python script designed to automate local code reviews using Ollama. The script identifies uncommitted changes via git diff, reads the full file context, and queries an LLM to detect bugs, logic issues, or potential optimizations.
# 🚀 Key Features

    Selective Analysis: Automatically detects modified files using git diff --name-only.

    Full Context Awareness: Sends both the entire file content and the specific diff to the LLM for high-precision feedback.

    Persistent Output: Saves each review into a dedicated text file (diff_filename.txt) for easy consultation.

    Modular Configuration: Settings, server URLs, and exclusion lists are managed via a separate configuration module.

# 🛠️ Requirements

    Python 3.x

    Ollama (installed and running)

    Git

    requests library:
    Bash

    pip install -r requirements/requirements.txt

# 📦 Project Structure

The script expects the following structure:
Plaintext

    .
    ├── configs/
    │   └── conf.py       # Contains LLM_DATA, OLLAMA_SERVER, and SKIP_FILES
    ├── review.py         # Main execution script
    └── requirements/     # requirements lists

⚙️ Configuration

Ensure your configs/conf.py is configured as follows:
Python

conf = {
    "OLLAMA_SERVER": "http://localhost:11434/api/generate",
    "LLM_DATA": {
        "model": "qwen3.5:9b", # you can use what you want
        "prompt": "",          # will be replaces
        "stream": False
    },
    "SKIP_FILES": ["README.md", ".gitignore", "configs/conf.py"]
}

# 🖥️ Usage

Modify your source files.

Run the script from your terminal:
Bash

    python review.py

The script will process each modified file and generate reports like diff_my_project_file.py.txt.

# 💡 Why this approach?

Unlike cloud-based AI reviewers, this local setup offers:

    Total Privacy: Your code never leaves your machine.

    Zero Cost: Leverages your local hardware via Ollama.

    Low Latency: Lightning-fast responses thanks to the local API connection.

Would you like me to add a section on how to integrate this script directly into your Makefile or as a Git pre-push hook?
