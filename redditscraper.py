"""
Scrapes specified subreddit for clips.twitch.tv urls
"""

from selenium import webdriver

TWITCH_CLIP_XPATH = "//div[@class='search-result-footer']//a[contains(@href,'clips.twitch')]"

def scrape_twitch_links(url):
    """
    Get twitch clip urls from specified subreddit's search results
    """

    #driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.get(url)
    elements = driver.find_elements_by_xpath(TWITCH_CLIP_XPATH)
    urls = []
    for element in elements:
        value = element.get_attribute("href")
        urls.append(value)

    video_urls = []

    for vid_source in urls:
        driver.get(vid_source)
        element = driver.find_element_by_xpath("//video[@type='video/mp4']")
        video_urls.append(element.get_attribute("src"))

    return video_urls
