import os
import sqlite3
import schedule
import asyncio
from UtilsFunctions import UtilsFunctions
from TelegramBot import TelegramBot
from tokens                         import *
from sys                            import argv
from datetime                       import datetime
from bancodedados                   import *
from random                         import randint
from time                           import sleep
from selenium                       import webdriver
from selenium.webdriver.common.by   import By
from urllib.error                   import URLError
from selenium.common.exceptions     import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    WebDriverException
)


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
            capaLocal = 'Null'
        except NoSuchElementException: capaLocal = 'Null'

        try:
            titulo = self.browser.find_element(By.ID, 'ctl00_cphMain_labelTitulo').text
            if not titulo: titulo = self.browser.find_element(By.ID, 'ctl00_cphMain_lblTitulo').text
        except NoSuchElementException: titulo = 'Null'

        try:
            assunto = self.browser.find_element(By.ID, 'ctl00_cphMain_labelCategoriaTitulo').find_element(By.TAG_NAME, 'a').text
            if not assunto: assunto = self.browser.find_element(By.ID, 'ctl00_cphMain_lblCategoriaTitulo').find_element(By.TAG_NAME, 'a').text
        except NoSuchElementException: assunto = 'Null'
        
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
        newItensCounter = 0
        updatedItens = 0
        UtilsFunctions.writeLog(f'{datetime.now()} | Iniciando busca')
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
                    updatedItens += 1
                    res = db.cur.execute(f"SELECT preco from sebo_messias WHERE link='{link}'")
                    priceDB = res.fetchone()[0]
                    res = db.cur.execute(f"SELECT menorPreco from sebo_messias WHERE link='{link}'")
                    #replace('.', '') probably not necessary
                    lowestPrice = res.fetchone()[0].replace('.', '').replace('R$ ', '').replace(',', '.')

                    if price != priceDB:
                        db.cur.execute(f"""
                                        UPDATE sebo_messias
                                        SET preco='R$ {price}'
                                        WHERE link='{link}'
                                        """)
                        message = f'{datetime.now()} | Preço Atualizado: {name} | Antigo: {priceDB} | Novo: {price}'
                        UtilsFunctions.writeLog(message)
                        print(f'\r{" " * 200}{message}\r', end='')

                    if not 'Null' in priceDB and not 'Null' in lowestPrice:
                            #replace('.', '') probably not necessary
                            if float(price.replace('.', '').replace('R$ ', '').replace(',', '.')) < float(lowestPrice):
                                db.cur.execute(f"""
                                                UPDATE sebo_messias
                                                SET menorPreco='R$ {price}'
                                                WHERE link='{link}'
                                                """)
                    db.con.commit()

                elif not db.exists('link', link):
                    newItensCounter += 1
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
                nextPageMultipleOfTen = self.browser.find_elements(By.CLASS_NAME, 'page-link')[-2].get_attribute('href')
                
                print(nextPageMultipleOfTen.split('&')[5])
                previousURL = self.browser.current_url
                nextPageElement.click()
                counter += 1
                sleep(0.5)

                if previousURL == self.browser.current_url: break
                
            except IndexError: break
            except TimeoutException: pass
            except WebDriverException: pass

        UtilsFunctions.writeLog(f'{datetime.now()} | Total de itens novos = {newItensCounter} | Total de itens atualizados = {updatedItens}')
        self.browser.quit()
        db.cur.close()

    def updateSeboMessiasNews(self) -> None:
        # self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=1&Dias=1&cdTpCategoria=0')
        self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=5&Dias=1&cdTpCategoria=0')


def mainSebo() -> None:
    getBooks = True
    getComics = True
    accessPages = True
    headless = False

    try:
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
    except WebDriverException: driver.browser.quit()

if __name__ == '__main__':
    # schedule.every().day.at('12:00').do(mainSebo)
    # schedule.every().day.at('19:00').do(mainSebo)

    # while True:
    #     schedule.run_pending()

    mainSebo()
    