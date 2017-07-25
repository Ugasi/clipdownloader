"""
Scrapes specified subreddit for clips.twitch.tv urls
"""

from selenium import webdriver
from clip import Clip

TWITCH_CLIP_XPATH = "//div[@class='search-result-footer']//a[contains(@href,'clips.twitch')]"
VID_SOURCE_XPATH = "//video[@type='video/mp4']"
STREAMER_XPATH = "//div[@class='view-bc-meta__name ellipsis']//a"
CLIP_NAME_XPATH = "//div[@class='view-clip__title']"
SRC_ATTR = "src"
HREF_ATTR = "href"

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
        value = element.get_attribute(HREF_ATTR)
        urls.append(value)

    clips = []

    for vid_source in urls:
        driver.get(vid_source)
        source = driver.find_element_by_xpath(VID_SOURCE_XPATH).get_attribute(SRC_ATTR)
        streamer = driver.find_element_by_xpath(STREAMER_XPATH).text
        clip_name = driver.find_element_by_xpath(CLIP_NAME_XPATH).text
        clip = Clip(source, streamer, clip_name)
        clips.append(clip)

    return clips
