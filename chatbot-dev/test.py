import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import os

output_file = "urls.txt"
output_dir = "data-dev/"  # Change this to your desired directory
output_path = os.path.join(output_dir, output_file)

# Function to extract all links from a webpage
def extract_links(url):
    links = set()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            links.add(urljoin(url, href))

    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")

    return links

# Function to recursively crawl a website
def crawl_website(root_url):
    visited = set()
    to_visit = [root_url]

    while to_visit:
        url = to_visit.pop()
        visited.add(url)

        # Extract links from the current URL
        links = extract_links(url)

        print(f"Visiting {url}")

        with open(output_path, 'a') as file:
            file.write(url + '\n')

        # Filter links to those of the same domain
        parsed_root = urlparse(root_url)
        domain = parsed_root.netloc
        filtered_links = [link for link in links if urlparse(link).netloc == domain]


        # Add new links to the to_visit list
        for link in filtered_links:
            if link not in visited and link not in to_visit:
                to_visit.append(link)

# Example usage
crawl_website("https://www.moveworks.com")
