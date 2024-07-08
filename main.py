from video_uploader import VideoUploader
from cookie_handler import CookieHandler

def main():
    youtube = VideoUploader()
    cookie_handler = CookieHandler(youtube.driver)
    try:
        # Gérer les cookies
        cookie_handler.handle_cookies()
        # Se connecter
        youtube.login("aaoo.youteube@gmail.com", "YouTube.Aa0O")
        # Téléverser une vidéo
        youtube.upload_video(r"C:\HOME\Telechargements\video\rumble_powerup_bug.mp4")
        # Définir les détails de la vidéo
        # youtube.set_video_details()
        video_info_link = youtube.set_video_details()

        # Se déconnecter
        youtube.logout()
    
        # Naviguer vers le lien de la vidéo
        youtube.driver.get(video_info_link)
       
    finally:
        # Fermer le navigateur
        #youtube.close()
        pass


if __name__ == "__main__":
    main()
