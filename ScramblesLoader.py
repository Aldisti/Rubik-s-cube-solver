# by Aldisti
# 640.1966454982758 seconds for 9000 scrambles
# 954.8817234039307 seconds for 13500 scrambles
# 1245.2768785953522 seconds for 18000 scrambles
# 1360.0848126411438 seconds for 18000 scrambles
# 2111.1964893341064 seconds for 27000 scrambles
# 2086.6672806739807 seconds for 27000 scrambles
# 1917.1332802772522 seconds for 27000 scrambles
# 2090.1329641342163 seconds for 27000 scrambles
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import time
from re import subn

OPTIONS = Options()
OPTIONS.add_argument('--kiosk-printing')
OPTIONS.add_argument('--incognito')
OPTIONS.add_argument('--disable-extensions')
OPTIONS.add_argument('--profile-directory=Default')
OPTIONS.add_argument("--disable-plugins-discovery")

def scramble(n):
    driver = webdriver.Chrome(executable_path = r"C:\Users\aless\OneDrive\Python\ProjectZ\chromedriver.exe", options = OPTIONS)
    wait = WebDriverWait(driver, 10)

    driver.get("https://ruwix.com/puzzle-scramble-generator/")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
    driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'scramblesvalue')))
    element = driver.find_element(By.ID, 'scramblesvalue')
    element.clear()
    element.send_keys("9")
    l = []
    for _ in range(int(n / 9)):
        wait.until(EC.element_to_be_clickable((By.ID, "scramblebutton")))
        driver.find_element(By.ID, "scramblebutton").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tobbscrmble"]/div[1]/div[3]')))
        container = list(driver.find_elements(By.XPATH, '//*[@id="tobbscrmble"]'))
        st = container[0].text.replace("\n", "&").replace(".", "")
        st = subn('[0-9]', '', st)[0].replace("&&", "$").replace("&", "").split("$")
        for s in st:
            moves = ""
            for i in range(len(s)):
                if (s[i] == "2"): moves += f" {s[i - 1]}"
                elif (s[i] == "'"): moves += "1"
                else: moves += s[i]
            moves += "\n"
            l.append(moves)
    try:
        with open(r"C:\Users\aless\OneDrive\Python\ProjectZ\scrambles.txt", "r") as file:
            lines = file.readlines()
        l += lines
        with open(r"C:\Users\aless\OneDrive\Python\ProjectZ\scrambles.txt", "w") as file:
            file.writelines(l)
    except FileNotFoundError:
        with open(r"C:\Users\aless\OneDrive\Python\ProjectZ\SWP.txt", "x") as file:
            file.writelines(l)
        print("""Rinomina il file "SWP.txt" in "scrambles.txt" altrimenti non sarai in grado di usare gli scramble generati""")
    driver.close()
t = time()
scramble(9)
print(time() - t)
