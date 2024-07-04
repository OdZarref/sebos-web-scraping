import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Main:
    class Driver():
        def __init__(self):
            if os.name == 'nt': self.browser = webdriver.Chrome()

        def seboMessias(self):
            self.browser.get('https://sebodomessias.com.br/gibi/dc-comics/watchmen-edicao-definitiva-16')
            self.scrapMessias()
        
        def scrapMessias(self):
            titulo = self.browser.find_element(By.CSS_SELECTOR, '[id*="labelTitulo"]').text
            autor = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAutor"]').text
            editora = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblEditora"]').text
            ano = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAno"]').text
            conservacaoCapa = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblCapa"]').text
            conservacaoMiolo = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblMiolo"]').text
            isbn = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblISBN"]').text
            acabamento = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAcabamento"]').text
            tradutor = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblTradutor"]').text
            idioma = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblIdioma"]').text
            edicao = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblEdicao"]').text
            numeroPaginas = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblNroPaginas"]').text
            formato = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblFormato"]').text
            print(titulo)
            print(autor)
            print(editora)
            print(ano)
            print(conservacaoCapa)
            print(conservacaoMiolo)
            print(isbn)
            print(acabamento)
            print(tradutor)
            print(idioma)
            print(edicao)
            print(numeroPaginas)
            print(formato)


    def __init__(self):
        pass

Main().Driver().seboMessias()