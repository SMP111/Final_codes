import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path

def get_text(url):
    # GET URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()
        clean_text = re.sub(r'\n\s*\n', '\n', text_content).strip()

        output_file = Path('/../data-dev/extracted_files') / (url + '.txt')

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(clean_text)

        print(f"Text content from '{url}' has been saved to '{output_file}'")
    else:
        print(f"Failed to fetch content from '{url}' (status code {response.status_code})")
