# Dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
def scrape_info():
    browser = init_browser()
    
#SCRAPE: https://mars.nasa.gov/news/

    # Retrieve webpage with splinter
    urlMarsNASAnews = 'https://mars.nasa.gov/news/'
    browser.visit(urlMarsNASAnews)

    # Create a Beautiful Soup object
    soupMarsNASAnews = bs(browser.html, 'html.parser')
    
    resultsMarsNASAnews = soupMarsNASAnews.find_all('li',class_='slide')
    
    #ASSIGN latest title and paragraph to variables
    newNASAtitle = resultsMarsNASAnews[0].find('div', class_='content_title').text
    newNASAparagraph = resultsMarsNASAnews[0].find('div', class_='article_teaser_body').text

    
#SCRAPE img from https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

    # Retrieve webpage with splinter
    urlJPL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(urlJPL)
    
    # Create a Beautiful Soup object
    soupJPL = bs(browser.html, 'html.parser')
    
    # review the featured image section
    featuredImage = soupJPL.find('section', class_='primary_media_feature')
    
    # ASSIGN featured image url a variable

    featuredImageStyle = featuredImage.article['style']

    urlstring = featuredImageStyle.find("url(")

    urlstart = featuredImageStyle.find("'", urlstring)

    urlend = featuredImageStyle.find("'", urlstart+1)

    urlJPLmainPage = 'https://www.jpl.nasa.gov'

    # cleaned up url string 
    featuredImageUrl = urlJPLmainPage + featuredImageStyle[urlstart+1:urlend]
    
#SCRAPE mars weather tweet

    # Retrieve webpage with splinter
    urlMarsWeather ='https://twitter.com/marswxreport?lang=en'
    browser.visit(urlMarsWeather)
    
    # Create a Beautiful Soup object
    soupMarsWeather = bs(browser.html, 'html.parser')
    
    # review the featured image section
    marsTweets = soupMarsWeather.find_all('li', class_='js-stream-item')
    
    # ASSIGN latest mars weather tweet to a variable
    latestMarsTweet = marsTweets[0].find('p', class_='js-tweet-text').text
    
#SCRAPE Mars facts

    urlMarsFacts = 'https://space-facts.com/mars/'
    
    # READ the html table
    marsFacts = pd.read_html(urlMarsFacts)
    
    # convert table to dataframe
    marsFactsDF = marsFacts[0]
    marsFactsDF.columns = ['Attribute','Value']

    # ASSIGN variable to converted panda dataframe to a HTML table string
    htmlTableMarsFacts = marsFactsDF.to_html()
    
#SCRAPE Mars Hemisphere data

    # Create an empty list of for dictionaries
    urlHemImagesList = []
    
    urlMarsHemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(urlMarsHemisphere)
    
    # Give time for page to load before click
    time.sleep(3)

    # Click on link to high resolution page
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(2)

    # Create a Beautiful Soup object
    soupCerberusHem = bs(browser.html, 'html.parser')

    # review the page list for download links
    urlCerberusHem = soupCerberusHem.find_all('a', target='_blank')

    # pull the link of the original size image
    urlPhotoCerberusHem = urlCerberusHem[1]['href']

    dictCerberusHem = {'title': 'Cerberus Hemisphere','img_url': urlPhotoCerberusHem}

    # APPEND to Image List
    urlHemImagesList.append(dictCerberusHem)
    
    
    
    # Click back to original page
    browser.visit(urlMarsHemisphere)
    time.sleep(3)

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(3)

    # Create a Beautiful Soup object
    soupSchiaparelliHem = bs(browser.html, 'html.parser')

    # review the page list for download links
    urlSchiaparelliHem = soupSchiaparelliHem.find_all('a', target='_blank')

    # pull the link of the original size image
    urlPhotoSchiaparelliHem = urlSchiaparelliHem[1]['href']

    dictSchiaparelliHem = {'title': 'Schiaparelli Hemisphere','img_url': urlPhotoSchiaparelliHem}

    # APPEND to Image List
    urlHemImagesList.append(dictSchiaparelliHem)
    
    
    
    # Click back to original page
    browser.visit(urlMarsHemisphere)
    time.sleep(3)

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(3)

    # Create a Beautiful Soup object
    soupSyrtisMajorHem = bs(browser.html, 'html.parser')

    # review the page list for download links
    urlSyrtisMajorHem = soupSyrtisMajorHem.find_all('a', target='_blank')

    # pull the link of the original size image
    urlPhotoSyrtisMajorHem = urlSyrtisMajorHem[1]['href']

    dictSyrtisMajorHem = {'title': 'Syrtis Major Hemisphere','img_url': urlPhotoSyrtisMajorHem}

    # APPEND to Image List
    urlHemImagesList.append(dictSyrtisMajorHem)
    
    
    
    # Click back to original page
    browser.visit(urlMarsHemisphere)
    time.sleep(3)

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(3)

    # Create a Beautiful Soup object
    soupVallesMarinerisHem = bs(browser.html, 'html.parser')

    # review the page list for download links
    urlVallesMarinerisHem = soupVallesMarinerisHem.find_all('a', target='_blank')

    # pull the link of the original size image
    urlPhotoVallesMarinerisHem = urlVallesMarinerisHem[1]['href']

    dictVallesMarinerisHem = {'title': 'Valles Marineris Hemisphere','img_url': urlPhotoVallesMarinerisHem}

    # APPEND to Image List
    urlHemImagesList.append(dictVallesMarinerisHem)
    
    
    
#STORE data in a dictionary

    mars_data = {
        'newNASAtitle': newNASAtitle,
        'newNASAparagraph': newNASAparagraph,
        'featuredImageUrl': featuredImageUrl,
        'latestMarsTweet': latestMarsTweet,
        'htmlTableMarsFacts': htmlTableMarsFacts,
        'urlHemImagesList': urlHemImagesList
    }
    
#CLOSE browser after scraping
    browser.quit()

    #return results
    return mars_data

    

    
    