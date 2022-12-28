import os
import sys
import random
import string
from colorama import Fore,Style

clear = lambda: os.system("cls")
def title(text):
    os.system(f"title {text}")

banner = f"""
  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE} {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE} {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}  {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE} {Fore.CYAN}Retro{Fore.WHITE}#{Fore.YELLOW}7893{Fore.WHITE}\t  
                                    ██████╗ ███████╗████████╗██████╗  ██████╗ 
                                    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
                                    ██████╔╝█████╗     ██║   ██████╔╝██║   ██║
                                    ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║
                                    ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝
                                    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
"""

class RedeemLicenses:
    def genstring(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    def Redeem(licensetoredeem):
        if os.path.exists("Licenses.txt"):
            with open("Licenses.txt", "r") as f:
                contents2 = f.read()
                if licensetoredeem in contents2:
                    contents = contents2.replace(licensetoredeem, "")
                    with open("Licenses.txt", "w") as f:
                        f.write(contents)
                    if os.path.exists("Users.txt"):
                        if os.path.getsize("Users.txt") == 0:
                            with open("Users.txt", "a") as f:
                                randomcredentialsgen = RedeemLicenses.genstring(5)
                                randomcredentials = randomcredentialsgen + ":" + randomcredentialsgen
                                f.write(randomcredentials)
                                f.close()
                                print("License redeemed! Username&Password: {}".format(randomcredentials))
                        else:
                                with open("Users.txt", "a") as f:
                                    randomcredentialsgen = RedeemLicenses.genstring(5)
                                    randomcredentials = "," + randomcredentialsgen + ":" + randomcredentialsgen
                                    f.write(randomcredentials)
                                    f.close()
                                    print("License redeemed! Username&Password: {}".format(randomcredentials))

                else:
                    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED}:{Fore.WHITE} License not found!")
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED}:{Fore.WHITE} Couldnt find Licenses file!")


class ManageUsers:
    def deleteuser(usertodel):
        if os.path.exists("Users.txt"):
            with open("Users.txt", "r") as f:
                try:
                    with open("Users.txt", "r") as f:
                        contents = f.read()
                    modified_contents = contents
                    while usertodel in modified_contents:
                        modified_contents = modified_contents.replace(usertodel, "")
                    with open("Users.txt", "w") as f:
                        f.write(modified_contents)
                    print(f"User {Fore.CYAN}({usertodel}){Fore.WHITE} has been deleted!")
                except:
                    pass
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED}:{Fore.WHITE} Couldnt find users file!")
class ManageLicense:
    def deletelicense(licensetodel):
        if os.path.exists("Licenses.txt"):
            with open("Licenses.txt", "r") as f:
                try:
                    with open("Licenses.txt", "r") as f:
                        contents = f.read()
                    modified_contents = contents
                    while licensetodel in modified_contents:
                        modified_contents = modified_contents.replace(licensetodel, "")
                    with open("Licenses.txt", "w") as f:
                        f.write(modified_contents)
                    print(f"License {Fore.CYAN}({licensetodel}){Fore.WHITE} has been deleted!")
                except:
                    pass
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED}:{Fore.WHITE} Couldnt find licenses file!")
class GenLicense:
    def genstring(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    def genlicense():
        rand1 = GenLicense.genstring(5)
        rand2 = GenLicense.genstring(5)
        license = f"LICESE-{rand1}-{rand2}"
        if os.path.exists("Licenses.txt"):
            if os.path.getsize("Licenses.txt") == 0:
                with open("Licenses.txt", "a") as f:
                    f.write(license)
                    f.close()
            else:
                with open("Licenses.txt", "a") as f:
                    f.write(f":{license}")
                    f.close()
        else:
            with open("Licenses.txt", "a") as f:
                f.write(license)
                f.close()
        print(f"\t\t\t\t\t{Fore.WHITE}Your license key is{Fore.CYAN}:{Fore.WHITE} {license}")
class MainApp:
    def Main():
        title("Kwstas (aka Retro) free License Generator and Redeem! - .gg/unban")
        clear()
        print(f"{Fore.CYAN}" + banner + f"{Fore.WHITE}")
        print(r'')
        print(f"\t\t\t\t\t   {Fore.WHITE}[{Fore.CYAN}1{Fore.WHITE}]{Fore.CYAN}:{Fore.WHITE} Generate License Key")
        print(r'')
        print(f"\t\t\t\t\t   {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}]{Fore.CYAN}:{Fore.WHITE} Redeem License Key")
        print(r'')
        print(f"\t\t\t\t\t   {Fore.WHITE}[{Fore.CYAN}3{Fore.WHITE}]{Fore.CYAN}:{Fore.WHITE} Delete License Key")
        print(r'')
        print(f"\t\t\t\t\t   {Fore.WHITE}[{Fore.CYAN}4{Fore.WHITE}]{Fore.CYAN}:{Fore.WHITE} Delete User")
        print(r'')
        print(r'')
        selection = input(f"{Fore.WHITE}[{Fore.YELLOW}.{Fore.WHITE}]{Fore.YELLOW}:{Fore.WHITE} > {Fore.CYAN}")
        if selection == "1":
            GenLicense.genlicense()
        elif selection == "2":
            licensetoredeem = input("Please enter the license that you want to redeem: ")
            RedeemLicenses.Redeem(licensetoredeem)
        elif selection == "3":
            licensetodel = input("Please enter the license that you want to delete: ")
            ManageLicense.deletelicense(licensetodel)
        elif selection == "4":
            usertodel = input("Please enter the user that you want to delete: ")
            ManageLicense.deletelicense(licensetodel)
        else:
            print("Invalid Option! Redirecting back..")
            time.sleep(3)
            MainApp.Main()

MainApp.Main()
