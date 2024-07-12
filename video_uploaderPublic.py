from youtube_automation import YouTubeAutomation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class VideoUploaderPublic(YouTubeAutomation):
    
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
        video_info_link_element = self.wait_for_element(By.CSS_SELECTOR, "a.ytcp-video-info", timeout=10)
        video_info_link = video_info_link_element.get_attribute('href')
        print(f"Found video info link: {video_info_link}")
        
        # Set video details 
        self.click_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")
        time.sleep(2)
        self.click_element(By.ID, "next-button")
        time.sleep(2)
        self.click_element(By.ID, "next-button")
        time.sleep(1)
        self.click_element(By.ID, "next-button")
        time.sleep(1)
    
        # # vidéo Public:
        self.click_element(By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]')
        time.sleep(2)
        self.click_element(By.CSS_SELECTOR, "#done-button")
        time.sleep(1)

        self.click_element(By.XPATH, '//*[@id="close-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        
        return video_info_link

        
        
