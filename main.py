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
        if os.name == 'nt': self.browser = webdriver.Firefox()
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
                print('Acessando: ', link)
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
                        print(mensagem)
                        self.browser.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensagem.replace('&', 'e')}")
    
                        

        elif 'livro' in district.lower():
            for tracker in livroTrackers:
                for dado in dados:
                    if tracker.lower() in dado.lower():
                        print(tracker, dado, dados)
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
                        print(f'Preço Atualizado: {name}\nAntigo: {priceDB}\nNovo: {price}')

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

    def acessarGuiaDosQuadrinhosPages(self) -> None:
        bd = BancoDeDadosBasicoGDQ()
        res = bd.cur.execute('SELECT * FROM guia_basico')
        linksPai = res.fetchall()
        mandar = False

        for site in linksPai:
            if site[0] in 'http://www.guiadosquadrinhos.com/capas/thor-3-serie/th011134': mandar = True

            if mandar:
                while True:
                    numeroDestaEdicao = 0
                    self.browser.get(site[0])
                    sleep(0.5)

                    try: 
                        self.browser.find_element(By.ID, 'error-information-popup-content')
                    except NoSuchElementException:
                        try:
                            self.browser.find_element(By.XPATH, "//option[@value='120']").click()
                            sleep(1)
                        except NoSuchElementException: pass
                        links = []
                        for link in self.browser.find_elements(By.CLASS_NAME, 'suppress'): links.append(link.get_attribute('href'))
                        for link in links:
                            numeroDestaEdicao += 1
                            print('===========================================================\n', site[0])
                            try:    self.scrapGuiaDosQuadrinhosPage(site[0], link, numeroDestaEdicao, site[5])
                            except: print('Error in ', link)
                        break

    def scrapGuiaDosQuadrinhosPage(self, linkPai='', link='', numeroDestaEdicao='', edicoesTotais='') -> None:
        while True:
            try:
                self.browser.get(link)
                self.showPrints = True
                sleep(0.5)
                try:
                    titulo = self.browser.find_element(By.ID, 'nome_titulo_lb').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "titulo"')
                    titulo = ''

                try:
                    capa = self.browser.find_element(By.ID, 'ampliar_capa')
                    capaLink = capa.get_attribute('href')
                    if capa.get_attribute('title') == 'Capa já adicionada': capaLocal = ''
                    else:
                        capaLocal = './capas_guia_dos_quadrinhos/' + capaLink.split('=')[-1]
                        DownloadImage().download(capaLink, 'guiadosquadrinhos')
                except NoSuchElementException:
                    try:
                        capaIMG = self.browser.find_element(By.ID, 'cover').find_element(By.TAG_NAME, 'img')
                        capaLink = self.browser.find_element(By.ID, 'cover').get_attribute('href')
                        if not capaLink: capaLink = capaIMG.get_attribute('src')
                        if not self.browser.find_elements(By.CSS_SELECTOR, '#sem_capa'):
                            if capaIMG.get_attribute('title') == 'Capa já adicionada': capaLocal = ''
                            else:
                                capaLocal = './capas_guia_dos_quadrinhos/' + capaLink.split('=')[-1]
                                DownloadImage().download(capaLink, 'guiadosquadrinhos')
                        else:
                            capaLocal = ''
                    except NoSuchElementException:
                        print('No Such Element "capaLink", "cover')
                        capaLocal = ''

                try:
                    publicado = self.browser.find_element(By.ID, 'data_publi').text.strip().replace('\n', '')
                except NoSuchElementException: 
                    print('No Such Element "publicado"')
                    publicado = ''

                try:
                    editora = self.browser.find_element(By.ID, 'editora_link').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "editora"')
                    editora = ''

                try:
                    licenciador = self.browser.find_element(By.ID, 'licenciador').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "licenciador"')
                    licenciador = ''

                try:
                    categoria = self.browser.find_element(By.ID, 'categoria').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "categoria"')
                    categoria = ''

                try:
                    genero = self.browser.find_element(By.ID, 'genero').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "genero"')
                    genero = ''

                try:
                    status = self.browser.find_element(By.ID, 'status').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "status"')
                    status = ''

                try:
                    paginas = self.browser.find_element(By.ID, 'paginas').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "paginas"')
                    paginas = ''
            
                try:
                    formato = self.browser.find_element(By.ID, 'formato').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "formato"')
                    formato = ''
                try:
                    preco = self.browser.find_element(By.ID, 'preco').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "preco"')
                    preco = ''
                try:
                    nota = self.browser.find_element(By.ID, 'Media_votos').text.strip().replace('\n', '')
                except NoSuchElementException:
                    print('No Such Element "nota"')
                    nota = ''
                try:
                    totalVotosb = self.browser.find_element(By.ID, 'total_votos').text.strip().replace('\n', '')
                    totalVotos = ''
                    for letra in totalVotosb:
                        if letra.isnumeric(): totalVotos += letra
                except NoSuchElementException:
                    print('No Such Element "totalVotos"')
                    totalVotos = ''
                try:
                    posicaoMaisColecionadasb = self.browser.find_element(By.ID, 'box_colecao').text
                    posicaoMaisColecionadas = ''
                    for letra in posicaoMaisColecionadasb:
                        if letra.isnumeric(): posicaoMaisColecionadas += letra
                except NoSuchElementException:
                    print('No Such Element "posicaoMaisColecionadas"')
                    posicaoMaisColecionadas = ''
                try: capitulos = len(self.browser.find_elements(By.CLASS_NAME, 'historia'))
                except NoSuchElementException:
                    print('No Such Element "capitulos"')
                    capitulos = ''
                try: textoDetalhes = self.browser.find_element(By.ID, 'texto_pag_detalhe').text
                except NoSuchElementException:
                    print('No Such Element "textoDetalhes"')
                    textoDetalhes = ''
                if self.showPrints: print(f'Titulo: {titulo}\nPublicado: {publicado}\nEditora: {editora}\nLicenciador: {licenciador}\nCategoria: {categoria}\nGenero: {genero}\nStatus: {status}\nPáginas: {paginas}\nFormato: {formato}\nPreço: {preco}\nNota: {nota}\nTotal Votos: {totalVotos}\nPosição Mais Colecionadas: {posicaoMaisColecionadas}\nCapitulos: {capitulos}')

                if titulo:
                    bd = BancoDeDadosGDQ()
                    bd.inserir((titulo, capaLocal, link, linkPai, publicado, editora, licenciador, categoria, genero, status, paginas, formato, preco, nota, totalVotos, posicaoMaisColecionadas, numeroDestaEdicao, edicoesTotais, capitulos, textoDetalhes))
                    break
            except TimeoutException: pass
        
    def getGuiaDosQuadrinhosPages(self) -> None:
        site = 'http://www.guiadosquadrinhos.com/titulos/'
        alphabet = '$abcdefghijklmnopqrstuvwzyz'
        self.browser.get(site)
        sleep(1)
        self.browser.find_element(By.XPATH, "//option[@value='100']").click()
        sleep(1)
        
        for letter in alphabet:
            self.browser.get(site + letter)
            sleep(1)
            self.browser.find_element(By.XPATH, "//option[@value='100']").click()

            while True:
                sleep(1)
                counter = 0
                for td in self.browser.find_elements(By.TAG_NAME, 'td'):
                    counter += 1
                    if counter == 1:
                        titulo = td.text
                        link = td.find_element(By.TAG_NAME, 'a').get_attribute('href').replace('..', 'http://www.guiadosquadrinhos.com/')
                    elif counter == 2: editora = td.text
                    elif counter == 3: licenciador = td.text
                    elif counter == 4: periodo = td.text
                    elif counter == 5: nEdicoes = td.text

                    if counter == 5:
                        print(f'Link: {link}\nTitulo: {titulo}\nEditora: {editora}\nLicenciador: {licenciador}\nPeriodo: {periodo}\nN°Edições: {nEdicoes}')
                        BancoDeDadosBasicoGDQ().inserir((link, titulo, editora, licenciador, periodo, nEdicoes))
                        counter = 0

                try: self.browser.find_elements(By.CLASS_NAME, 'next_last')[2].click()
                except ElementNotInteractableException: break

    def updateSeboMessiasNews(self) -> None:
        # self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=1&Dias=1&cdTpCategoria=0')
        self.getMessiasPages('https://sebodomessias.com.br/UltimosItens.aspx?cdTpProduto=5&Dias=1&cdTpCategoria=0')




def main() -> None:
    #ver se dá pra passar como argumento essas variaveis
    global getAllPages
    global accessPages

    if getAllPages:
        getAllPages = False
        Driver().getMessiasPages('HQ/Mangá')
        Driver().getMessiasPages('livro')
#    elif not getAllPages:
#        Driver().updateSeboMessiasNews()
        
    if accessPages: Driver().accessMessiasPages()
        

# def test() -> None:
#     messiasDB = BancoDeDadosMessias()
    
#     columns = messiasDB.cur.execute("""
#                                     SELECT
#                                         * FROM sebo_messias
#                                     WHERE
#                                         titulo LIKE 'Crimson%' AND distrito='HQ/Mangá' AND ano='2002'""").fetchall()

#     # for column in columns:
#     print(columns)

if __name__ == '__main__':
    ignoreBooks = False
    getAllPages = False
    ignoreBooks = False
    accessPages = False

    for option in argv:
        if '--get-all-pages' in option: getAllPages = True
        if '--ignore-books' in option: ignoreBooks = True
        if '--access-pages' in option: accessPages = True

    schedule.every(1).seconds.do(main)

    while True:
        schedule.run_pending()
