import requests
from bs4 import BeautifulSoup


print ("This is a test!")
# Define the URL to scrape
url = "https://en.wikipedia.org/wiki/W3Schools"  # Replace with the target URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract all links from the page
    links = soup.find_all('a')
    print("Links found on the page:")
    for link in links:
        href = link.get('href')
        if href:
            print(href)

    # Example: Extract all headings
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print("\nHeadings found on the page:")
    for heading in headings:
        print(heading.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
