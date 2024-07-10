import os
import requests
import telepot
from bancodedados import BancoDeDados
from random import randint
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from tokens import *


class DownloadImage():
    import urllib.request

    def __init__(self):
        self.path = os.getcwd() + '/images'
        if not os.path.exists(self.path): os.mkdir(self.path)

    def download(self, url, nome):
        self.urllib.request.urlretrieve(url, self.path + '/' + url.split('/')[-1])


class Driver():
    def __init__(self):
        if os.name == 'nt': self.browser = webdriver.Chrome()
    
    def scrapMessiasPage(self, links):
        bot = telepot.Bot(TELEGRAM_TOKEN)

        for link in links:
            self.browser.get(link)
            print('Acessando: ', link)
            sleep(3)

            imagemTituloURL = self.browser.find_element(By.ID, 'ctl00_cphMain_rptImage_ctl00_imgProduto').get_attribute('src')
            imagemTitulo = imagemTituloURL.split('/')[-1]

            DownloadImage().download(imagemTituloURL, imagemTitulo)


            #try: titulo = self.browser.find_element(By.CSS_SELECTOR, '[id*="labelTitulo"]').text.strip()
            try: titulo = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblTitulo"]').text
            except NoSuchElementException: titulo = 'Null'

            distrito = 'HQ/Mangá'

            try: categoria = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblCategoriaTitulo"]').text
            except NoSuchElementException: categoria = 'Null'
            
            try:
                autor = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAutor"]').text
                if not autor: autor = 'Null'
            except NoSuchElementException: autor = 'Null'

            try:
                editora = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblEditora"]').text
                if not editora: editora = 'Null'
            except NoSuchElementException: editora = 'Null'
            
            try: 
                ano = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAno"]').text
                if not ano: ano = 'Null'
            except NoSuchElementException: ano = 'Null'

            try:
                conservacaoCapa = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblCapa"]').text
                if not conservacaoCapa: conservacaoCapa = 'Null'
            except NoSuchElementException: conservacaoCapa = 'Null'

            try:
                conservacaoMiolo = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblMiolo"]').text
                if not conservacaoMiolo:
                    conservacaoMiolo = 'Null'
            except NoSuchElementException: conservacaoMiolo = 'Null'

            try:
                isbn = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblISBN"]').text
                if not isbn: isbn = 'Null'
            except NoSuchElementException: isbn = 'Null'

            try:
                acabamento = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblAcabamento"]').text
                if not acabamento: acabamento = 'Null'
            except NoSuchElementException: acabamento = 'Null'

            try:
                tradutor = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblTradutor"]').text
                if not tradutor: tradutor = 'Null'
            except NoSuchElementException: tradutor = 'Null'       
            
            try:
                idioma = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblIdioma"]').text
                if not idioma: idioma = 'Null'
            except NoSuchElementException: idioma = 'Null'

            try:
                edicao = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblEdicao"]').text
                if not edicao: edicao = 'Null'
            except NoSuchElementException: edicao = 'Null'

            try:
                numeroPaginas = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblNroPaginas"]').text
                if not numeroPaginas: numeroPaginas = 'Null'
            except NoSuchElementException: numeroPaginas = 'Null'

            try:
                formato = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblFormato"]').text.replace(' ', '')
                if not formato: formato = 'Null'
            except NoSuchElementException: formato = 'Null'

            try:
                precoDesconto = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblPrecoDesconto"]').text
                if not precoDesconto: precoDesconto = 'Null'
            except NoSuchElementException: precoDesconto = 'Null'
            
            try: 
                precoNaoTratado = self.browser.find_element(By.CSS_SELECTOR, '[id*="lblPreco"]').text
                preco = ''
                for letra in precoNaoTratado:
                    if letra.isnumeric() or letra == ',': preco += letra
                preco = 'R$ ' + preco
            except NoSuchElementException: preco = 'Null'

            try:
                curiosidades = self.browser.find_element(By.CSS_SELECTOR, '[id*="pnlCuriosidade"]').text.replace('Curiosidades: ', '')
                if curiosidades == '':
                    curiosidades = 'Null'
            except NoSuchElementException: curiosidades = 'Null'

            if 'vendido' in self.browser.find_element(By.CSS_SELECTOR, '[id*="divCardBuy"]').text: status = 'Vendido'
            else: status = 'À venda'

            mensagem = (f'Titulo: {titulo}\nDistrito: {distrito}\nCategoria: {categoria}\nAutor: {autor}\nEditora: {editora}\nAno: {ano}\nConservação Capa: {conservacaoCapa}\nConservação Miolo: {conservacaoMiolo}\nISBN: {isbn}\nAcabamento: {acabamento}\nTradutor: {tradutor}\nIdioma: {idioma}\nEdição: {edicao}\nNúmero de Páginas: {numeroPaginas}\nFormato: {formato}\nPreço Base: {preco}\nPreço com Desconto: {precoDesconto}\nStatus: {status}\nImagem Titulo: {imagemTitulo}\ncuriosidades')
            print(mensagem)

            if 'dura' in acabamento.lower():
                bot.sendPhoto(CHAT_ID, photo=open(f'./images/{imagemTitulo}', 'rb'))
                mensagem = (f'Titulo: {titulo}\nURL: {link}\nDistrito: {distrito}\nCategoria: {categoria}\nAutor: {autor}\nEditora: {editora}\nAno: {ano}\nConservação Capa: {conservacaoCapa}\nConservação Miolo: {conservacaoMiolo}\nISBN: {isbn}\nAcabamento: {acabamento}\nTradutor: {tradutor}\nIdioma: {idioma}\nEdição: {edicao}\nNúmero de Páginas: {numeroPaginas}\nFormato: {formato}\nPreço Base: {preco}\nPreço com Desconto: {precoDesconto}\nStatus: {status}\nImagem Titulo: {imagemTitulo}\ncuriosidades')
                print(mensagem)
                bot.sendMessage(CHAT_ID, mensagem)

            BancoDeDados().inserir((link, titulo, distrito, categoria, autor, editora, ano, conservacaoCapa, conservacaoMiolo, isbn, acabamento, tradutor, idioma, edicao, numeroPaginas, formato, preco, precoDesconto, status, imagemTitulo, curiosidades))

    def getMessiasPages(self):
        contador = 0
        self.browser.get('https://sebodomessias.com.br/gibis')

        while True:
            sleep(1)
            hqs = self.browser.find_elements(By.CLASS_NAME, 'card-news')
            for hq in hqs:
                nome = hq.find_element(By.CLASS_NAME, 'product-title').text
                contadorLetras = 0
                for letra in nome:
                    if '°' == letra or 'º' == letra: contador += 1
                
                if not contadorLetras == 1: 
                    link = hq.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    with open('links.txt', 'a') as file:
                        file.write(link + '\n')
                        print(link)
                        file.close()

            if self.browser.find_elements(By.CLASS_NAME, 'page-link')[-1].text.lower() == 'next' or self.browser.find_elements(By.CLASS_NAME, 'page-link')[-1].text == '...':
                self.browser.find_elements(By.CLASS_NAME, 'page-link')[-1].click()
                contador += 1
                print(contador)



# Driver().scrapMessiasPage(['https://sebodomessias.com.br/gibi/dc-comics/watchmen-em-ingles-4'])
with open('./links.txt', 'r') as file:
    linhas = file.readlines()
    Driver().scrapMessiasPage(linhas)
# Driver().getMessiasPages()