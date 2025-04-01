import os
import requests
import telepot
import sqlite3
import schedule
import asyncio
from sys                            import argv
from datetime                       import datetime
from bancodedados                   import *
from random                         import randint
from time                           import sleep
from selenium                       import webdriver
from selenium.webdriver.common.by   import By
from tokens                         import *
from urllib.error import URLError
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    WebDriverException
)


class UtilsFunctions:
    def getStrTime() -> str:
        return datetime.now().isoformat()[0:-13]

    def randintID() -> str:
        return str(randint(10 ** 8, 10 ** 9))


class TelegramBot:
    def __init__(self) -> None:
        self.bot = telepot.Bot(TELEGRAM_TOKEN)


    def sendMessage(self, mensagem) -> None:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensagem}"
        print(requests.get(url))
        

    def sendPhoto(self, imagemLocal) -> None:
        photo = open(f'./images/{imagemLocal}', 'rb')
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={CHAT_ID}"
        print(requests.post(url, files={'photo': photo}))


class DownloadImage():
    import urllib.request

    def download(self, url, path=''):
        if url:
            while True:
                try:
                    if 'guiadosquadrinhos' in url:
                            nomeNaoTratado = url.split('=')[-1].replace('/', '')
                            nome = ''

                            for letra in nomeNaoTratado:
                                if letra.isalnum() or letra == '.': nome += letra

                            path = os.getcwd() + '/capas_guia_dos_quadrinhos'
                            if not os.path.exists(path): os.mkdir(path)

                    elif 'messias' in url:
                        nome = url.split('/')[-1]
                        path = os.getcwd() + '/images'
                        if not os.path.exists(path): os.mkdir(path)
                    else: nome = str(randint(10**8, 10**9-1)) + '.jpg'
                    self.urllib.request.urlretrieve(url, path + '/' + nome )

                    break
                except URLError: pass
                except RemoteDisconnected: pass


