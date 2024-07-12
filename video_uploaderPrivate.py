from youtube_automation import YouTubeAutomation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class VideoUploaderPrivate(YouTubeAutomation):
    
    
    def upload_video(self, file_path):
        # Click the creation button and select the video upload option
        self.click_element(By.CSS_SELECTOR, "yt-icon-button.ytd-topbar-menu-button-renderer")
        self.click_element(By.CSS_SELECTOR, "ytd-compact-link-renderer.style-scope:nth-child(1) > a:nth-child(1)")
        time.sleep(4)
        # Enter the video file path to upload
        self.send_keys(By.CSS_SELECTOR, "#content > input:nth-child(6)", file_path)
        time.sleep(5)

    def set_video_details(self):
        print("Setting video details")
        # Adding logs to help diagnose issues
        print("Waiting for video info link")
        try:
            video_info_link_element = self.wait_for_element(By.CSS_SELECTOR, "a.ytcp-video-info", timeout=10)
            video_info_link = video_info_link_element.get_attribute('href')
            print(f"Found video info link: {video_info_link}")
        except TimeoutException:
            print("Timeout waiting for video info link")
            return None
        
        # Set video details 
        self.click_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")
        time.sleep(2)
        
        try:
            self.click_element(By.ID, "next-button")
        except TimeoutException:
            print("Timeout clicking next button")
            return None
        
        time.sleep(2)
        try:
            self.click_element(By.ID, "next-button")
        except TimeoutException:
            print("Timeout clicking next button")
            return None
        
        time.sleep(1)
        try:
            self.click_element(By.ID, "next-button")
        except TimeoutException:
            print("Timeout clicking next button")
            return None
        
        time.sleep(1)
        
        # vidéo private
        try:
            self.click_element(By.ID, "private-radio-button")
        except TimeoutException:
            print("Timeout clicking private radio button")
            return None
        
        try:
            self.click_element(By.CSS_SELECTOR, "#done-button")
        except TimeoutException:
            print("Timeout clicking done button")
            return None
        
        time.sleep(5)
        
        try:
            self.click_element(By.XPATH, '//*[@id="close-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        except TimeoutException:
            print("Timeout clicking close button")
            return None
        
        return video_info_link