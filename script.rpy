# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lola")


# The game starts here.

label start:

    init python:
        import requests

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "Lola happy.png" to the images
    # directory.

    show Lola happy

    # These display lines of dialogue.

    l "This is a Ren'Py Boilerplate for Lovense Connectivity."

    l "Users set up a toy, then continue on with the story. They recieve vibrations to their toy as they play."

    l "The basics are done for you!"

    l "Let's test it out!"

label set_up:

    l "Open your Lovense Remote app and go to Settings. Enable 'Game Mode' and get ready to enter your info! Ensure your phone is connected to the same network as the game."

    l "If you are using the PC Remote app, enable third parties control. Your config info is entered by default during setup. (IP= 127-0-0-1, SSLport= 30010)"
    
    $ address = renpy.input("What is your local IP listed in the Lovense Remote App (Game Mode)?", "127-0-0-1")
    $ SSLport = renpy.input("What is your SSL port?", "30010")

    l "Your config is [address], [SSLport]"

    python:
        url = "https://" + address + ".lovense.club:" + SSLport + "/command"
        try:
            response = requests.post(url, json={"command": "Function", "action": "Vibrate:20", "timeSec": 1, "apiVer": 1}, verify=False)
            print(response.json())
        except:
            renpy.notify("ERROR: Toys are NOT connected, please try again! Are you connected to the APP?")
            #To force the player to set up toys first and NOT continue with the story, remove the '#' on the next line
            #renpy.jump("set_up")

    l "Your toys should be set up, unless a pop-up says otherwise! Enjoy the ride."

label story:
    scene bg room 
    show Lola happy

    l "Here is where your story starts!"
    
    l "Vibrations can be added as needed."

    python:
        try:
            response = requests.post(url, json={"command": "Pattern", "rule": "V:1;F:vrp;S:1000#", "strength": "20;15;20;15;20;10;20;20", "timeSec": 30,"apiVer": 1}, verify=False)
            print(response.json())
        except:
            renpy.notify("ERROR: Toys are NOT connected, please try again! Are you connected to the APP?")
                #To force the player to set up toys first and NOT continue with the story, remove the '#' on the next line
            #renpy.jump("set_up")
    
    l "This concludes the boilerplate. For help, reach out to the boilerplate developer {a=https://github.com/lolabray}Lola Bray{/a}"


    # This ends the game.

    return
