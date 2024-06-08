from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import tools.FFMpeg
import os

class Amedia:
    def __init__(self, link, over=False):
        tools.info("Starting parser")
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Firefox(options=options)
        tools.info("Parser started")
        self.browser.get(link)

        self.over = over

    def download_one(self, dest=None):
        current = self.browser.find_element(By.CSS_SELECTOR, '.sel-active.nav_video_links')
        ep = current.get_attribute('data-vid')
        tools.info("Parsing {} episode".format(ep))
        link = current.get_attribute('data-vlnk')
        filename = "{:02d}.mp4".format(int(ep))

        tools.info("Downloading {} episode".format(ep))
        self.__download(link, dest, filename)
        tools.info("Downloaded {} episode".format(ep))

    def download_multiple(self, dest=None, first=1, last=None):
        eps = self.browser.find_elements(By.CSS_SELECTOR, '.nav_video_links')

        if not last:
            last = len(eps)

        for current in eps[int(first)-1:int(last)]:
            ep = current.get_attribute('data-vid')
            tools.info("Parsing {} episode".format(ep))
            link = current.get_attribute('data-vlnk')
            filename = "{:02d}.mp4".format(int(ep))

            tools.info("Downloading {} episode".format(ep))
            self.__download(link, dest, filename)
            tools.info("Downloaded {} episode".format(ep))

    
    def __download(self, link, dest, filename):
        original_window = self.browser.current_window_handle
        self.browser.switch_to.new_window('tab')
        self.browser.get(link)
        reg = r'https\:\/\/aser\.pro\/content\/stream\/[a-z0-9_]+\/[0-9_]+\/hls\/index\.m3u8'
        m3u8 = re.findall(reg, self.browser.page_source)[0]
        tools.FFMpeg(m3u8, os.path.join(dest, filename), self.over).exec()
        self.browser.close()
        self.browser.switch_to.window(original_window)

    def __del__(self):
        tools.info("Stopping parser")
        self.browser.quit()
        tools.info("Parser stopped")