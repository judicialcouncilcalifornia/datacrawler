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
% make run

# Visit http://localhost:9001

# To stop the container
% make stop
# To start the container
% make start
# To remove the container
% make rm
# To see the logs
% make logs
```

## Running the spider
To run the spider, login to the container:
```shell script
% make shell

# Run the spider
% portiacrawl PROJECT_NAME SPIDER_NAME

# Run the spider and save to file
% portiacrawl PROJECT_NAME SPIDER_NAME -o PROJECT_PATH/results/all.json

#To detach from the login:
Ctrl+P, then Ctrl+Q
```

## The Process
1. Create a project, eg. trialcourt-slo
2. In the project, create a spider, eg. www.slo.courts.ca.gov
3. In the spider, create Starting Pages
4. Create sample pages to train the spider on what to extract
5. Label the sample pages with the appropriate type.
6. When adding properties, reuse the existing field type.

![Portia Screenshot](https://raw.githubusercontent.com/JudicialCouncilOfCalifornia/datacrawler/master/images/datacrawler-portia.png)

### Sample Result
https://github.com/JudicialCouncilOfCalifornia/datacrawler/blob/master/projects/trial-court-slo/results/all.json

## Configuring the spider

Use regex to limit the URL that will be crawled. For example, ```.*\/sh\/.*``` will only index urls with `/sh/`.