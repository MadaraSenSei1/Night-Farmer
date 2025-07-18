import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 🔁 Argumente vom Web-Formular
USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
MIN_INTERVAL = int(sys.argv[3])
MAX_INTERVAL = int(sys.argv[4])

# Funktion: Travian öffnen & einloggen
def start_bot():
    print("✅ Starte Travian Bot...")

    # Chrome starten
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://ts9.x1.europe.travian.com/")
    time.sleep(2)

    # Login
    driver.find_element(By.NAME, "name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("🔓 Eingeloggt...")

    time.sleep(3)

    while True:
        try:
            # Zum Rally-Point (gid=16)
            rally_point = driver.find_element(By.XPATH, "//a[contains(@href, 'gid=16')]")
            rally_point.click()
            print("📍 Rally Point geöffnet")
        except:
            print("❌ Rally Point nicht gefunden")
            break

        time.sleep(3)

        try:
            # Farm-Tab öffnen
            farm_tab = driver.find_element(By.XPATH, "//a[contains(@href, 'tt=99')]")
            farm_tab.click()
            print("🌾 Farm List geöffnet")
        except:
            print("❌ Farm-Tab nicht gefunden")
            break

        time.sleep(3)

        # Farm-Buttons finden und klicken
        send_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'green')]")
        print(f"➡️  {len(send_buttons)} Raids gefunden")

        for button in send_buttons:
            try:
                button.click()
                time.sleep(0.5)
            except:
                continue

        # Zufälliger Timer für nächste Runde
        interval = random.randint(MIN_INTERVAL * 60, MAX_INTERVAL * 60)
        print(f"⏱ Wartezeit bis zur nächsten Runde: {interval} Sekunden")
        time.sleep(interval)

# Bot starten
start_bot()
