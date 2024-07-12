from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class YouTubeAutomation:
    
    def __init__(self):
        # Initialiser le navigateur Firefox
        self.driver = webdriver.Firefox()
        # Accéder à la page d'accueil de YouTube
        self.driver.get("https://www.youtube.com/")

    def close(self):
        # Fermer le navigateur
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=10):
        # Attendre que l'élément soit présent
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        # Attendre et cliquer sur l'élément
        element = self.wait_for_element(by, value)
        element.click()

    def send_keys(self, by, value, keys):
        # Attendre et envoyer des touches à l'élément
        element = self.wait_for_element(by, value)
        element.send_keys(keys)

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        print(f"Entering text in element by {by} with value {value}")
        element.send_keys(text)

    def login(self, email, password):
        # Attendre que la superposition disparaisse
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "opened")))

        # Cliquer sur le bouton "Se connecter"
        self.click_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a")
        time.sleep(2)

        # Saisir l'adresse email et valider
        self.send_keys(By.XPATH, "//*[@id='identifierId']", email)
        self.send_keys(By.XPATH, "//*[@id='identifierId']", Keys.ENTER)
        time.sleep(2)

        # Saisir le mot de passe et valider
        self.send_keys(By.CSS_SELECTOR, "#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)", password)
        self.send_keys(By.CSS_SELECTOR, "#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)", Keys.ENTER)

    def logout(self):
        # Cliquer sur le bouton de compte et se déconnecter
        self.click_element(By.ID, "account-button")
        time.sleep(2)
        self.click_element(By.CSS_SELECTOR, "ytd-compact-link-renderer.style-scope:nth-child(4) > a:nth-child(1)")
        time.sleep(2)
