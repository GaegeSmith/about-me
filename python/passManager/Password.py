from Checker import Checker
class Password:

    def __init__(self, password):
        self.txt = password

    # Get the strength of the password 
    def getScore(self):
        return Checker.passChecker(self.txt)


    # return the password as a string 
    def __str__(self):
        return "score: " + str(self.getScore()) + " password: " + self.txt

    def getPass(self):
        return self.txt
    # set the txt to a new value 
    def set(self, newPass):
        self.txt = newPass

    # is the password valid, does the password have a strength greater than the one inputed, or the default of 2
    # strength of 2 means it is a valid password length
    # getScore is the strength value
    def check(self, strength = 2):
        if  type(self.getScore()) != str and self.getScore() == strength:
            return True
        return False

