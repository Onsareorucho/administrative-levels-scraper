import requests
from bs4 import BeautifulSoup
import os, json
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--country","-C",help="ISO Code of Desired country")
args = parser.parse_args()

URL = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/"

page = requests.get(URL)


# Set up the folder to save JSON files
folder_path = "adminLevels"
os.makedirs(folder_path, exist_ok=True)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("table")

all_json_links = []
for row in results.find_all("tr"):
    links = row.find_all("a")
    for link in links:
        href = link.get("href")
        if href.endswith('.json'):
            all_json_links.append(href)
countries = {}

for country_json_link in all_json_links:
    country_code = country_json_link.split("_")[1]
    if args.country:
     if country_code != args.country:
         continue

    level = int(country_json_link.split("_")[2].split('.')[0])
    if country_code not in countries:
        countries[country_code] = {}
    if level not in countries[country_code]:
        countries[country_code][level] = country_json_link

for country,levels in countries.items():
    if args.country:
     if country != args.country:
         continue
     link =URL + countries[country][max(levels)]
     response = requests.get(link)
     json_content = response.json()
     country_name = json_content['features'][0]['properties'].get('COUNTRY').replace(" ","_")
     folderpath = os.path.join(folder_path,country_name)
     os.makedirs(folderpath, exist_ok=True)
     file_name = os.path.join(folderpath, f"{country}_{max(levels)}.json")
     with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded and saved: {country_name}")

     print(link)
