# import os
# import pygame
# import subprocess
# import platform

# def Speak(data):
#     voice0 = "en-GB-SoniaNeural"
#     voice = 'en-US-SteffanNeural'
#     voice1 = 'en-US-GuyNeural'
#     voice2 = 'en-US-AriaNeural'
#     voice3 = 'en-US-JennyNeural'
#     voice4 = 'hi-IN-MadhurNeural'
#     command = f'edge-tts --voice "{voice0}" --rate=+22% --text "{data}" --write-media "C:/Users/SATYAM/Desktop/ZERO/BuildInFun/TTS/Data.mp3"'


#     try:
#         # Use subprocess to run the command and redirect output to null device.
#         subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, stdin=subprocess.DEVNULL)
#         # a = data.capitalize()
#         print(data)
#         pygame.init()
#         pygame.mixer.init()
#         pygame.mixer.music.load("C:/Users/SATYAM/Desktop/ZERO/BuildInFun/TTS/Data.mp3")

#         pygame.mixer.music.play()

#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)

#     except Exception as e:
#         print(e)
#     finally:
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()

    

# if __name__ == "__main__":
        
#     while 1:
#         i = input("Enter : ")
#         Speak(i)


import os
import pygame

def Speak(data):
    command = f'edge-tts --voice "en-GB-SoniaNeural" --rate=+22% --text "{data}" --write-media "C:/Users/SATYAM/Desktop/ZERO/BuildInFun/TTS/Data.mp3" '
    os.system(command)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:/Users/SATYAM/Desktop/ZERO/BuildInFun/TTS/Data.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__=="__main__":
    Speak("hello")  
