"""
Scrapes specified subreddit for clips.twitch.tv urls
"""

from selenium import webdriver

TWITCH_CLIP_XPATH = "//div[@class='top-matter']//a[contains(@data-href-url,'clips.twitch')]"

def scrape_sub(url):
    """
    Get twitch clip urls from specified subreddit
    """

    #driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.get(url)
    elements = driver.find_elements_by_xpath(TWITCH_CLIP_XPATH)
    for element in elements:
        print(element.get_attribute("data-href-url"))

scrape_sub("https://www.reddit.com/r/hearthstone/")
