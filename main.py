import pygame
import sys
from Modules.button import *
from Modules.functions import profileMenu
from Modules.function import songMenu


profiles = []
fetch = cursor.execute("SELECT * from profiles")
for profile in fetch:
    profiles.append(profile)

print(profiles)

profile1 = {
"ProfileName": str(profiles[0][1]),
"SongsPlayed": str(profiles[0][2]),
"TimePlayed": str(profiles[0][3]),
 "Level": str(profiles[0][4])
}
profile2 = {
"ProfileName": str(profiles[1][1]),
"SongsPlayed": str(profiles[1][2]),
"TimePlayed": str(profiles[1][3]),
"Level": str(profiles[1][4])
}

if __name__ == "__main__":
    pygame.display.set_caption("Psychic Journey")
    DISPLAY.fill(CYAN)
    icon = pygame.image.load("Psychic Journey.png") #Loads the image.
    DISPLAY.blit(icon, (250, 45)) #Blits the image on the surface at 250,45

    #Instances of button.
    play_button = button(50, 100, 100, 50, "Play")
    settings_button = button(50, 300, 200, 50, "Settings")
    guide_button = button(50, 200, 300, 50, "Instructions")
    quit_button = button(50, 400, 100, 50, "Quit")

    #Calls draw method for each
    play_button.draw()
    settings_button.draw()
    quit_button.draw()
    guide_button.draw()

    #Game loop
    while True:
        #Getting events and updating screen.
        for event in pygame.event.get(): #pygame.event.get returns a list of events.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Updates each button as per class methods.
            #Branching starts here.
            play_button.update(event)
            if play_button.ButtonClicked == True:
                profileMenu(profile1, profile2)
                icon = pygame.image.load("Psychic Journey.png")
                DISPLAY.blit(icon, (250, 45))
            settings_button.update(event)
            if settings_button.ButtonClicked == True:
                pass
            quit_button.update(event)
            if quit_button.ButtonClicked == True:
                pygame.quit()
                sys.exit()
            guide_button.update(event)
            if guide_button.ButtonClicked == True:
                pass
            pygame.display.flip() #Updates the whole screen.
            clock.tick(60) #60 FPS cap
