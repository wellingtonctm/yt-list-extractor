import getpass
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    def __init__(self) -> None:
        self.logado = False
        self.driver = uc.Chrome(use_subprocess=True)

        print("Partiu!")

    def login(self, email, password):
        self.driver.get('https://accounts.google.com/ServiceLogin')
        print("Abri o accounts!")

        time.sleep(1)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, 'identifier'))).send_keys(f'{email}\n')

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, 'Passwd'))).send_keys(f'{password}\n')

        self.logado = True
        print("Loguei!")

    def code(self, playlist):
        self.driver.get(playlist)
        print("Abri a playlist!")

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a.sign-in-link'))).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'ytmusic-responsive-list-item-renderer')))

        title = self.driver.find_element(
            By.CSS_SELECTOR, 'ytmusic-detail-header-renderer yt-formatted-string.title').text
        elements = self.driver.find_elements(
            By.CSS_SELECTOR, 'ytmusic-responsive-list-item-renderer')
        
        links = []

        for element in elements:
            try:
                links.append(element.find_element(By.CSS_SELECTOR, 'a').get_property('href'))
            except:
                continue

        with open(f'{title}.txt', 'w') as lista:
            lista.write('\n'.join(links))

        print("Terminei!")


if __name__ == "__main__":
    sucesso = False
    tentativas = 0

    email = input("User: ")
    password = getpass.getpass()
    playlist = input("Playlist: ")

    driver = Main()

    while (not sucesso and tentativas < 5):
        try:
            if not driver.logado:
                driver.login(email, password)

            driver.code(playlist)
            sucesso = True
        except Exception as ex:
            print(ex)
            tentativas += 1
            continue

    driver.driver.close()
