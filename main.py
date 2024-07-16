import os
import requests
import telepot
from sys import argv
from datetime import datetime
from bancodedados import *
from random import randint
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from tokens import *


class DownloadImage():
    import urllib.request

    def download(self, url, path=''):
        if url:
            if 'guiadosquadrinhos' in url:
                    nomeNaoTratado = url.split('=')[-1].replace('/', '')
                    nome = ''

                    for letra in nomeNaoTratado:
                        if letra.isalnum() or letra == '.': nome += letra

                    path = os.getcwd() + '/capas_guia_dos_quadrinhos'
                    if not os.path.exists(path): os.mkdir(path)


            elif 'messias' in url:
                nome = url.split('/')[-1]
                path = os.getcwd() + './images'
                if not os.path.exists(path): os.mkdir(path)
            else: nome = str(randint(10**8, 10**9-1)) + '.jpg'
            self.urllib.request.urlretrieve(url, path + '/' + nome )


class Driver():
    def __init__(self):
        if os.name == 'nt': self.browser = webdriver.Chrome()

    def acessMessiasPages(self) -> None:
        db = BancoDeDadosMessias()
        columns = db.cur.execute('SELECT link, checado FROM sebo_messias').fetchall()

        for column in columns:
            if column[1] == '0': self.scrapMessiasPage(column[0])

    def scrapMessiasPage(self, link):
        db = BancoDeDadosMessias()
        district = db.cur.execute(f'SELECT distrito FROM sebo_messias WHERE link="{link}"').fetchone()[0]
        bot = telepot.Bot(TELEGRAM_TOKEN)
        livroTrackers = []#['susan sontag', 'craig thompson', 'isaac asimov', 'emily bront', 'george orwell', 'lewis carroll', 'h.g wells', 'saramago', 'frank herbert', 'verne', 'heinlein', 'kafka', 'darkside', 'nanquim', 'schopenheuer', 'bene barnosa', 'paulo coelho', 'cortela', 'kahneman', 'john milton', 'robert c', 'simon sinek', 'mitnick', 'alan lightman', 'feynman', 'philip k', 'ray bradbury', 'stephen hawking', 'carl sagan', 'david seltzer', 'bram stoker', 'lovecraft', 'edgar allan poe', 'mary shelley', 'ludvig von mises', 'milton friedman', 'bastiat', 'homero', 'john milton', 'johann wolfgang von', 'douglas adams', 'neil gaiman', 'bernard cornwell', 'anthony burgess', 'chuck palahniuk', 'pierre boulle', 'arthur c. clarke', 'richard dawkins', 'agatha christie', 'orleans', 'richard adams', 'stephen king']
        hqTrackers = ['dura', 'maus', 'habibi']
        self.browser.get(link)
        print('Acessando: ', link)
        sleep(1)

        try:
            capaURL = self.browser.find_element(By.ID, 'ctl00_cphMain_rptImage_ctl00_imgProduto').get_attribute('src')
            capaLocal = capaURL.split('/')[-1]
            DownloadImage().download(capaURL, 'sebodomessias')
        except NoSuchElementException: capaLocal = 'Null'

        try: titulo = self.browser.find_element(By.ID, 'ctl00_cphMain_labelTitulo').text
        except NoSuchElementException: titulo = 'Null'

        try: categoria = self.browser.find_element(By.ID, 'ctl00_cphMain_labelCategoriaTitulo').find_element(By.TAG_NAME, 'a').text
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
        
        checado = '1'
        if 'vendido' in self.browser.find_element(By.CSS_SELECTOR, '[id*="divCardBuy"]').text: status = 'Vendido'
        else: status = 'À venda'
        dados = (titulo,
                 link,
                 capaLocal,
                 district,
                 categoria,
                 autor,
                 editora,
                 ano,
                 conservacaoCapa,
                 conservacaoMiolo,
                 isbn,
                 acabamento,
                 tradutor,
                 idioma,
                 edicao,
                 numeroPaginas,
                 formato,
                 preco,
                 precoDesconto,
                 status,
                 curiosidades,
                 checado,
                 link)
        db.update(dados)                                   
        db.con.close()

        if 'hq' in district.lower():
            for tracker in hqTrackers:
                for dado in dados:
                    if tracker in dado.lower():
                        #bot.sendPhoto(CHAT_ID, photo=open(f'./images/{capaLocal}', 'rb'))
                        mensagem = (f'Titulo: {titulo}\ndistrict: {district}\nCategoria: {categoria}\nAutor: {autor}\nEditora: {editora}\nAno: {ano}\nConservação Capa: {conservacaoCapa}\nConservação Miolo: {conservacaoMiolo}\nISBN: {isbn}\nAcabamento: {acabamento}\nTradutor: {tradutor}\nIdioma: {idioma}\nEdição: {edicao}\nNúmero de Páginas: {numeroPaginas}\nFormato: {formato}\nPreço Base: {preco}\nPreço com Desconto: {precoDesconto}\nStatus: {status}\ncuriosidades\nURL: {link}')
                        bot.sendMessage(CHAT_ID, mensagem)
        elif 'livro' in district.lower():
            for tracker in livroTrackers:
                for dado in dados:
                    if tracker in dado.lower():
                        print(tracker, dado, dados)
                        #bot.sendPhoto(CHAT_ID, photo=open(f'./images/{capaLocal}', 'rb'))
                        mensagem = (f'Titulo: {titulo}\ndistrict: {district}\nCategoria: {categoria}\nAutor: {autor}\nEditora: {editora}\nAno: {ano}\nConservação Capa: {conservacaoCapa}\nConservação Miolo: {conservacaoMiolo}\nISBN: {isbn}\nAcabamento: {acabamento}\nTradutor: {tradutor}\nIdioma: {idioma}\nEdição: {edicao}\nNúmero de Páginas: {numeroPaginas}\nFormato: {formato}\nPreço Base: {preco}\nPreço com Desconto: {precoDesconto}\nStatus: {status}\ncuriosidades\nURL: {link}')
                        bot.sendMessage(CHAT_ID, mensagem)
                        #print(mensagem)

    def getMessiasPages(self, district):
        counter = 0
        if district == 'livro': self.browser.get('https://sebodomessias.com.br/livros')
        elif district == 'HQ/Mangá': self.browser.get('https://sebodomessias.com.br/gibis')
        db = BancoDeDadosMessias()
        res = db.cur.execute("SELECT * FROM sebo_messias")
        columns = res.fetchall()
        sleep(1)

        while True:
            itens = self.browser.find_elements(By.CLASS_NAME, 'card-news')

            for item in itens:
                name = item.find_element(By.CLASS_NAME, 'product-title').text.strip().replace('\n', '')
                pricePlaceHolder = item.find_element(By.CLASS_NAME, 'price-new').text.strip().replace('\n', '')
                price = ''

                for letter in pricePlaceHolder:
                    if letter.isnumeric() or letter == ',': price += letter

                link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
                data = datetime.now().isoformat()[0:-13]

                if db.exists('link', link):
                    for column in columns:
                        if link in column[0]:
                            if float(price.replace(',', '.')) < float(column[18].replace(',', '.')):
                                db.cur.execute(f"""
                                               UPDATE sebo_messias
                                               SET precoDesconto='{price}'
                                               WHERE link='{link}'
                                               """)
                                db.con.commit()
                                print('Preço atualizado')
                elif not db.exists('link', link):
                    checado = '0'
                    BancoDeDadosMessias().inserir((
                    link,
                    name,
                    'Null',
                    district,
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    'Null',
                    price,
                    'Null',
                    'Null',
                    data,
                    checado
                    ))

            nextPageElement = self.browser.find_elements(By.CLASS_NAME, 'page-link')[-1]
            if nextPageElement.text.lower() == 'next' or nextPageElement.text == '...'.lower():
                nextPageElement.click()
                counter += 1
                sleep(1)
            else:
                print('fim')
                break


        db.cur.close()

    def acessarGuiaDosQuadrinhosPages(self) -> None:
        bd = BancoDeDadosBasicoGDQ()
        res = bd.cur.execute('SELECT * FROM guia_basico')
        linksPai = res.fetchall()
        mandar = False

        for site in linksPai:
            #if site[0] in 'http://www.guiadosquadrinhos.com/capas/batman-1-serie/ba001102':
            if site[0] in 'http://www.guiadosquadrinhos.com/capas/cretinos-nao-mandam-flores-os/cr010100':
                mandar = True

            print(site[0])
            if mandar:
                while True:
                    numeroDestaEdicao = 0
                    self.browser.get(site[0])
                    sleep(2)
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

                            print(site)
                            print('======================================================================================================================================================\n', site[0])
                            self.scrapGuiaDosQuadrinhosPage(site[0], link, numeroDestaEdicao, site[5])
                        break

    def scrapGuiaDosQuadrinhosPage(self, linkPai='', link='', numeroDestaEdicao='', edicoesTotais='') -> None:
        while True:
            try:
                self.browser.get(link)
                self.showPrints = True
                sleep(2)
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

                    #######################

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


if __name__ == '__main__':
    if argv[1] == '-g':
        Driver().acessarGuiaDosQuadrinhosPages()
        # Driver().scrapGuiaDosQuadrinhosPage('http://www.guiadosquadrinhos.com/capas/100-balas/10012100', 'http://www.guiadosquadrinhos.com/edicao/ai-mocinho-9-serie-n-1/ai001900/54523', '30', '72')
    elif argv[1] == '-s':
        # Driver().getMessiasPages('HQ/Mangá')
        #Driver().getMessiasPages('livro')
        Driver().acessMessiasPages()
