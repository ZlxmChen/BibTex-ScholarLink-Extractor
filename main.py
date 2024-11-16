from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# If using Chrome, check https://developer.chrome.google.cn/docs/chromedriver/downloads for correct webdriver version.
# Function to open the file based on append_mode
# If append_mode is True and the file exists, open in append ('a') mode.
# Otherwise, open in write ('w') mode.
def open_file(file_path, append_mode):
    if append_mode and os.path.exists(file_path):
        return open(file_path, 'a', encoding='utf-8')  # Append mode
    else:
        return open(file_path, 'w', encoding='utf-8')  # Write mode


def extract_href(input_file, output_file, output_bib_file, append_mode):
    # Open the input file for reading
    with open(input_file, encoding='utf-8') as scholars:
        # Open the output files in append or write mode based on append_mode
        file_out = open_file(output_file, append_mode)
        file_bib_out = open_file(output_bib_file, append_mode)
        scholars = scholars.readlines()

        # Initialize the browser (using Chrome in this example)
        browser = webdriver.Chrome()
        # browser = webdriver.Safari()    # According to https://github.com/SeleniumHQ/selenium/issues/14698 safari may have type Error problem, if so, try chrome instead.

        # Navigate to Google Scholar
        url = "https://scholar.google.com"
        browser.get(url)

        # Lists to store links, bibliographic data, and failed cases
        links = []
        bibs = []
        failed = []

    for tt in scholars:
        # Skip empty lines
        if not tt.strip():
            file_out.write('\n')
            file_bib_out.write('\n')
            continue

        # Process each line of input
        tt = tt.strip().split('\t')
        print(tt[0])
        tt = tt[-1]
        browser.get(url)
        time.sleep(0.5)

        try:
            # Wait for the search box to be clickable and interact with it
            search_box = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(tt)
            browser.find_element(By.NAME, "btnG").click()
            time.sleep(1)

            # Wait for and click the citation link
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "gs_or_cit"))
            ).click()
            time.sleep(1)

            # Extract the citation link
            link = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gs_citi"))
            ).get_attribute('href')
            print(link)
            if link not in links:
                links.append(link)
                file_out.write(link + '\n')

            # Fetch bibliographic data from the citation link
            browser.get(link)
            time.sleep(1)
            text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'pre'))
            ).text + '\n'
            file_bib_out.writelines(text)
            bibs.append(text)

        except Exception as e:
            # Log any failed cases
            print('[*****Failed*****]', str(e))
            failed.append(tt)
            continue

    # Print the collected links and bibliographic data
    print(links)
    print(bibs)
    file_out.close()
    file_bib_out.close()


# How to use
input_file = 'scholars.txt'  # Input file containing scholar data
output_file = 'links.txt'  # Output file for storing links
output_bib_file = 'bib.txt'  # Output file for storing bibliographic data
append_mode = False  # Set to True for appending to files, False for overwriting files
extract_href(input_file, output_file, output_bib_file, append_mode)