"""
Scrapes specified subreddit for clips.twitch.tv urls
"""

from selenium import webdriver

def scrape_sub(url):
    """
    Get twitch clip urls from specified subreddit
    """

    #driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.get(url)
