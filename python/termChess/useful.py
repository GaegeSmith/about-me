# https://www.kite.com/python/answers/how-to-create-functions-with-optional-arguments-in-python
import re
from os import system, name
import random
import time
import cmath
import math



# below 2 lines grab the current users desktop, and make it a directory you can import from
# import sys, getpass
# sys.path.insert(1, "C:\\Users\\" + getpass.getuser() + "\\Desktop")
# sources
    # https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
    # https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python



# signal(SIGINT, Terminal.signal_handler)
# def signal_handler():
#         stdout.write("\x1B[2D") # moves cursor back 2 so that when user enter ^c to quit, these characters don't appear
#         quit()


class Dice:
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        return self.random.randint(1, self.sides)

class Maths:
    

    class Stats:
        def ave(nums):
            return sum(nums)/len(nums)

        def rag(nums):
            return (max(nums) - min(nums))

        def basicStats(listOfNums):
            minNum = min(listOfNums)
            maxNum = max(listOfNums)
            sumNum = sum(listOfNums)
            aveNum = Maths.Stats.ave(listOfNums)
            rngNum = Maths.Stats.rag(listOfNums)
            return minNum, maxNum, sumNum, aveNum, rngNum

    class Graphs:

        def quadratic(a, b, c):
            insideSQRT = (b * b) - 4 * a * c
            print(insideSQRT)
            denom = 2 * a
            print(denom)
            negB = -1 * b
            print(negB)
            posRoot = (negB + cmath.sqrt(insideSQRT)) / denom
            negRoot = (negB - cmath.sqrt(insideSQRT)) / denom

            return posRoot, negRoot

        def distance(x1, y1, x2, y2):
            return math.sqrt((float(x2)-x1) ** 2 + (y2-y1) ** 2)

    def tax(subTotal, taxAsIntOutOf100):
        return (1 + (taxAsIntOutOf100 / 100) ) * subTotal




    def halfTime():
        return random.randint(0,1) == 1


    # checks if a number is prime
    def isPrime(number):
        prime = False
        if number == 2:
            prime = True
        elif number == 1:
            prime = False
        elif number == 3:
            prime = True
        elif number == 5:
            prime = True
        elif number == 7:
            prime = True
        else:
            # is the number divisible evenly by every number between 2 and half of itself
            for i in range(2, ((number//2) + 2)):
                numDivided = number % i
                if (numDivided != 0):
                    prime = True
                else:
                    prime = False
                    break
        return prime


    def rng(numNumsWant, rndStart, rndEnd):
        numlist = []
        for i in range(numNumsWant):
            numlist.append(random.randint(rndStart, rndEnd))
        return (numlist)

class Terminal:
    class Color:
        # print("\033[1;37;40m" + "\033[2;37:40m" + "TextColour BlackBackground          WhiteText ColouredBackground\033[0;40m\n")
        # print("\033[1;30;40m Dark Gray      \033[0m \\033[1;30;40m               \033[0;41m Black      \033[0m \\033[0;41m")
        # print("\033[1;31;40m Bright Red     \033[0m \\033[1;31;40m               \033[0;42m Black      \033[0m \\033[0;42m")
        # print("\033[1;32;40m Bright Green   \033[0m \\033[1;32;40m               \033[0;43m Black      \033[0m \\033[0;43m")
        # print("\033[1;33;40m Yellow         \033[0m \\033[1;33;40m               \033[0;44m Black      \033[0m \\033[0;44m")
        # print("\033[1;34;40m Bright Blue    \033[0m \\033[1;34;40m               \033[0;45m Black      \033[0m \\033[0;45m")
        # print("\033[1;35;40m Bright Magenta \033[0m \\033[1;35;40m               \033[0;46m Black      \033[0m \\033[0;46m")
        # print("\033[1;36;40m Bright Cyan    \033[0m \\033[1;36;40m               \033[0;47m Black      \033[0m \\033[0;47m")
        # print("\033[1;37;40m White          \033[0m \\033[1;37;40m               \033[0;48m Black      \033[0m \\033[0;48m")
        # https://ozzmaker.com/add-colour-to-text-in-python/
        RED = '\033[1;31;40m'
        GREEN = '\033[1;32;40m'
        YELLOW = '\033[1;33;40m'
        BLUE = '\033[1;34;40m'
        PURPLE = '\033[1;35;40m'
        CYAN = '\033[1;36;40m'
        WHITE = '\033[1;37;40m'
        DARKGREY = '\033[1;30;40m'
        
        BACKGREY = '\033[0;40m'
        BACKRED = '\033[0;41m'
        BACKGREEN = '\033[0;42m'
        BACKYELLOW = '\033[0;43m'
        BACKBLUE = '\033[0;44m'
        BACKPURPLE = '\033[0;45m'
        BACKCYAN = '\033[0;46m'
        BACKWHITE = '\033[0;48m'

        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        listOfColors = [
            RED,
            GREEN,
            YELLOW,
            BLUE,
            PURPLE,
            CYAN,
            WHITE,
            DARKGREY,
            BACKGREY,
            BACKRED,
            BACKGREEN,
            BACKYELLOW,
            BACKBLUE,
            BACKPURPLE,
            BACKCYAN,
            BACKWHITE,
            BOLD,
            UNDERLINE,
            END,
        ]

    def clear():
        # https://www.geeksforgeeks.org/clear-screen-python/
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    def pause():
        input()
        Terminal.clear()


    def clearCurrLine():
        # https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console/51388326
        # clear line above and move cursor up to it
        print("\033[A                             \033[A")

    # ask for input until input is a number
    def intput(msg):
        num = 0
        while True:
            num = input(msg)
            if num.isdigit() or (len(num) > 1 and(num[0] == "-" and num[1:].isdigit())):
                num = int(num)
                break
        return num

    
    def delayPrint(s, delay = 0.04, skipSpaces = True):
        # print(delay)
        skip = False
        for c in range(len(s)):
            print(s[c], end = "", flush = True)
            
            if s[c] == '\033':
                skip = True

            elif s[c - 1] in Strings.lets('0', '9') and s[c] == 'm':
                skip = False

            if (s[c] == " " and skipSpaces) or skip:
                time.sleep(0)
            else:
                time.sleep(delay)
        print()

    def delayInput(msg, delay):
        skip = False
        for c in range(len(msg)):
            print(msg[c], end = "", flush = True)
            
            if msg[c] == '\033':
                skip = True

            elif msg[c - 1] in Strings.lets('0', '9') and msg[c] == 'm':
                skip = False

            if msg[c] == " " or skip:
                time.sleep(0)
            else:
                time.sleep(delay)
        return input()

    def inputFlt(msg):
        num = 0
        while True:
            num = input(msg)
            if ("." in num):
                splitterList = num.split(".")
                if ((splitterList[0].isdigit() or (splitterList[0][0] == "-" and splitterList[0][1:].isdigit())) and splitterList[1].isdigit() and len(splitterList) == 2):
                    break

    def inputChecker(ui, reqInput):
        match = False
        copyInput = ui
        if reqInput == "int":
            if copyInput.isdigit() or (copyInput[0] == "-" and copyInput[1:].isdigit()):
                match = True
                
        elif reqInput == "float":
            if ("." in copyInput):
                splitterList = copyInput.split(".")
                if ((splitterList[0].isdigit() or (splitterList[0][0] == "-" and splitterList[0][1:].isdigit())) and splitterList[1].isdigit() and len(splitterList) == 2):
                    match = True
    
        elif type(reqInput) == int:
            if int(copyInput) == reqInput:
                match = True

        elif type(reqInput) == float:
            if float(copyInput) == reqInput:
                match = True

        elif type(reqInput) == list or type(reqInput) == tuple:
            if copyInput in reqInput:
                match = True
        
        elif type(reqInput) == str:
            if copyInput == reqInput:
                match = True

        return match

    def matrix():
        while True:
            print(random.randint(0, 1), end = "")



    # custom print function that takes in 2 lists
    #  and a description and outputs them as ordered pairs
    def dataSetPrint(listDesc0, listDesc1, inputList0, inputList1):
        output = f"({listDesc0}, {listDesc1})\n"
        for i in inputList0:
            output += f"({i}, {inputList1[inputList0.index(i)]})\n"
        return output

class Strings:
    def formatAsMoney(val):
        return ('$' + '{:,.2f}'.format(val))

    # function takes in a definition and a dictionary and returns the [index] to get to it, if its an n-D dict, returns full path
    def findInDict(definition, dicty, temp = "NULL"):
        for i in dicty:
            if type(dicty[i]) == dict:
                temp = Strings.findInDict(definition, dicty[i], i)
            
            if temp != "NULL":
                if dicty[i] == definition:
                    return f"['{temp}']['{i}']"
                return temp

    # checks if a list contains a certain number of some data
    def contains(listy, num, someData):
        numOfData = 0
        for i in listy:
            if i == someData:
                numOfData += 1
        return numOfData == num


    # how many different letters are in a list
    def numLetLst(list0):
        count = 0
        newList = []
        for i in list0:
            newList.append(i)
        for i in Strings.lets("a", "z"):
            while i in newList:
                index = newList.index(i)
                newList[index] = "§"
                count += 1
        
        for i in Strings.lets("A", "Z"):
            while i in newList:
                    index = newList.index(i)
                    newList[index] = "§"
                    count += 1
            
        return count

    def indexOfDict(number, dicty):
        keys = []
        for i in dicty:
            keys.append(i)
        return keys[number - 1]

    # return list as string
    def lstToStr(listy, splitter = "", addNewLine = True):
        result = ""
        if type(listy) == dict:
            for i in listy:
                if i == Strings.indexOfDict(len(listy), listy):
                    result += i
                else:
                    result += i + splitter

        else:
            for i in range(len(listy)):
                if i == (len(listy) - 1):
                    result += str(listy[i])
                else:
                    result += str(listy[i]) + splitter
        if addNewLine:
            return result + "\n"
        return result

    def regex(string, find, replace):
        # modified code from here https://regex101.com/
        return re.sub(r"{}".format(find), r"{}".format(replace), string, 0, re.MULTILINE)






    # takes in 2 characters and gives you all the characters between them, it is inclusive
    def lets(start, end):
        i = ord(start)
        lets = []

        while i <= ord(end):
            lets.append(chr(i))
            i+=1
        return lets




    def countVowel(word):
        count = 0
        vLst = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in word:
            if i in vLst:
                count += 1
        return count


class Grid:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def create(x, y):
        board = []
        num = 0
        for i in range(y):
            tempList = []
            for j in range(x):
                num += 1
                tempList.append(f"   ")
            board.append(tempList)
        return board

    def build(grid):
        buildABoard = '  '

        for i in range(len(grid[0])):
            buildABoard += Strings.lets('A', 'Z')[i] + '   '
        buildABoard += '\n'

        buildABoard += "╔" + "═══╦" * (len(grid[0]) - 1) + "═══╗\n"
        for i in range(len(grid)):
            buildABoard += "║"
            for j in range(len(grid[i])):

                if not (j == len(grid[i]) - 1):
                    buildABoard += (str(grid[i][j]) + "║")
                else:
                    buildABoard += str(grid[i][j]) + f"║ {i+1}\n"
            
            if not (i == len(grid) - 1):
                buildABoard += ("╠" + "═══╬" * (len(grid[i]) - 1) + "═══╣\n")
        buildABoard += "╚" + "═══╩" * (len(grid[0]) - 1) + "═══╝"
        return buildABoard

