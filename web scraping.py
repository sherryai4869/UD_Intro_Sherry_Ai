# ###***I'm sorry I didn't write a program that would run. I tried all weekend, asked a lot of my programmer friends, and even wrote the program in my dreams, but it ended in failure.
# ###***I tried a dozen different websites and many different approaches
# ###***but they all failed.
# ###***I think I need to take longer to teach myself web scraping.
# ###***If you see this, teacher
# ###***please choose another student's assignment to demonstrate.

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
url="https://archive.org/details/audio_bookspoetry"
books_list = []
author_list=[]
link_list=[]
pdf_list=[]
def extract_page_data(driver):
    #Grab all books
    books=driver.find_elements("class name", "hoverable")
    #print(len(books))

    #Create loop to itterate on the list
    for b in range(len(books)):
        try:
            #Extracting title
            title = books[b].find_element("class name","truncated").text
            #print(title)

            #Extraction of authors
            authors=books[b].find_element("class name","created-by").text
            #print(authors)

            #Extraction of link
            link = books[b].find_element("link text",books).get_attribute('href')
            #print(link)


            #Add item to the respective lists
            books_list.append(title)
            author_list.append(authors)
            link_list.append(link)
            sleep(2)

        except:
            pass


driver = webdriver.Chrome()
driver.get(url)


#Step 1: identify search box
search_query = driver.find_element("name","query")

#Step 2: search a topic
search_query.send_keys('Future')
search_query.send_keys(Keys.RETURN)
#Delay
sleep(1)


#Execute the function
extract_page_data(driver)

#Close the webpage
driver.quit()

print(books_list)
#%%
