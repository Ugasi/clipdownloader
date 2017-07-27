"""
Scrapes specified subreddit for clips.twitch.tv urls
"""
import re
from clip import Clip

TWITCH_CLIP_XPATH = "//div[@class='search-result-footer']//a[contains(@href,'clips.twitch')]"
VID_SOURCE_XPATH = "//video[@type='video/mp4']"
STREAMER_XPATH = "//div[@class='view-bc-meta__name ellipsis']//a"
CLIP_NAME_XPATH = "//div[@class='view-clip__title']"
SRC_ATTR = "src"
HREF_ATTR = "href"

def scrape_twitch_links(url, driver):
    """
    Get twitch clip urls from specified subreddit's search results
    """
    #driver = webdriver.PhantomJS()
    driver.get(url)
    elements = driver.find_elements_by_xpath(TWITCH_CLIP_XPATH)
    urls = []

    for element in elements:
        value = element.get_attribute(HREF_ATTR)
        urls.append(value)
    print("Amount of videos expected: "+str(len(urls)))
    return urls

def get_twitch_info(urls, driver):
    """
    Parses video source, streamer name and clip name from given list of twitch url
    """
    clips = []

    for index, vid_source in enumerate(urls):
        driver.get(vid_source)
        source = driver.find_element_by_xpath(VID_SOURCE_XPATH).get_attribute(SRC_ATTR)
        if "index" in source:
            print("Video from source")
            continue
        streamer = driver.find_element_by_xpath(STREAMER_XPATH).text
        clip_name = str(index)
        clip = Clip(source, streamer, clip_name)
        clips.append(clip)

    return clips
