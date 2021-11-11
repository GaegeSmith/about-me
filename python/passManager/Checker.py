import useful


class Checker:
    # #reqCheckList = [length, allCharsAreAllowed, hasSpecChar, hasNum, hasLowerLet, hasCapLet] 
    reqCheckList = [   False,  False,              False,       False,  False,       False]

    scoreList = []
    passList = []

    allowedChars = []
    specChars = ["!", "@", "#", "$", "%", "^", "&", "(", ")"]

    # below for loops append all acceptable characters into one list
    for i in range(0, 10):
        allowedChars.append(str(i))

    for i in specChars:
        allowedChars.append(str(i))

    for i in useful.Strings.lets("a", "z"):
        allowedChars.append(str(i))

    for i in useful.Strings.lets("A", "Z"):
        allowedChars.append(str(i))

    def passChecker(inputPassword):
        
        password = [inputPassword].copy()[0]
        #                    specChars  digits  lowers  Uppers
        hasBeenScoredList = [False,     False,  False,  False]
        # if the password is within the length guidlines
        if (len(password) <= 16 and len(password) >= 6):
            # check that requirment off the list
            Checker.reqCheckList[0] = True

            # below for loop checks to make sure all the characters are acceptable characters, if there is an unacceptable character, it outputs "character not allowed" + char
            for i in password:
                for j in Checker.allowedChars:
                    # when it does match, move to the next character in password
                    if j == i:
                        Checker.reqCheckList[1] = True
                        score = 1
                        break
                    else:
                        score = "character not allowed: " + i

                if (score == "character not allowed: " + i):
                    return score


            # if all chars are allowed, start checking all requirements
            for i in password:
                # check if the current char of password is in specChars
                if i in Checker.specChars:

                    if not hasBeenScoredList[0]:
                        score += 1
                        hasBeenScoredList[0] = True
                    
                    Checker.reqCheckList[2] = True

                # check if the current char of password is 0 thru 9
                elif i in useful.Strings.lets("0", chr( ord("9") )):

                    if not hasBeenScoredList[1]:
                        score += 1
                        hasBeenScoredList[1] = True

                    Checker.reqCheckList[3] = True

                # check if the current char of password is a lowercase letter
                elif i in useful.Strings.lets("a", "z"):

                    if not hasBeenScoredList[2]:
                        score += 1
                        hasBeenScoredList[2] = True

                    Checker.reqCheckList[4] = True

                # check if the current char of password is a capitol letter
                elif i in useful.Strings.lets("A", "Z"):

                    if not hasBeenScoredList[3]:
                        score += 1
                        hasBeenScoredList[3] = True

                    Checker.reqCheckList[5] = True

            # return strength
            return score
        return "Password length invalid"
    


    
