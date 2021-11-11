import os
from getpass import getpass
from pathlib import Path

import useful
from EncryptDecrypt import CryptoGraphy
from Generator import Generator
from Password import Password

# https://stackoverflow.com/questions/5214578/print-string-to-text-file
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
useful.Terminal.clear()

actions = {
    "add" : "PasswordManager.addPass()",
    "edit" : "PasswordManager.edit()",
    "remove" : "PasswordManager.remove()",
    "list" : "PasswordManager.listPass()",
    "close" : "PasswordManager.close()",
    "delete profile" : "PasswordManager.delete()"
} 
rBrkt = "{"
lBrkt = "}"



pathToDir = Path(__file__).parent.absolute().__str__() + "\\$70ra93"

if not Path(pathToDir).is_dir():
    os.mkdir(Path(pathToDir))

passFilePath = Path(f"{pathToDir}\\passwordFile.store")
pathToLoginFile = Path(f"{pathToDir}\\login.encrypted")
class PasswordManager:
    namePass = ''
    mstrPWStor = {}
    storeContents = ""
    def login():

        

        # if the login file doesn't exist, have the user create an account
        if not pathToLoginFile.is_file():
            firstName = input("What is your first name? ")
            lastName = input("What is your last name? ")
            loginUser = input('What do you want your username to be? ')
            loginPass = Password( getpass('What do you want as your password? ') )

            # loops until the user puts in a max strength password, a strength of 5
            while True:
                if loginPass.check(5):
                    PasswordManager.namePass = f"{rBrkt}'First name' : '{firstName}', 'Last name' : '{lastName}', 'UserName' : '{loginUser}', 'Password' : '{loginPass.txt}'{lBrkt}"
                    
                    # generate a key based on the namePass string, then encrypt namePass with that key, that key is also the global encryption key
                    CryptoGraphy.genKey(PasswordManager.namePass, pathToDir)
                    CryptoGraphy.encrypt(PasswordManager.namePass, f"{pathToDir}", f"{pathToLoginFile}")
                    break
                # set the txt value of loginPass to the ui
                loginPass.set( getpass('That password is not very secure, try a different one: ') )

        # if the login file exists
        if pathToLoginFile.is_file():
            PasswordManager.namePass = CryptoGraphy.decrypt(pathToLoginFile, pathToDir)
            # namePass is decrypted into a string, so eval it to turn it into the dictionary it is
            PasswordManager.namePass = eval(PasswordManager.namePass)
            username = PasswordManager.namePass["UserName"]
            password = PasswordManager.namePass["Password"]
            
            fails = 0
            while True:
                useful.Terminal.clear()
                print(f"Attempts: {fails}")
                if fails == 3:
                    useful.Terminal.clear()
                    print("You have reached the maximum number of attempts.")
                    if input("Have you forgoten your login info? (y/n) ") == 'y':
                        PasswordManager.forgotPass()
                        return
                    else:
                        quit()
                fails += 1
                if useful.Terminal.inputChecker(input("What's your username? "), username) and useful.Terminal.inputChecker(getpass("What's your password? "), password):
                    break
            PasswordManager.openApp()





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def openApp(newKey = ''):
        while True:    
            if passFilePath.is_file():
                file = open(f"{passFilePath}", 'r')
                PasswordManager.storeContents = file.read()
                file.close()
                if PasswordManager.storeContents != "":
                    PasswordManager.storeContents = CryptoGraphy.decrypt(passFilePath, pathToDir)
                break
            else:
                open(f"{passFilePath}", 'wb').close()
        if newKey != '':
            CryptoGraphy.genKey(newKey, pathToDir)
            CryptoGraphy.encrypt(newKey, f"{pathToDir}", f"{pathToLoginFile}")
            
        useful.Terminal.clear()
        # set the global dict of all passwords to the dict from the decrypted file
        if PasswordManager.storeContents == "":
            PasswordManager.mstrPWStor = {}
        else:
            PasswordManager.mstrPWStor = eval(PasswordManager.storeContents)
    
        PasswordManager.save()
        
        while True:
            
            userChoice = input(f"What do you want to do; {useful.Strings.lstToStr(actions, ', ', False)}? ")
            if userChoice in actions:
                eval(actions[userChoice])
            PasswordManager.save()
            PasswordManager.listPass()
            
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def forgotPass():
        first = input("What is your first name? ")
        last = input("What is your last name? ")
        if first == PasswordManager.namePass['First name'] and last == PasswordManager.namePass['Last name']:
            username = input("What is your new username? ")
            newPass = Password( getpass( "What do you want as your new password? "))
            while not newPass.check(5):
                newPass.set( getpass( "That password is not very secure, try again. "))
            newKey = f"{rBrkt}'First name' : '{first}', 'Last name' : '{last}', 'UserName' : '{username}', 'Password' : '{newPass.txt}'{lBrkt}"
            PasswordManager.openApp(newKey)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def addPass():
        useful.Terminal.clear()
        # ask the user what catagory the password is in, and where the password is used
        if PasswordManager.mstrPWStor.keys().__str__() == "dict_keys([])":
            catagory = input("What do you want to call your first catagory, type back to return to the home page ")
            if catagory == 'back':
                return
            passFor = input("Where is this password going to be used, type back to return to the home page ")
            if passFor == 'back':
                return
        else:
            while True:
                catagory = input(f"What category is this password; {useful.Strings.lstToStr(PasswordManager.mstrPWStor, ', ', False)}, or enter a new name to create a new catagory, type back to return to the home page ")
                if catagory == 'back':
                    return
                passFor = input("Where is this password going to be used, type back to return to the home page ")
                if passFor == 'back':
                    return
                break

        # ask the user what the password is, or generate one for them
        ui = input("Type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong, type back to return to the home page ")
        useful.Terminal.clear()
        if ui  == 'back':
            return
        if ui.isdigit():
            if 3 <= int(ui) + 2 <= 5:
                if not catagory in PasswordManager.mstrPWStor:
                    PasswordManager.mstrPWStor[catagory] = {}
                randPass = Password( Generator.genPass(int(ui) + 2) )
                PasswordManager.mstrPWStor[catagory][passFor] = randPass.getPass()
                
        else:
            passTemp = Password(ui)
            if not catagory in PasswordManager.mstrPWStor:
                PasswordManager.mstrPWStor[catagory] = {}
            PasswordManager.mstrPWStor[catagory][passFor] = pa
            ssTemp.getPass()
            useful.Terminal.clear()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

    def edit():
        useful.Terminal.clear()
        # ask the user what catagory the password is in
        PasswordManager.listPass()
        cat = input(f"What category is the password in, type back to return to the home page ")
        while not cat in PasswordManager.mstrPWStor:
            if cat == 'back':
                return
            useful.Terminal.clear()
            PasswordManager.listPass()
            cat = input("That's not a category, try again, type back to return to the home page ")
        
        # ask the user where the password gets used
        useful.Terminal.clear()
        PasswordManager.listPass()
        place = input("What is the password to, type back to return to the home page ")
        while not place in PasswordManager.mstrPWStor[cat]:
            if place == 'back':
                return
            useful.Terminal.clear()
            PasswordManager.listPass()
            place = input("That place isn't in the records, try again, type back to return to the home page ")
        
        useful.Terminal.clear()
        
        # ask the user what they want the new password to be, or generate one for them
        ui = input("Type a password, or put a number 1 to 3 for a password with that strength to be generated, 1 being super weak, 3 being super strong, type back to return to the home page ")

        if ui  == 'back':
            return
        useful.Terminal.clear()
        if ui.isdigit():
            if 3 <= int(ui) + 2 <= 5:
                if not cat in PasswordManager.mstrPWStor:
                    PasswordManager.mstrPWStor[cat] = {}
                randPass = Password( Generator.genPass(int(ui) + 2) )
                PasswordManager.mstrPWStor[cat][place] = randPass.getPass()
        else:
            passTemp = Password(ui)
            if passTemp.check():
                if not cat in PasswordManager.mstrPWStor:
                    PasswordManager.mstrPWStor[cat] = {}
                PasswordManager.mstrPWStor[cat][place] = passTemp.getPass()
            
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove():
        useful.Terminal.clear()
        # ask the user what catagory the password is in
        PasswordManager.listPass()
        cat = input(f"What category is the password in, if the category is empty, it will be deleted, type back to return to the home page ")
        while not cat in PasswordManager.mstrPWStor:
            if cat == 'back':
                return
            useful.Terminal.clear()
            PasswordManager.listPass()
            cat = input("That's not a category, try again, if the category is empty, it will be deleted, type back to return to the home page ")
        

        if PasswordManager.mstrPWStor[cat] == {}:
            PasswordManager.mstrPWStor.pop(cat)
        
        else:

            # ask the user where the password gets used
            useful.Terminal.clear()
            PasswordManager.listPass()
            place = input("What is the password to, type back to return to the home page ")
            while not place in PasswordManager.mstrPWStor[cat]:
                if place == 'back':
                    return
                useful.Terminal.clear()
                PasswordManager.listPass()
                place = input("That place isn't in the records, try again, type back to return to the home page ")
            PasswordManager.mstrPWStor[cat].pop(place)
        
        if PasswordManager.mstrPWStor[cat] == {}:
            PasswordManager.mstrPWStor.pop(cat)
        useful.Terminal.clear()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # formats as a string all the passwords from the global dict, so the can be printed
    def listPass():
        result = ""
        for i in PasswordManager.mstrPWStor:
            result += f'\n{i}'
            for j in PasswordManager.mstrPWStor[i]:
                result += f'\n    {j} : {PasswordManager.mstrPWStor[i][j]}'
        useful.Terminal.clear()
        if result != '':
            print(result)
        

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def delete():
        if input(f"Are you sure you want to delete your profile, {useful.Terminal.Color.RED}WARING: THIS WILL PERMANANTLY DELETE ALL SAVED PASSWORDS, THERE IS NO GOING BACK!!!!!!!!{useful.Terminal.Color.END}, type yes to confirm ") == "yes":
            os.remove(pathToLoginFile)
            os.remove(passFilePath)
            os.remove(Path(f"{pathToDir}\\key.key"))
            os.removedirs(Path( pathToDir ))
            quit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def close():
        PasswordManager.save()
        quit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def save():
        CryptoGraphy.encrypt(f"{PasswordManager.mstrPWStor}", pathToDir, passFilePath)

PasswordManager.login()
