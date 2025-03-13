import requests
from bs4 import BeautifulSoup
import subprocess

def scrape_url(url):
    """
    Scrapes the given URL and returns the text content from paragraph tags.
    If no <p> tags are found, returns an empty string.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text_content = "\n".join([para.get_text() for para in paragraphs]).strip()
        return text_content
    except Exception as e:
        return f"Error occurred: {str(e)}"

def get_llm_response(model, prompt):
    """
    Calls the Ollama CLI to run the specified model (e.g., "llama:3.2")
    with the provided prompt and returns the output.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            encoding='utf-8',  # Ensure we use UTF-8 encoding
            check=True,
            timeout=60  # Timeout after 60 seconds
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "LLM error: The request timed out."
    except Exception as e:
        return f"LLM error: {str(e)}"

def summarize_text(text):
    """
    Summarizes the given text using the 'llama:3.2' model via Ollama.
    The text is limited to the first 1000 characters to keep the prompt size manageable.
    If no text is provided, returns an appropriate message.
    """
    if not text:
        return "There is no text for me to summarize. Please provide the text you would like me to summarize, and I'll be happy to help!"
    
    # Limit the text input size to the first 1000 characters
    max_length = 1000
    limited_text = text[:max_length]
    prompt = f"Summarize the following text:\n{limited_text}"
    
    print("Sending prompt to LLM using llama3.2...")  # Debug print
    summary = get_llm_response("llama3.2:latest", prompt)
    print("Received response from LLM.")  # Debug print
    return summary