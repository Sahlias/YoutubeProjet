from video_uploaderPrivate import VideoUploaderPrivate
from video_uploaderPublic import VideoUploaderPublic
from video_detailsUnlisted import VideoDetailsUnlisted
from cookie_handler import CookieHandler
import traceback


def upload_private_videos():
    try:
        # Instanciation du driver et des classes nécessaires
        youtube_private = VideoUploaderPrivate()
        cookie_handler = CookieHandler(youtube_private.driver)
        

        # Gérer les cookies
        cookie_handler.handle_cookies()

        # Se connecter et travailler avec les vidéos privées
        youtube_private.login("aaoo.youteube@gmail.com", "YouTube.Aa0O")
        video_file_path_private = r"C:\HOME\Telechargements\video\rumble_powerup_bug.mp4"
        youtube_private.upload_video(video_file_path_private)
        video_info_link_private = youtube_private.set_video_details()
        youtube_private.logout()

        # Exemple de navigation vers le lien de la vidéo privée
        youtube_private.driver.get(video_info_link_private)

    except Exception as e:
        print(f"Une erreur est survenue lors du téléversement des vidéos privées : {str(e)}")
        traceback.print_exc()
    finally:
        # Fermer le navigateur
        youtube_private.close()


def upload_public_videos():
    try:
        # Instanciation du driver et des classes nécessaires
        youtube_public = VideoUploaderPublic()
        cookie_handler = CookieHandler(youtube_public.driver)

        # Gérer les cookies
        cookie_handler.handle_cookies()

        # Se connecter et travailler avec les vidéos publiques
        youtube_public.login("aaoo.youteube@gmail.com", "YouTube.Aa0O")
        video_file_path_public = r"C:\HOME\Telechargements\video\rumble_powerup_bug.mp4"
        youtube_public.upload_video(video_file_path_public)
        video_info_link_public = youtube_public.set_video_details()
        youtube_public.logout()

        # Exemple de navigation vers le lien de la vidéo publique
        youtube_public.driver.get(video_info_link_public)

    except Exception as e:
        print(f"Une erreur est survenue lors du téléversement des vidéos publiques : {str(e)}")
        traceback.print_exc()
    finally:
        # Fermer le navigateur
        youtube_public.close()


def upload_unlisted_videos():
    try:
        # Instanciation du driver et des classes nécessaires
        youtube_unlisted = VideoDetailsUnlisted()
        cookie_handler = CookieHandler(youtube_unlisted.driver)

        # Gérer les cookies
        cookie_handler.handle_cookies()

        # Se connecter et travailler avec les vidéos non répertoriées
        youtube_unlisted.login("aaoo.youteube@gmail.com", "YouTube.Aa0O")
        video_file_path_unlisted = r"C:\HOME\Telechargements\video\rumble_powerup_bug.mp4"
        youtube_unlisted.upload_video(video_file_path_unlisted)
        video_info_link_unlisted = youtube_unlisted.set_video_details()
        youtube_unlisted.logout()

        # Exemple de navigation vers le lien de la vidéo non répertoriée
        youtube_unlisted.driver.get(video_info_link_unlisted)

    except Exception as e:
        print(f"Une erreur est survenue lors du téléversement des vidéos non répertoriées : {str(e)}")
        traceback.print_exc()
    finally:
        # Fermer le navigateur
        youtube_unlisted.close()


def main():
    # Appeler chaque fonction séparément pour exécuter chaque partie
    upload_private_videos()
    upload_public_videos()
    upload_unlisted_videos()


if __name__ == "__main__":
    main()
