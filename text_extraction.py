import requests
from bs4 import BeautifulSoup
import re
import os

def get_text(url):
    # GET URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()
        clean_text = re.sub(r'\n\s*\n', '\n', text_content).strip()

        url_edited = url.replace("/", "-")
        output_file = os.path.join('data-dev/scraped_content/', url_edited + ".txt")

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(clean_text)

        print(f"Text content from '{url}' has been saved to '{output_file}'")
    else:
        print(f"Failed to fetch content from '{url}' (status code {response.status_code})")

get_text("https://www.moveworks.com")
