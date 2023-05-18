from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import sqlite3
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://dejt.jt.jus.br/dejt/f/n/diariocon')
navegador.find_element('xpath' , '//*[@id="diarioArg"]/fieldset/table/tbody/tr/td[1]/table/tbody/tr/td[1]/span/button/span').click()
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="diarioArg"]/fieldset/table/tbody/tr/td[2]/table/tbody/tr/td[1]/span/button/span')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="corpo:formulario:botaoAcaoPesquisar"]/table/tbody/tr/td[2]/div')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="corpo:formulario:tipoCaderno"]').click()
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="corpo:formulario:tribunal"]')
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="diarioCon"]/fieldset/table/tbody/tr[2]/td[3]/button/img').click()
time.sleep(10)
navegador.find_element('xpath' , '//*[@id="diarioCon"]/fieldset/table/tbody/tr[3]/td[3]/button/img').click()
time.sleep(10)







