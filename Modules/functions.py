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
 
 
 def textbox():
    DISPLAY.fill(CYAN)
    back_button = button(0, 550, 175, 50, "Cancel...")
    back_button.draw()
    rect = pygame.draw.rect(DISPLAY, GREY, (200, 300, 300, 50))
    font = pygame.font.SysFont("courier new", 40)
    usr_string = ""
    while True:
        for event in pygame.event.get():
            #Rendering the cancel button
            back_button.update(event)
            if back_button.ButtonClicked == True:
                return False
            #Checking if quit attempt has been made.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Checking if a key was pressed down.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    usr_string = usr_string[:-1] #Removes the last character from string
                    DISPLAY.fill(GREY, (rect.x, rect.y, rect.width, rect.height)) #Fills textbox modified string can render over
                elif event.key == 13:
                    if len(usr_string) > 15:
                        print("Username should be less than 15 characters long!")
                    else:
                        return usr_string #usr_string returned to function to commit to database
                elif event.key >= 97 and event.key <= 122: #A-Z keys
                    usr_string += event.unicode
                elif event.key >= 48 and event.key <= 57: #0-9 keys
                    usr_string += str(event.unicode)
            txt = font.render(usr_string, True, TEXT_COLOUR)
            DISPLAY.blit(txt, (rect.x + 5, rect.y + 5))
            pygame.display.flip()
