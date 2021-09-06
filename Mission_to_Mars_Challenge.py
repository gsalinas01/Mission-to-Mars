#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# ^ this line: searching for elements with combination of tag (div)
# and attribute (list_text). & telling browser wait 1 sec.


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# ^ set up the html parser, assigned slide_elem as the variable
# to look for the <div /> tag and it's descendent. This is our 
#parent element, holds all other elements within it. 


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


#Use the parent element to find the first 'a' tag and save it as
#'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_parag = slide_elem.find_all('div', class_='article_teaser_body')
for x in news_parag:
    words = x.text
    print(words)


# In[8]:


#______________________________________________________


# In[ ]:


#______________________________________________________


# In[ ]:


#______________________________________________________


# In[ ]:


# Image scraping


# # Featured Images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1] #<- to click second button
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# .get('src' pullls the link to the image.)


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


### Scraping tables


# # Mars Facts

# In[15]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
# ^ assigning columns to new DF for more clarity
df.set_index('Description', inplace=True)
# ^ turns 'description' column into index
df


# In[16]:


df.to_html()
# ^ to add df to a web app in HTML


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[25]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[32]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Find the HTML tag that holds all the links to the full-resolution images, or find a common CSS element for the full-resolution image.

#use a for loop to iterate through the tags or CSS element
for x in range(4):
    #create an empty dictionary
    hemispheres = {}
    browser.find_by_tag('h3')[x].click()
    image_selection = browser.find_link_by_text('Sample').first
    img_url = image_selection['href']
    image_title = browser.find_by_css('h2.title').text
    hemispheres["img_url"] = img_url
    hemispheres["Title"] = image_title
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    


# In[33]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[34]:


# 5. Quit the browser
browser.quit()


# In[ ]:




