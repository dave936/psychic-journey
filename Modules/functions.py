import pygame
from Modules.button import button
from Modules.variables import *
import sqlite3


def profileMenu(profile1, profile2):
    #Handles the rendering and logic to display the profile menu.
    #Only two profiles can be loaded at a time.. make prompt to choose which.
    DISPLAY.fill(CYAN)
    pygame.display.flip()
    profiles = []
    index = 1
    fetch = cursor.execute("SELECT * FROM profiles")
    for profile in fetch:
        profiles.append(profile)
    
    
    profileName1 = "Profile: " + profile1["ProfileName"] #First line, passed into button constructor

    #Split each line into an element.
    profileStringList1 = [
    "Songs Played: " + str(profile1["SongsPlayed"]),
    "Time Played: " + str(profile1["TimePlayed"]),
    "Level: " + str(profile1["Level"])
    ]

    profileName2 = "Profile: " + profile2["ProfileName"]
    profileStringList2 = [
    "Songs Played: " + str(profile2["SongsPlayed"]),
    "Time Played: " + str(profile2["TimePlayed"]),
    "Level: " + str(profile2["Level"]),
    ]

    #Defining buttons
    profile1_button = button(0, 10, 500, 200, profileName1)
    profile2_button = button(0, 250, 500, 200, profileName2) #Test to see space on screen
    back_button = button(0, 550, 175, 50, "<< Back")
    create_button = button(500, 550, 275, 50, "New Profile")
    left_arrow_button = button(250, 475, 45, 45, "<<")
    right_arrow_button = button(450, 475, 45, 45, ">>")

    #Drawing the buttton and adding more text.
    profile1_button.draw()
    profile1_button.addText(profileStringList1)

    profile2_button.draw()
    profile2_button.addText(profileStringList2)
    
    left_arrow_button.draw()
    right_arrow_button.draw()
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
                print("Returning...")
                return False
            profile2_button.update(event)
            create_button.update(event)
            if create_button.ButtonClicked == True:
                new_user = textbox()
                profileFetch = cursor.execute("SELECT * from profiles") #Returned as an iterable SQL object.
                profileIDs = []
                for p in profileFetch:
                    profileIDs.append(p[0]) # The 0th index it the primary key.
                max_profileID = max(profileIDs) #Getting the maximum value.
                
                new_profileID = max_profileID + 1
                query = "INSERT INTO profiles VALUES({profileID}, '{username}', 0, 0, 0)".format(profileID=str(new_profileID), username=str(new_user))
                cursor.execute(query)
                name = cursor.execute("SELECT * from profiles WHERE profileID={profileID}".format(profileID=str(new_profileID))) #Tests to see if the profile was inserted.
                for c in name:
                    print(c[1]) #Name entered previously is put in variable.
                conn.commit()
                profiles = []
                index = 1
                fetch = cursor.execute("SELECT * FROM profiles")
                for profile in fetch:
                    profiles.append(profile)
                DISPLAY.fill(CYAN)
            left_arrow_button.update(event)
            if left_arrow_button.ButtonClicked == True:
                previous_1 = index - 3
                previous_2 = index - 2

                if previous_1 < 0:
                    pass
                else:
                    #In case of an index error, use try-except cases.
                    try:
                        profile1 = {
                        "ProfileName": str(profiles[previous_1][1]),
                        "SongsPlayed": str(profiles[previous_1][2]),
                        "TimePlayed": str(profiles[previous_1][3]),
                        "Level": str(profiles[previous_1][4]),
                        }
                        profile2 = {
                        "ProfileName": str(profiles[previous_2][1]),
                        "SongsPlayed": str(profiles[previous_2][2]),
                        "TimePlayed": str(profiles[previous_2][3]),
                        "Level": str(profiles[previous_2][4]),
                        }
                        profileName1 = "Profile: " + profile1["ProfileName"] #First line, passed into button constructor

                        #Split each line into an element.
                        profileStringList1 = [
                        "Songs Played: " + str(profile1["SongsPlayed"]),
                        "Time Played: " + str(profile1["TimePlayed"]),
                        "Level: " + str(profile1["Level"])
                        ]

                        profileName2 = "Profile: " + profile2["ProfileName"]
                        profileStringList2 = [
                        "Songs Played: " + str(profile2["SongsPlayed"]),
                        "Time Played: " + str(profile2["TimePlayed"]),
                        "Level: " + str(profile2["Level"]),
                        ]

                        DISPLAY.fill(CYAN)

                        DISPLAY.fill(GREY, (0, 10, 500, 200))
                        DISPLAY.fill(GREY, (0, 250, 500, 200))

                        #Re-defining buttons
                        profile1_button = button(0, 10, 500, 200, profileName1)
                        profile2_button = button(0, 250, 500, 200, profileName2)

                        profile1_button.addText(profileStringList1)
                        profile2_button.addText(profileStringList2)

                        index -= 2
                    except Exception as e:
                        print("Max Page reached")
   
            right_arrow_button.update(event)
            if right_arrow_button.ButtonClicked == True:
                next_1 = index + 1
                next_2 = index + 2

                try:
                    #In case of an index error, use try-except error.
                    profile1 = {
                    "ProfileName": str(profiles[next_1][1]),
                    "SongsPlayed": str(profiles[next_1][2]),
                    "TimePlayed": str(profiles[next_1][3]),
                    "Level": str(profiles[next_1][4]),
                    }
                    profile2 = {
                    "ProfileName": str(profiles[next_2][1]),
                    "SongsPlayed": str(profiles[next_2][2]),
                    "TimePlayed": str(profiles[next_2][3]),
                    "Level": str(profiles[next_2][4]),
                    }
                    profileName1 = "Profile: " + profile1["ProfileName"] #First line, passed into button constructor

                    #Split each line into an element.
                    profileStringList1 = [
                    "Songs Played: " + str(profile1["SongsPlayed"]),
                    "Time Played: " + str(profile1["TimePlayed"]),
                    "Level: " + str(profile1["Level"])
                    ]

                    profileName2 = "Profile: " + profile2["ProfileName"]
                    profileStringList2 = [
                    "Songs Played: " + str(profile2["SongsPlayed"]),
                    "Time Played: " + str(profile2["TimePlayed"]),
                    "Level: " + str(profile2["Level"]),
                    ]

                    DISPLAY.fill(GREY, (0, 10, 500, 200))
                    DISPLAY.fill(GREY, (0, 250, 500, 200))

                    #Defining buttons
                    profile1_button = button(0, 10, 500, 200, profileName1)
                    profile2_button = button(0, 250, 500, 200, profileName2)

                    profile1_button.addText(profileStringList1)
                    profile2_button.addText(profileStringList2)

                    index += 2


                except Exception as e:
                    try:
                        profile1 = {
                        "ProfileName": str(profiles[next_1][1]),
                        "SongsPlayed": str(profiles[next_1][2]),
                        "TimePlayed": str(profiles[next_1][3]),
                        "Level": str(profiles[next_1][4])
                        }
                        profileName1 = "Profile: " + profile1["ProfileName"] #First line, passed into button constructor

                        #Split each line into an element.
                        profileStringList1 = [
                        "Songs Played: " + str(profile1["SongsPlayed"]),
                        "Time Played: " + str(profile1["TimePlayed"]),
                        "Level: " + str(profile1["Level"])
                        ]
                        DISPLAY.fill(GREY, (0, 10, 500, 200))
                        DISPLAY.fill(GREY, (0, 250, 500, 200))

                        profile1_button = button(0, 10, 500, 200, profileName1)
                        profile1_button.addText(profileStringList1)
                        profile2_button = button(0, 250, 500, 200, "")
                        index += 2
                    except Exception as c:
                        print("Max page reached")
                        
            pygame.display.flip()


def songMenu():
    pass

def textbox():
    DISPLAY.fill(CYAN)
    pygame.display.flip()
    back_button = button(0, 550, 175, 50, "Cancel")
    back_button.draw() 
    rect = pygame.draw.rect(DISPLAY, GREY, (0, 300, 800, 50))#Create the rectangle where the text will be entered.
    
    font = pygame.font.SysFont("courier new", 40)
    small_font = pygame.font.SysFont("courier new", 20)
    
    usr_string = ""
    instruct = "Enter the name of your profile:"
    instruct_txt = font.render(instruct, True, TEXT_COLOUR)#Render the text of the font.
    
    max_text = "Username must be less than 15 characters!"
    max_text_render = small_font.render(max_text, True, TEXT_COLOUR) 
    
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
                        DISPLAY.blit(max_text_render, (rect.x, rect.y + 50)) #Blits a prompt below the rectangle.
                    else:
                        return usr_string #usr_string returned to function to commit to database
                elif event.key >= 97 and event.key <= 122: #A-Z keys
                    usr_string += event.unicode #Translate the key pressed to a character and add it to the string.
                elif event.key >= 48 and event.key <= 57: #0-9 keys
                    usr_string += str(event.unicode)
            txt = font.render(usr_string, True, TEXT_COLOUR) #Render the font.
            DISPLAY.blit(txt, (rect.x + 5, rect.y + 5)) #Put it on the screen, inside the rectangle.
            instruct_txt = font.render(instruct, True, TEXT_COLOUR) #Renders the instruction on the screen
            DISPLAY.blit(instruct_txt, (rect.x, rect.y - 50)) #Blits a little above the rectangle.
            pygame.display.flip() 

