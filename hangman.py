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
    if not check: lives -= 1


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
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    currentUser = User(username, password)
    return currentUser


def userLogin():
    username = input('Enter your username : ')
    password = input('Enter your password : ')


def userDataRecorder(username, numberofgames, numberofvictories):
    dirName = os.path.dirname(__file__)
    filePath = os.path.join(dirName, f'UserData/Users/{username}.txt')
    userRecords = open(filePath, 'a')
    nameStr = 'Username : ' + username
    gamesStr = 'Number of games played : ' + str(numberofgames)
    victoriesStr = 'Number of victories : ' + str(numberofvictories)
    dataArray = ['------------------------------------', '', nameStr, gamesStr, victoriesStr]

    for data in dataArray:
        userRecords.write(data)
        userRecords.write('\n')

    userRecords.write('\n')
    userRecords.write('\n')
    userRecords.write('\n')

    userRecords.close()


# Game On | Start Menu
print('Welcome to the hangman game!')
gamePower = gameListener()

# user data (to save on a txt file)
username = ''
numberOfGames = 0
numberOfVictories = 0

userTest = User('max4', 'allo123')
userTest.registerUserList()

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
    while lives > -1 and not finish:
        letterSelection = input('Enter a letter : ')
        checked = letterCheck(letterSelection)
        lifeCounter(checked, lives)
        finish = wordCheck()
        messageOutput(checked, finish)
        print(hiddenWord)

    gameFinishedMessage()
    gamePower = gameListener()

userData = []
