
print()
print("###################################################")
print("###################################################")
print("Python script to remove your InSis notification")
print("This script runs only localy and none of your credentials are stored in any way")
print()
print("Author: Šimon Charvát")
print("Version: 1.3 - 2024-05-07")
print("###################################################")
print("###################################################")
print()


try:
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from pwinput import pwinput
except Exception as e:
    print()
    print("###################################################")
    print("##################   ERROR   ######################")
    print("###################################################")
    print("Unable to import required packages.\nPlease make sure that all packages listed bellow are installed properly:")
    print("selenium")
    print("webdriver_manager")
    print("pwinput")
    print("\nTo install package, use the command bellow in your command line (CMD) [for Windows users]")
    print("py -m pip install package_name")
    print()
    print("Error message:")
    print(e)
    print()
    input("\nPress enter to exit")
    quit()


print("-------------------------")

cred = {"user":"",
        "pass":""}

if cred["user"] == "":
    cred["user"] = input("Enter your Xname: ")
    

if cred["pass"] == "":
    cred["pass"] = pwinput(mask = "*", prompt = "Enter your password: ")


print("\nWait please...\nOpening web browser (Google Chrome)...")
print("New update is downloaded automatically if required")
try:
    #dr = webdriver.Chrome(ChromeDriverManager().install())
    dr = webdriver.Chrome()
except Exception as e:
    print()
    print("###################################################")
    print("##################   ERROR   ######################")
    print("###################################################")
    print("Unable to load or install Chrome web driver\nPlease install or update following packages:")
    print("webdriver-manager")
    print("packaging")
    print()
    print("You can use following command in your command line:")
    print("pip install package_name")
    print("or")
    print("pip install package_name --upgrade")
    print()
    print("Error message:")
    print(e)
    print()
    input("\nPress enter to exit")
    quit()

dr.get("https://insis.vse.cz/auth/")

sleep(1.5)



dr.find_element(By.ID, "credential_0").send_keys(cred["user"])
dr.find_element(By.ID, "credential_1").send_keys(cred["pass"])
sleep(0.1)

dr.find_element(By.ID, "login-btn").click()

while True: # repeat until correct 2FA entered correctly
    sleep(0.1)
    try:
        FA_input_field = dr.find_element(By.ID, "overovaci_kod")
    except:
        break

    print("Two-factor authorization required")
    FA_code = input("Enter 2FA code:")
    FA_code = FA_code[0:3] + " " + FA_code[3:] # add whitespace into the code
    FA_input_field.send_keys(FA_code)
    sleep(0.1)
    dr.find_element(By.ID, "login-btn").click()

notifications = []

def get_notifications():
    print()
    global notifications
    notifications = []
    #notifications = dr.find_elements(By.XPATH, "//a[text()='Announce an exam date of course']") + dr.find_elements(By.XPATH, "//a[text()='Change in exam date']") + dr.find_elements(By.XPATH, "//a[text()='Cancel the exam date in course']")
    #notifications = dr.find_elements(By.XPATH, "//a[text()='Announce an exam date of course']")
    
    phrases = ["Announce an exam date of course", "Change in exam date", "Cancel the exam date in course", "Vypsání termínu předmětu", "Změna v termínu předmětu", "Zrušení termínu předmětu", "Uvolnění místa na termínu předmětu", "An exam date place in course has become free", "Zaplnění místa na termínu předmětu", "An exam date place in course has been taken", "Změna v&nbsp; termínu předmětu", "Mobilní aplikace Moje studium. Prostě. Studuj. Kdekoli."]
    for i in range(3):
        if i == 0:
            print(f"Waiting for website to load...")
        sleep(1)
    
    for string in phrases:
        
        notifications_part = dr.find_elements(By.XPATH, f"//a[text()='{string}']")
        print(f"Found {len(notifications_part)} elements with following text: {string}")
        
        notifications.extend(notifications_part)

    #notifications = dr.find_elements(By.XPATH, f"//a[text()={phrases}]")
    print(f"Notifications left: {len(notifications)}")

get_notifications()

while(len(notifications) > 0):
    print()
    print("--------------------------------")
    print("Notification soon to be closed:")
    
    notifications[0].click()
    
    sleep(0.1)

    try:
        dr.find_element(By.XPATH, "//b[text()='Do not display this information']").click()
    except: pass
    
    try:
        dr.find_element(By.XPATH, "//b[text()='Již nezobrazovat tuto informaci']").click()
    except: pass

    get_notifications()

print()
print("###################################################")
print("Finished!")
print("No more notifications!")
print("###################################################")
print()
input("\n###################################################\nPress enter to exit (or close the console window and browser)\n###################################################\n")


print()
print("Closing browser")
dr.quit()
sleep(0.5)
print("Script finished!")
sleep(0.5)