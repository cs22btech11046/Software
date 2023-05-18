import pygame
import random
import os
def play_random_song(playlist):
    random.shuffle(playlist)  # Shuffle the playlist randomly

    pygame.mixer.init()

    for song in playlist:
        print(f"Now playing: {song}")
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            command = input("Enter a command (pause/play/next/exit): ")
            if command == "pause":
                pygame.mixer.music.pause()
            elif command == "unpause":
                pygame.mixer.music.unpause()
            elif command == "next":
                pygame.mixer.music.stop()
                break
            elif command == "exit":
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                return    

    pygame.mixer.quit()
    
downloads_folder = os.path.join(os.path.expanduser("~/Software"), "Playlist")


playlist = [
    os.path.join(downloads_folder, "IMG_0553.mp3"),
    os.path.join(downloads_folder, "IMG_0555.mp3"),
    os.path.join(downloads_folder, "IMG_0556.mp3"),
    os.path.join(downloads_folder, "IMG_0557.mp3"),
    os.path.join(downloads_folder, "IMG_0558.mp3"),
    os.path.join(downloads_folder, "IMG_0559.mp3"),
    os.path.join(downloads_folder, "IMG_0560.mp3"),
    os.path.join(downloads_folder, "IMG_0561.mp3"),
    os.path.join(downloads_folder, "IMG_0562.mp3"),
    os.path.join(downloads_folder, "IMG_0563.mp3"),
    os.path.join(downloads_folder, "IMG_0565.mp3"),
    os.path.join(downloads_folder, "IMG_0566.mp3"),
    os.path.join(downloads_folder, "IMG_0567.mp3"),
    os.path.join(downloads_folder, "IMG_0568.mp3"),
    os.path.join(downloads_folder, "IMG_0569.mp3"),
    os.path.join(downloads_folder, "IMG_0570.mp3"),
    os.path.join(downloads_folder, "IMG_0571.mp3"),
    os.path.join(downloads_folder, "IMG_0572.mp3"),
    os.path.join(downloads_folder, "IMG_0574.mp3"),
    os.path.join(downloads_folder, "IMG_0575.mp3"),
]

play_random_song(playlist)
