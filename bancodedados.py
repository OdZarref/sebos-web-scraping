import sqlite3
import os

class BancoDeDadosMessias():
    def __init__(self) -> None:
        if os.path.exists('sebomessias.db'):
            self.con = sqlite3.connect('sebomessias.db')
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect('sebomessias.db')
            self.cur = self.con.cursor()
            self.cur.execute('''
                            CREATE TABLE sebo_messias (
                            titulo,
                            id,
                            distrito,
                            assunto,
                            autor,
                            tradutor,
                            editora,
                            ano,
                            capa,
                            miolo,
                            acabamento,
                            preco,
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
                            checado
                            )''')
            self.con.commit()

    def inserir(self, dados) -> None:
        self.cur.execute("""
                        INSERT INTO sebo_messias (
                            titulo,
                            id,
                            distrito,
                            assunto,
                            autor,
                            tradutor,
                            editora,
                            ano,
                            capa,
                            miolo,
                            acabamento,
                            preco,
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
                            checado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", dados)
        self.con.commit()
        print(f'{dados[0]} adicionado.')

    def update(self, dados):
        self.cur.execute(f"""
                        UPDATE sebo_messias
                        SET titulo = ?,
                        id = ?,
                        distrito = ?,
                        assunto = ?,
                        autor = ?,
                        tradutor = ?,
                        editora = ?,
                        ano = ?,
                        capa = ?,
                        miolo = ?,
                        acabamento = ?,
                        preco = ?,
                        menorPreco = ?,
                        idioma = ?,
                        edicao = ?,
                        numeroPaginas = ?,
                        formato = ?,
                        status = ?,
                        curiosidades = ?,
                        ultimoUpdate = ?,
                        isbn = ?,
                        capaLocal = ?,
                        link = ?,
                        checado = ?
                        WHERE link = ?
                        """, dados)
        self.con.commit()

    def exists(self, column, value):
        res = self.cur.execute(f"SELECT {column} from sebo_messias WHERE {column}='{value}'")
        res = res.fetchall()
        if len(res) > 0:
            return True
            
class BancoDeDadosBasicoGDQ():
    def __init__(self) -> None:
        if os.path.exists('guiabasico.db'):
            self.con = sqlite3.connect('guiabasico.db')
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect('guiabasico.db')
            self.cur = self.con.cursor()
            self.cur.execute('''
                            CREATE TABLE guia_basico (
                            link,
                            titulo,
                            editora,
                            licenciador,
                            periodo,
                            nedicoes
                            )''')
            self.con.commit()

    def inserir(self, dados) -> None:
        self.cur.execute("INSERT INTO guia_basico (link, titulo, editora, licenciador, periodo, nedicoes) VALUES (?, ?, ?, ?, ?, ?)", dados)
        self.con.commit()
        self.con.close()
        print(f'{dados[1]} salvo')

    def contarTotal(self) -> int:
        res = self.cur.execute('SELECT nedicoes FROM guia_basico')
        total = 0
        for item in res.fetchall(): total += int(item[0])

        return total

class BancoDeDadosGDQ():
    def __init__(self) -> None:
        if os.path.exists('guiadosquadrinhos.db'):
            self.con = sqlite3.connect('guiadosquadrinhos.db')
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect('guiadosquadrinhos.db')
            self.cur = self.con.cursor()
            self.cur.execute('''
                CREATE TABLE guia_dos_quadrinhos (
                titulo,
                capaLocal,
                link,
                link_pai,
                publicado,
                editora,
                licenciador,
                categoria,
                genero,
                status,
                numero_paginas,
                formato,
                preco_capa,
                nota,
                total_votos,
                posicao_mais_colecionadas,
                numero_desta_edicao,
                edicoes_totais,
                capitulos,
                detalhes
                )''')
            self.con.commit()
    
    def inserir(self, dados) -> None:
        self.cur.execute('''
        INSERT INTO guia_dos_quadrinhos (
                         titulo,
                         capaLocal,
                         link,
                         link_pai,
                         publicado,
                         editora,
                         licenciador,
                         categoria,
                         genero,
                         status,
                         numero_paginas,
                         formato,
                         preco_capa,
                         nota,
                         total_votos,
                         posicao_mais_colecionadas,
                         numero_desta_edicao,
                         edicoes_totais,
                         capitulos,
                         detalhes)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                         ''', dados)
        self.con.commit()
        self.con.close()
        print(f'{dados[1]} salvo')


#verificar se a tabela foi criada
# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

# cur.execute("""
#     INSERT INTO filme VALUES
#             ('O senhor dos Anéis: A Sociedade do Anel', 2001, 178),
#             ('Conan, O Bárbaro', 1982, 129)

# """)
# con.commit()

#res = cur.execute("SELECT titulo FROM filme")
#print(res.fetchall())

# dados_filmes = [
#     ("Transformers", 2007, 120),
#     ("Guerra Infinita", 2018, 170),
#     ("De Volta Para o Futuro", 1985, 116)
# ]

# cur.executemany("INSERT INTO filme (titulo, ano, duracao) VALUES(?, ?, ?)", dados_filmes)
# con.commit()

# res = cur.execute("SELECT titulo FROM filme")
# print(res.fetchall())

# for linha in cur.execute("SELECT ano, titulo FROM filme ORDER BY ano"):
#     print(linha)

# try:
#     with con:
#         con.execute("INSERT INTO filme (titulo, ano, duracao) VALUES (?, ?, ?)", ('Oppenheimer', 2020, 130))
# except sqlite3.ProgrammingError:
#     print("Banco de dados não acessível")

# res = cur.execute("SELECT titulo, ano, duracao FROM filme")
# print(res.fetchall())
# con.close()
