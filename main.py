# pip install selenium
from selenium import webdriver
import time


def extract_href(input_file, output_file, output_bib_file, chrome_driver):
    with open(input_file, encoding='utf-8') as scholars:
        file_out = open(output_file,'w', encoding='utf-8')  # Also good practice to specify encoding when writing
        file_bib_out = open(output_bib_file, 'w', encoding='utf-8')
        scholars = scholars.readlines()
        browser = webdriver.Chrome(executable_path=chrome_driver)
        url = "https://scholar.google.com"
        browser.get(url)
        links = []
        bibs = []
        failed = []
    for tt in scholars:
        tt = tt.strip().split('\t')
        print(tt[0])
        tt = tt[-1]
        browser.get(url)
        time.sleep(0.5)
        browser.find_element_by_name("q").send_keys(tt)
        try:
            browser.find_element_by_name("btnG").click()
            time.sleep(1)
            browser.find_element_by_class_name("gs_or_cit").click()
            time.sleep(1)
            link = browser.find_element_by_class_name("gs_citi").get_attribute('href')
            print(link)
            if link not in links:
                links.append(link)
                file_out.write(link + '\n')

            browser.get(link)
            time.sleep(1)
            text = browser.find_element_by_tag_name('pre').text + '\n'
            file_bib_out.writelines(text)
            bibs.append(text)
        except Exception as e:
            print('[*****Failed*****]', str(e))
            failed.append(tt)
            continue

    print(links)
    print(bibs)
    file_out.close()
    file_bib_out.close()


# How to use
input_file = 'scholars.txt'
output_file = 'links.txt'
output_bib_file = 'bib.txt'
extract_href(input_file, output_file, output_bib_file, "D:\\Program Files\\Network\\chromedriver.exe")