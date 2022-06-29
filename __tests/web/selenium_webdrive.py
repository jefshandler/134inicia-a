# configura //
# bibliotecas / import

# dados de entrada
import time

import pytest
from selenium import webdriver
# from selenium.common.exceptions import *
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.opera.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.drivers.chrome import ChromeDriver

# origem = 'São Paolo'
# destino = 'New York'
# primeiro_nome = 'Juca'
# bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# Executa
class Testes:

    # Início
    # def setup_method(self):

        # instanciar a biblioteca / motor / engine
        # informar onde esta o WebDriver

        # chrome_options = Options()
        # chrome_options.add_argument('--lang=pt-BR')
        # chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--mute-audio")
        # self.driver = webdriver.Chrome('F:\\projetoPython\\134inicial-a\\vendors\\chromedriver\\chromedriver102.exe', options=chrome_options)
        # # self.driver.implicitly_wait(3)
        # self.wait = WebDriverWait(
        #     driver=self.driver,
        #     timeout=10,
        #     poll_frequency=1,
        #     ignored_exceptions=[
        #         NoSuchElementException,
        #         ElementNotVisibleException,
        #         ElementNotSelectableException
        #     ]
        # )

    # Fim
    def teardown_method(self):

        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    lista_de_valores = [
        ('São Paolo', 'New York', 'Juca', 'American Express', 'fire'),
        ('Paris', 'Buenos Aires', 'Noah', 'Visa', 'chrome'),
        ('Paris', 'Buenos Aires', 'Helia', 'Visa', 'chrome'),
        ('Paris', 'Buenos Aires', 'Jeferson', 'American Express', 'fire'),
    ]

    # primeiro_nome = 'Juca'
    # bandeira = 'American Express'
    # lembrar_de_mim = True
    @pytest.mark.parametrize('origem,destino,primeiro_nome,bandeira,browser', lista_de_valores)
    def testar_comprar_passagem(self, origem, destino, primeiro_nome, bandeira, browser):

        # e2e / end to end / ponta a ponta
        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereço

        # navegadores
        match browser:
            case 'chrome':

                chrome_options = Options()
                chrome_options.add_argument('--lang=pt-BR')
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_argument("--mute-audio")
                self.driver = webdriver.Chrome('F:\\projetoPython\\134inicial-a\\vendors\\chromedriver\\chromedriver102.exe',
                                               options=chrome_options)
            case 'fire':
                self.driver = webdriver.Firefox(executable_path='F:\\projetoPython\\134inicial-a\\vendors\\chromedriver\\geckodriver.exe')


        self.driver.get('https://www.blazedemo.com')
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Welcome to the Simple Travel Agency!"
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        # selecionar cidade de origen
        lista.find_element(By.XPATH, f'//option[ .= "{origem}" ]').click()
        # clicar na lista de cidade de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        # selecionar cidade de origen
        lista.find_element(By.XPATH, f'//option[ .= "{destino}" ]').click()

        # cliar no botao procurar voos
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == f"Flights from {origem} to {destino}:"
        time.sleep(3)
        # Pagina Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == f'Flights from {origem} to {destino}:'

        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(6)").text == "Price"
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()


        # for preco in precos:
        #     print(preco.text)

        # Pagina de Compra

        # Executa / Valida
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Your flight from TLV to SFO has been reserved."
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys(f"{primeiro_nome}")
        self.driver.find_element(By.ID, "address").click()
        self.driver.find_element(By.ID, "address").send_keys("rua")
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("goiania")
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.ID, "state").send_keys("go")
        self.driver.find_element(By.ID, "zipCode").click()
        self.driver.find_element(By.ID, "zipCode").send_keys("12345")
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.XPATH, f"//option[. = '{bandeira}']").click()
        self.driver.find_element(By.ID, "creditCardNumber").click()
        self.driver.find_element(By.ID, "creditCardNumber").send_keys("2222222222221111")
        self.driver.find_element(By.ID, "creditCardMonth").click()
        self.driver.find_element(By.ID, "creditCardMonth").clear()
        self.driver.find_element(By.ID, "creditCardMonth").send_keys("12")
        self.driver.find_element(By.ID, "creditCardYear").click()
        self.driver.find_element(By.ID, "creditCardYear").clear()
        self.driver.find_element(By.ID, "creditCardYear").send_keys("30")
        self.driver.find_element(By.ID, "nameOnCard").click()
        self.driver.find_element(By.ID, "nameOnCard").send_keys("teseeeee")
        self.driver.find_element(By.ID, "rememberMe").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        # Pagina de Obrigado
        # Executa

        # Valida
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == mensagem_agradecimento_esperada



