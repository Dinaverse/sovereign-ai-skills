import json
import subprocess
import requests
import sys

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_mistral(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        return response.json().get("response", "")
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

def summarize_log(file_path):
    with open(file_path, 'r') as f:
        log_data = f.read()[-5000:] # Get last 5KB
    prompt = f"Summarize the following log file content, highlighting any errors or critical alerts: {log_data}"
    return query_mistral(prompt)

def document_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    prompt = f"Provide a brief documentation header and docstrings for the following code:\n{code}"
    return query_mistral(prompt)

def audit_config(file_path):
    with open(file_path, 'r') as f:
        config = f.read()
    prompt = f"Perform a security audit on the following configuration file and list potential risks: {config}"
    return query_mistral(prompt)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 ollama_suite.py <action: log|doc|audit> <file_path>")
        sys.exit(1)
    
    action, path = sys.argv[1], sys.argv[2]
    if action == "log":
        print(summarize_log(path))
    elif action == "doc":
        print(document_code(path))
    elif action == "audit":
        print(audit_config(path))
