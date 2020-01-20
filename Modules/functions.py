import pygame
from button import button
from variables import *

profile1 = {
"ProfileName": "Example",
"SongsPlayed": 750,
"TimePlayed": "07:05:51",
 "Level": 10
}
profile2 = {
"ProfileName": "Example2",
"SongsPlayed": 215,
"TimePlayed": "12:05:51",
"Level": 14
}


def profileMenu(profile1, profile2):
    #Handles the rendering and logic to display the profile menu.
    #Only two profiles can be loaded at a time.. make prompt to choose which.
    DISPLAY.fill(CYAN)
    pygame.display.flip()
    profileString1 = "Profile: " + profile1["ProfileName"] #First line, passed into button constructor

    #Split each line into an element.
    profileStringList1 = [
    "Songs Played: " + str(profile1["SongsPlayed"]),
    "Time Played: " + str(profile1["TimePlayed"]),
    "Level: " + str(profile1["Level"])
    ]
    profile1_button = button(0, 10, 500, 200, profileString1)
    profile2_button = button(0, 250, 500, 200, profile2["ProfileName"]) #Test to see space on screen
    back_button = button(0, 550, 175, 50, "<< Back")
    create_button = button(500, 550, 275, 50, "New Profile")
    
    profile1_button.draw()
    profile1_button.addText(profileStringList1)

    profile2_button.draw()
    back_button.draw()
    create_button.draw()
    while True:
        #Getting events and updating screen.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Updates each button. Branches again here.
            profile1_button.update(event)
            if profile1_button.ButtonClicked == True:
                print("Works!")
                songMenu()
            back_button.update(event)
            if back_button.ButtonClicked == True:
                DISPLAY.fill(CYAN)
                return False
            create_button.update(event)
            if create_button.ButtonClicked == True:
                print("Yes")
            profile2_button.update(event)
            pygame.display.flip()
def songMenu():
    pass
