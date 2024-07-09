import os
from random import randint
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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
    
    def scrapMessiasPage(self, link):
        self.browser.get(link)
        sleep(3)

        imagemTituloURL = self.browser.find_element(By.ID, 'ctl00_cphMain_rptImage_ctl00_imgProduto').get_attribute('src')
        imagemTitulo = imagemTituloURL.split('/')[-1]

        DownloadImage().download(imagemTituloURL, imagemTitulo)


        try: titulo = self.browser.find_element(By.CSS_SELECTOR, '[id*="labelTitulo"]').text
        except NoSuchElementException: titulo = 'Null'

        try: categoria = self.browser.find_element(By.CSS_SELECTOR, '[id*="labelCategoriaTitulo"]').text
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
            if not conservacaoMiolo: conservacaoMiolo = 'Null'
        except NoSuchElementException: conservacaoCapa = 'Null'

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

        try: curiosidades = self.browser.find_element(By.CSS_SELECTOR, '[id*="pnlCuriosidade"]').text.replace('Curiosidades: ', '').split('\n')
        except NoSuchElementException: curiosidades = 'Null'

        if 'vendido' in self.browser.find_element(By.CSS_SELECTOR, '[id*="divCardBuy"]').text: status = 'Vendido'
        else: status = 'À venda'

        print(f'Titulo: {titulo}')
        print(f'Categoria: {categoria}')
        print('Autor: ', autor)
        print('Editora: {}'.format(editora))
        print('Ano: ' + ano)
        print('Conservação Capa: ' + conservacaoCapa)
        print('Conservação Miolo: ' + conservacaoMiolo)
        print('ISBN: ' + isbn)
        print('Acabamento: ' + acabamento)
        print('Tradutor: ' + tradutor)
        print('Idioma: ' + idioma)
        print('Edição: ' + edicao)
        print('Número de Páginas: ' + numeroPaginas)
        print('Formato: ' + formato)
        print('Preço Base: ' + preco)
        print('Preço com Desconto: ' + precoDesconto)
        print('Status: ' + status)
        print('Imagem Titulo: ' + imagemTitulo)
        print(curiosidades)


Driver().scrapMessiasPage('https://sebodomessias.com.br/gibi/dc-comics/arlequina-volume-1-uma-estranha-no-ninho-1')