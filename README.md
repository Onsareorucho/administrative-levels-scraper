# Country Administrative Level Crawler

Crawl the GADM website to fetch administrative levels for all the countries or just the specific country you need.

All you need is the country's ISO name. For example, Kenya is 'KEN'. It works with the three letter code. You can find the ISO names for all the countries here https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes 

To run this project:
   1. clone the directory
   2. run python gadm_scraper.py --country KEN (You can replace KEN with the ISO code of your desired country)
   3. Sit back and wait as the administrative levels are downloaded to the folder adminLevels and in the country name's folde, for example: adminLevels\Kenya\
