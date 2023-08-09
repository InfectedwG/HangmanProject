import json
from random import random
from user import User

theme1 = ["mazda", "honda", "nissan", "subaru"]
theme2 = ['apple', 'orange', 'grape', 'watermelon']


def selectTheme():
    if themeChosen == 1:
        return theme1
    else:
        return theme2


def letterCheck(letter):
    check = False
    for i in range(len(word)):
        if word[i] == letter:
            hiddenWord[i] = letter
            check = True
    return check


def wordCheck():
    if hiddenWord == wordKey:
        return True
    else:
        return False


def messageOutput(check, finish):
    if check and not finish:
        print('nice! next!')
    elif not check and not finish:
        print('try again!')
        print('number of lives : ' + str(lives))


def lifeCounter(check, lives):
    if not check:
        lives -= 1
    return lives


def gameFinishedMessage():
    if lives >= 0 and wordCheck():
        print("Congrats!")
    else:
        print("Loser haha!")


def gameListener():
    gamePowerInput = input('Type ''y'' to start a new game or ''n'' to close the game : ')
    gamePower = True
    if gamePowerInput == 'y':
        print('Good luck!')
        gamePower = True
    elif gamePowerInput == 'n':
        print('Alright see you next time!')
        gamePower = False
    else:
        print('Invalid answer, please enter y or n!')
        gameListener()

    return gamePower


def userRegister():
    print('Registering...')
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    currentUser = User(username, password)
    confirmation = currentUser.registerUserList()
    if not confirmation:
        print('Registration completed succesfully')
        print('Please login to continue : ')
        return True
    else:
        print('The username entered already exists. Please try again : ')
        userRegister()


def userLogin():
    print('Logging in...')
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    currentUser = User(username, password)
    confirmation = currentUser.userLoginFile()
    if confirmation:
        return currentUser
    else:
        print('Wrong username or password, please try again : ')
        userLogin()



def startMenuInterface():
    print('Do you want to create an account (create), login (login) or continue as a guest (guest)?')
    choice = input('Type one of the word in parentheses and press enter to make your selection : ')
    registrationCompleted = False
    currentUser = None
    if choice == 'create':
        registrationCompleted = userRegister()
        if registrationCompleted:
            currentUser = userLogin()
    elif choice == 'login':
        currentUser = userLogin()
    elif choice == 'guest':
        print('Your progress will not be saved')
    else:
        print('Error. Either a typo or you''re trying to pull a fast one on me')
        startMenuInterface()

    return currentUser

# Game On | Start Menu
print('Welcome to the hangman game!')

currentUser = startMenuInterface()
#print(currentUser)
currentUser.userDataRecorder(1, 1)
gamePower = gameListener()

# user data (to save on a txt file)
username = ''
numberOfGames = 0
numberOfVictories = 0

#userDataRecorder(username, numberOfGames, numberOfVictories)

# session loop
while gamePower:
    lives = 5
    themeChosen = int(input('Select a theme : '))
    currentTheme = selectTheme()
    randomWordSelection = int(random() * 4)
    word = currentTheme[randomWordSelection]
    hiddenWord = []
    wordKey = []
    finish = False
    for i in range(len(word)):
        hiddenWord.append('_')
        wordKey.append(word[i])

    print(hiddenWord)

    # game loop
    while lives > 0 and not finish:
        letterSelection = input('Enter a letter : ')
        checked = letterCheck(letterSelection)
        lives = lifeCounter(checked, lives)
        finish = wordCheck()
        messageOutput(checked, finish)
        print(hiddenWord)

    numberOfGames += 1
    if finish:
        numberOfVictories += 1

    gameFinishedMessage()
    gamePower = gameListener()
    if not gamePower:
        currentUser.userDataRecorder(numberOfGames, numberOfVictories)

print(currentUser.userDataRetriever())
