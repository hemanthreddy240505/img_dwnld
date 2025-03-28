import requests
from bs4 import BeautifulSoup
import os

url = input("Enter the URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all('img')

for i, image in enumerate(images):
    image_url = image.get('src')
    if image_url:
        filename = f"image_{i+1}.jpg"
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded: {filename}")
        else:
            print(f"Failed to download image: {filename}")
