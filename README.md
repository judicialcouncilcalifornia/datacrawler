# Judicial Council Data Scraper
A set of tools and processes to scrape data from web properties that need to be migrated to the web platform.

Uses the following tools:
* Scrapy
* Portia

## Running the project
```shell script
# Clone this project
# Go to this projects root directory

# Run the container
# Replace "~/Sites/datacrawler" with the full path to the project directory
% docker run -d -v ~/Sites/datacrawler:/app/data/projects:rw -p 9001:9001 --name datacrawler scrapinghub/portia

# Visit http://localhost:9001

# To stop the container
% docker stop datacrawler
# To start the container
% docker start datacrawler
# To remove the container
% docker rm datacrawler
```

## Running the spider
To run the spider, login to the container:
```shell script
% docker exec -it datacrawler /bin/bash
```
In the container, go to the project folder:
```shell script
% cd /app/data/projects

# Run the spider
% portiacrawl PROJECT_PATH SPIDER_NAME

# Run the spider and save to file
% portiacrawl PROJECT_PATH SPIDER_NAME -o results.json
```
To detach from the login:
```shell script
Ctrl+P, then Ctrl+Q
```

## Configuring the spider

Use regex to limit the URL that will be crawled. For example, ```.*\/sh\/.*``` will only index urls with `/sh/`.