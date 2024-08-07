import csv
import time
from pages.Imports import *
from pages.functions import *

# List of states and territories
states_and_territories = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", 
    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Dakota", "Texas", "Tennessee", 
    "Utah", "Vermont", "Washington", "West Virginia", "Wisconsin", "Wyoming", 
    "Territories", "Virginia", "South Carolina", "Delaware", 
    "District of Columbia", "New Hampshire"
]

# Path to the CSV file
csv_file_path = 'E:\\My Data\\my_Projects\\Kick-Starter-Full-projct\\Scraper script\\Sent_messages.csv'

def main_code_1():
    driver = None
    try:
        driver = get_undetected_chrome_browser('christoph')
        driver.maximize_window()
        
        # Iterate through each state in the list
        for state in states_and_territories:
            # Open the CSV file for each state
            with open(csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                
                # Check if the state is in the header
                if state in reader.fieldnames:
                    # Process each row
                    print(f"Processing state: {state}")
                    for row in reader:
                        # Get the URL from the column corresponding to the state
                        url = row.get(state, "")
                        
                        # Check if the URL is not empty
                        if url:
                            print(f"URL: {url}")
                            time.sleep(1)
                            driver.get(f"{url}search/web")
                            time.sleep(1)
                            current_url = driver.current_url
                            print(f"Current URL: {current_url}")
                            time.sleep(1)
                            try:
                                result = driver.find_elements(By.XPATH, '//*[@class="search bd-can-hover"]//*[@class="result-info"]//a')
                                print(f"Length of URL: {len(result)}")
                                # for res in result:
                                #     result_url = res.get_attribute('href')
                                #     # print(result_url)
                                #     print(f"Length of URL: {len(result_url)}")
                            except Exception as e:
                                print(e)
                        else:
                            pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

print("Scraping complete. Data saved to CSV.")
