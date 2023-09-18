import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website to scrape
url = "https://www.theworlds50best.com/previous-list/2002"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the restaurant entries within div elements with class 'item'
    restaurant_entries = soup.find_all('div', class_='item')

    # Initialize empty lists to store the data
    rankings = []
    restaurant_names = []
    locations = []
    year_of_award = '2002'  # The year is constant in this case

    # Extract data from the restaurant entries
    for entry in restaurant_entries:
        # Extract the ranking
        ranking = entry.find('p', class_='position').text.strip()

        # Extract the restaurant name
        name = entry.find('h2').text.strip()

        # Extract the location
        location = entry.find_all('p')[1].text.strip()

        # Append the data to the respective lists
        rankings.append(ranking)
        restaurant_names.append(name)
        locations.append(location)

    # Create a dictionary with the extracted data
    data = {
        'Ranking': rankings,
        'Restaurant Name': restaurant_names,
        'Location': locations,
        'Year of Award': year_of_award
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Save the DataFrame as a CSV file
    df.to_csv('path/to/csv/file.csv', index=False)

    print("Data has been scraped and saved as 'restaurants_2002.csv'.")
else:
    print("Failed to retrieve the web page.")





