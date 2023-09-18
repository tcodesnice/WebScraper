Restaurant Ranking Scraper
Overview

The "Restaurant Ranking Scraper" is a Python script designed to automate the process of extracting essential information about renowned restaurants from "The World's 50 Best Restaurants" list for a specific year. This script utilizes web scraping techniques to gather data about restaurant rankings, names, locations, and the year of the award. The scraped data is then organized and saved in a CSV file for further analysis.
Features

    Web Scraping: Automatically retrieves data from a specified URL by sending an HTTP GET request and parsing the HTML content using BeautifulSoup.

    Data Extraction: Extracts key information, including restaurant rankings, names, locations, and the year of the award.

    Data Storage: Organizes the scraped data into a structured format and saves it as a CSV file for easy access and analysis.

    Customization: Allows users to customize the target URL to scrape data from different years or websites with similar HTML structures.

    Isolation: Ensures a clean and isolated environment for package management, separating dependencies from the system-wide Python installation.

Getting Started
Prerequisites

Before using the script, make sure you have the following:

    Python 3.x installed on your system.

    The required Python packages (requests, BeautifulSoup4, pandas) installed. You can install them using pip by running:

    pip install requests beautifulsoup4 pandas

Usage

    Clone this repository or download the script (bestrest.py) to your local machine.

    Open a terminal or command prompt and navigate to the directory where the script is located.

    Run the script by executing the following command:

    python bestrest.py

    The script will send an HTTP request to the specified URL, scrape the data, and save it as a CSV file named restaurants_YYYY.csv, where YYYY is the year of the award.

Customization

You can customize the script by modifying the url variable in the script to target different years or websites with similar HTML structures.
