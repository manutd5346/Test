import pygame
import time

class Music:

    def play(self):
        pygame.init()
        music_file = "apt.mp3"   # mp3 or mid file
        freq = 16000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
        bitsize = -16   # signed 16 bit. support 8,-8,16,-16
        channels = 1    # 1 is mono, 2 is stereo
        buffer = 2048   # number of samples (experiment to get right sound)

        # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.load(music_file)

        play_clock = pygame.time.Clock()

        pygame.mixer.music.play()
        time.sleep(15)
        pygame.mixer.music.stop()

        running = True
        while running:
            for event in pygame.event.get():
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                    #play sound
                        pygame.mixer.Sound.play(beep_sound)
                    if event.key == pygame.K_p:
                    #play music
                        pygame.mixer.music.play(-1)
                    if event.key == pygame.K_s:
                    #stop music
                        pygame.mixer.music.stop()
                  
        #Draw Section
        DISPLAYSURF.fill((128, 128, 128))

        pygame.display.flip()

        #pygame.mixer.music.play()

        #clock = pygame.time.Clock()
        #while pygame.mixer.music.get_busy():
         #   print("playing... -func => playmusic")
          #  clock.tick(10)
            
        #pygame.mixer.quit()

         
 

if __name__ == '__main__':
   test = Music()
   test.play()
#   test.stop()     


