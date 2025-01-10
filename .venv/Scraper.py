!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET

def scrape_website(url):
    # Make an HTTP request to the website
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}. Status: {response.status_code}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def extract_data(soup):
    # Custom extraction logic (Example: Extracting all links)
    data = []
    for link in soup.find_all('a'):  # Extract 'a' tags
        href = link.get('href')  # Get the 'href' attribute
        text = link.text.strip()  # Get the visible text
        if href:
            data.append({"href": href, "text": text})
    return data


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")


def save_to_xml(data, filename):
    # Create an XML root element
    root = ET.Element("data")

    for item in data:
        link = ET.SubElement(root, "link")
        href = ET.SubElement(link, "href")
        href.text = item["href"]
        text = ET.SubElement(link, "text")
        text.text = item["text"]

    # Generate an XML tree and save to file
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    url = "https://wikipedia.com"  # Replace with the target website

    # Scrape the website
    soup = scrape_website(url)
    if soup:
        # Extract the data
        data = extract_data(soup)

        # Display the extracted data in the Colab notebook
        print("Extracted Links:")
        for item in data:
            print(f"Text: {item['text']}, Href: {item['href']}")

        # Save the data in JSON format
        save_to_json(data, "data.json")

        # Save the data in XML format
        save_to_xml(data, "data.xml")

        # Optionally, download the saved files
        from google.colab import files
        files.download('data.json')
        files.download('data.xml')