class Driver():
    def __init__(self):
        pass
    
    def initDriver(self):
        if os.name == 'nt': self.browser = webdriver.Firefox()
        else:
            if self.headless:
                options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                self.browser = webdriver.Firefox(options)
            else: self.browser = webdriver.Firefox()

    def accessMessiasPages(self) -> None:
        db = BancoDeDadosMessias()
        columns = db.cur.execute('SELECT link, checado FROM sebo_messias').fetchall()

        for column in columns:
            if column[1] == '0': self.scrapMessiasPage(column[0])

        self.browser.quit()

    def scrapMessiasPage(self, link):
        db = BancoDeDadosMessias()
        district = db.cur.execute(f'SELECT distrito FROM sebo_messias WHERE link="{link}"').fetchone()[0]
        livroTrackers = ['nanquim', 'darkside', 'susan sontag', 'isaac asimov', 'Ludwig von Mises', 'Milton FRIEDMAN', 'h.g wells', 'josé saramago', 'bene barnosa', 'paulo coelho', 'cortela', 'daniel kahneman', 'john milton', 'mitnick', 'alan lightman', 'richard p. feynman', 'philip k. dick', 'stephen hawking', 'carl sagan', 'ludvig von mises', 'milton friedman', 'bastiat', 'john milton', 'johann wolfgang von', 'bernard cornwell', 'richard dawkins', 'stephen king', 'Adam Smith', 'Frank Herbert', 'George R.R. Martin', 'Hayek', 'tropas estelares', 'Laranja Mecânica', 'Clube da luta', 'coraline', 'mitologia nórdica', 'Deuses Americanos', 'Planeta dos Macacos', 'A Profecia', 'Fahrenheit 451', 'Em busca de Watership Down', 'O labirinto do fauno', 'neuromancer']
        hqTrackers = ['dura', 'maus', 'habibi']
        while True:
            try:
                self.browser.get(link)
                print(f'\r{" " * 200}\r{datetime.now()} | Acessando: {link}', end='')
                sleep(0.5)
                break
            except WebDriverException: pass

        try:
            capaURL = self.browser.find_element(By.ID, 'ctl00_cphMain_rptImage_ctl00_imgProduto').get_attribute('src')
            capaLocal = capaURL.split('/')[-1]
            DownloadImage().download(capaURL, 'sebodomessias')
        except NoSuchElementException: capaLocal = 'Null'

        try:
            titulo = self.browser.find_element(By.ID, 'ctl00_cphMain_labelTitulo').text
            if not titulo: titulo = self.browser.find_element(By.ID, 'ctl00_cphMain_lblTitulo').text
        except NoSuchElementException: titulo = 'Null'

        try:
            assunto = self.browser.find_element(By.ID, 'ctl00_cphMain_labelCategoriaTitulo').find_element(By.TAG_NAME, 'a').text
            if not assunto: assunto = self.browser.find_element(By.ID, 'ctl00_cphMain_lblCategoriaTitulo').find_element(By.TAG_NAME, 'a').text
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
            curiosidades = self.browser.find_element(By.CSS_SELECTOR, '[id*="pnlCuriosidade"]').text.replace('Curiosidades: ', '')
            if curiosidades == '':
                curiosidades = 'Null'
        except NoSuchElementException: curiosidades = 'Null'
        
        checado = '1'
        if 'vendido' in self.browser.find_element(By.CSS_SELECTOR, '[id*="divCardBuy"]').text: status = 'Vendido'
        else: status = 'À venda'
        menorPreco = precoDesconto
        ultimoUpdate = UtilsFunctions.getStrTime()
        varId = UtilsFunctions.randintID()
        dados = (titulo,
                 varId,
                 district,
                 assunto,
                 autor,
                 tradutor,
                 editora,
                 ano,
                 conservacaoCapa,
                 conservacaoMiolo,
                 acabamento,
                 precoDesconto,
                 menorPreco,
                 idioma,
                 edicao,
                 numeroPaginas,
                 formato,
                 status,
                 curiosidades,
                 ultimoUpdate,
                 isbn,
                 capaLocal,
                 link,
                 checado,
                 link)
        db.update(dados)                                   
        db.con.close()

        if 'hq' in district.lower():
            for tracker in hqTrackers:
                for dado in dados:
                    if tracker.lower() in dado.lower():
                        mensagem = f'Titulo: {titulo}%0Adistrict: {district}%0AAssunto: {assunto}%0AAutor: {autor}%0AEditora: {editora}%0AAno: {ano}%0AConservação Capa: {conservacaoCapa}%0AConservação Miolo: {conservacaoMiolo}%0AISBN: {isbn}%0AAcabamento: {acabamento}%0ATradutor: {tradutor}%0AIdioma: {idioma}%0AEdição: {edicao}%0ANúmero de Páginas: {numeroPaginas}%0AFormato: {formato}%0APreço: {precoDesconto}%0AStatus: {status}%0ACuriosidades:{curiosidades}%0AURL: {link}'
                        #TelegramBot().sendPhoto(capaLocal)
                        #TelegramBot().sendMessage(mensagem)
                        print(f'\r{datetime.now()} | Mensagem enviada para {CHAT_ID}', end='')
                        self.browser.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensagem.replace('&', 'e')}")
    
                        

        elif 'livro' in district.lower():
            for tracker in livroTrackers:
                for dado in dados:
                    if tracker.lower() in dado.lower():
                        mensagem = f'Titulo: {titulo}%0Adistrict: {district}%0AAssunto: {assunto}%0AAutor: {autor}%0AEditora: {editora}%0AAno: {ano}%0AConservação Capa: {conservacaoCapa}%0AConservação Miolo: {conservacaoMiolo}%0AISBN: {isbn}%0AAcabamento: {acabamento}%0ATradutor: {tradutor}%0AIdioma: {idioma}%0AEdição: {edicao}%0ANúmero de Páginas: {numeroPaginas}%0AFormato: {formato}%0APreço: {precoDesconto}%0AStatus: {status}%0ACuriosidades:{curiosidades}%0AURL: {link}'
                        #TelegramBot().sendPhoto(capaLocal)
                        # TelegramBot().sendMessage(mensagem)
                        self.browser.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensagem}")
                        
    def getMessiasPages(self, district):
        counter = 0
        if district == 'livro': self.browser.get('https://sebodomessias.com.br/livros')
        elif district == 'HQ/Mangá': self.browser.get('https://sebodomessias.com.br/gibis')
        else:
            self.browser.get(district)
            if 'Produto=5' in district: district = 'HQ/Mangá'
            if 'Produto=1' in district: district = 'livro'

        db = BancoDeDadosMessias()
        sleep(0.5)

        while True:
            itens = self.browser.find_elements(By.CLASS_NAME, 'card-news')

            for item in itens:
                name = item.find_element(By.CLASS_NAME, 'product-title').text.strip().replace('\n', '')
                price = item.find_element(By.CLASS_NAME, 'price-new').text.strip().replace('\n', '')

                link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
                data = UtilsFunctions.getStrTime()

                if db.exists('link', link):
                    res = db.cur.execute(f"SELECT preco from sebo_messias WHERE link='{link}'")
                    priceDB = res.fetchone()[0]
                    res = db.cur.execute(f"SELECT menorPreco from sebo_messias WHERE link='{link}'")
                    lowestPrice = res.fetchone()[0].replace('.', '').replace('R$ ', '').replace(',', '.')

                    if price != priceDB:
                        db.cur.execute(f"""
                                        UPDATE sebo_messias
                                        SET preco='R$ {price}'
                                        WHERE link='{link}'
                                        """)
                        print(f'\r{" " * 200}\r{datetime.now()} | Preço Atualizado: {name}\nAntigo: {priceDB}\nNovo: {price}', end='')

                    if not 'Null' in priceDB and not 'Null' in lowestPrice:
                            if float(price.replace('.', '').replace('R$ ', '').replace(',', '.')) < float(lowestPrice):
                                db.cur.execute(f"""
                                                UPDATE sebo_messias
                                                SET menorPreco='R$ {price}'
                                                WHERE link='{link}'
                                                """)
                    db.con.commit()

                elif not db.exists('link', link):
                    checado = '0'
                    varID = UtilsFunctions.randintID()
                    BancoDeDadosMessias().inserir((
                                                 name,
                                                 varID,
                                                 district,
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 price,
                                                 price,
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 'null',
                                                 data,
                                                 'null',
                                                 'null',
                                                 link,
                                                 checado))
            try:
                nextPageElement = self.browser.find_elements(By.CLASS_NAME, 'page-link')[-1]
                previousURL = self.browser.current_url
                nextPageElement.click()
                counter += 1
                sleep(0.5)

                if previousURL == self.browser.current_url:
                    break
                
            except IndexError:
                print('fim')
                break
            except TimeoutException: pass
            except WebDriverException: pass

        self.browser.quit()
        db.cur.close()

    def updateSeboMessiasNews(self) -> None:
        # self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=1&Dias=1&cdTpCategoria=0')
        self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=5&Dias=1&cdTpCategoria=0')


def main() -> None:
    #ver se dá pra passar como argumento essas variaveis
    global getAllPages
    global accessPages
    global getComics
    global getBooks

    if getAllPages:
        getAllPages = False
        getComics = True
        getBooks = True
        
    if getComics:
        driver = Driver()
        driver.headless = headless
        driver.initDriver()
        driver.getMessiasPages('HQ/Mangá')
        
    if getBooks:
        driver = Driver()
        driver.headless = headless
        driver.initDriver()
        driver.getMessiasPages('livro')
        
        
    if accessPages:
        driver = Driver()
        driver.headless = headless
        driver.initDriver()
        driver.accessMessiasPages()

if __name__ == '__main__':
    getAllPages = False
    getBooks = False
    getComics = False
    accessPages = False
    headless = False

    for option in argv:
        if '--get-all-pages' in option: getAllPages = True
        if '--get-comics' in option: getComics = True
        if '--get-books' in option: getBooks = True
        if '--access-pages' in option: accessPages = True
        if '--headless' in option: headless = True

    schedule.every(1).seconds.do(main)

    while True:
        schedule.run_pending()
