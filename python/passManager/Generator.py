import random
from Password import Password


class Generator:

    def genPass(strength):

        while True:
            numCap = random.randint(0, 4)
            numLet = random.randint(0, 4)
            numSpecChar = random.randint(0, 4)
            numNums = random.randint(0, 4)

            password = ""
            specChars = "!@#$%^&()"
            pwNoRand = ""

            # assign random capitol letters based on how many are requested
            for i in range(numCap):
                pwNoRand += ( chr( random.randint(65, 90)))

            # assign random lowercase letters based on how many are requested
            for i in range(numLet):
                pwNoRand += ( str(chr( random.randint(65, 90) ) ).lower())

            # assign random digits based on how many are requested
            for i in range(numNums):
                pwNoRand += ( str( random.randint(0, 9)))

            # assign random special characters based on how many are requested
            for i in range(numSpecChar):
                pwNoRand += ( str( specChars[random.randint(0, len(specChars) - 1 )]))


            # randomize the order of string created above
            for i in range(len(pwNoRand)):
                num = random.randint(0, len(pwNoRand) - 1)
                password += pwNoRand[num]
                # https://stackoverflow.com/questions/14198497/remove-char-at-specific-index-python
                pwNoRand = pwNoRand[:num] + pwNoRand[num + 1:]
            
            passAttempt = Password(password)
            if passAttempt.check(strength):
                return passAttempt.getPass()
