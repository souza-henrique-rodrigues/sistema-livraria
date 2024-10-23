from classeLivro import Livro
from datetime import datetime




livro1 = Livro("1", "O Senhor dos Anéis", 1954, "Fantasia", "HarperCollins", 59.90, 10)
livro2 = Livro("2", "1984", 1949, "Ficção Distópica", "Companhia das Letras", 45.00, 5)
livro3 = Livro("3", "Dom Quixote", 1605, "Clássico", "Planeta", 39.90, 7)


class Livraria():
    def __init__(self):
        
        self.ano_atual = datetime.now().year
        self.livros = [livro1,livro2,livro3]
    
    def verificarLivroExiste(self):
        if len(self.livros) > 0:
            return True
    
    def cadastrarLivro(self):      
        codigo = (input("Informe o codigo : "))   
        titulo = input("Informe o nome do livro : ")  
        
        while True:
            try:
                ano = int(input("Informe o ano : "))                        
                if (ano > self.ano_atual):
                    print("O ano de lançamento não pode ser maior que o ano atual.")
                else:
                    break
            except ValueError:
                print("Insira um valor valido : ")
        
        genero = input("Informe de qual gênero é o livro :")
        editora = input("Informe qual editora publicou o livro : ")
        
        while True:
            try:
                valor = float(input("Informe qual valor do livro : "))
                break
            except ValueError:
                print("Informe um valor valido, como : 19.90 ")
        
        while True:
            try:
                quantidade = int(input("Informe quantos livros serão adicionados ao sistema : "))
                if (quantidade <= 0):
                    print("Informe um valor inteiro maior que 0 : ")
                else:
                    break
            except ValueError:
                print("Informe um valor inteiro maior que 0 : ")                        
        
        # Insere as informações no objeto instanciado
        livro = Livro(codigo,titulo,ano,genero,editora,valor,quantidade)
        self.livros.append(livro)
        
    def mostrarLivros(self):
        if self.verificarLivroExiste:        
            for livro in self.livros:
                livro.infoLivro()
        else:
            print("Nenhum livro cadastrado até o momento.")

    def buscarLivroNome(self):
        if self.verificarLivroExiste:
            nome_livro = input("Informe o livro que deseja buscar : ")        
            for livro in self.livros:
                if nome_livro == livro.titulo:
                    return livro.infoLivro()
        else:
            print("Nenhum livro em estoque no momento")
    
    def buscarLivroGenero(self):
        if self.verificarLivroExiste:
            genero = input("Informe qual categoria deseja procurar : ")        
            for livro in self.livros:
                if livro.genero == genero:
                    livro.infoLivro()
        else:
            print(f"Nenhum livro encontrado da categoria {genero}")
    
    def buscarLivroPreco(self):
        if self.verificarLivroExiste:
            valor = float(input("Buscar livros com valor a baixo ou igual à : "))
            for livro in self.livros:
                if livro.valor <= valor:
                    livro.infoLivro()
        else:
            print("Nenhum livro cadastrado até o momento.")
    
    def buscarLivroQtdEstoque(self):
        if self.verificarLivroExiste:
            quantidade = int(input("Buscar livros com quantidade maior ou igual à : "))
            for livro in self.livros:
                if livro.quantidade >= quantidade:
                    livro.infoLivro()
        else:
            print("Nenhum livro cadastrado até o momento.")
    
    def valorTotalEstoque(self):
        if self.verificarLivroExiste:
            valor = 0
            for livro in self.livros:
                valor += livro.valor * livro.quantidade                
            print(f"valor total de estoque R$ : {valor}")
        else:
            print("Nenhum livro cadastrado até o momento.")
    
    def cadastrarViaTxt(self):
        arquivo = open("livro.txt",'r',encoding='utf-8') 
        linha = arquivo.readline().replace("\n","")
        
        while linha:
            info_linha = linha.split(",")
            livro_existe = False
            for livro in self.livros:
                if livro.codigo == info_linha[0]:
                    livro_existe = True
                    break
            if not livro_existe:         
                livro = Livro(info_linha[0],info_linha[1],info_linha[2],info_linha[3],info_linha[4],info_linha[5],info_linha[6])
                self.livros.append(livro)
                
            linha = arquivo.readline().replace("\n","")
    
    def carregarLivrosTxt(self):
        #salvar o codigo de todos livros existentes no txt
        codigos_livros_txt = []
        arquivo = open("livro2.txt",'r',encoding='utf-8') 
        linha = arquivo.readline().replace("\n","")
        
        while linha:
            info_linha = linha.strip().split(",")
            codigos_livros_txt.append(info_linha[0])
            linha = arquivo.readline().replace("\n","")
        
        
        arquivoEscrita = open('livro2.txt', 'a', encoding="utf-8")
        for livro in self.livros:
            codigo = str(livro.codigo)
            titulo = str(livro.titulo)
            ano = str(livro.ano)
            genero = str(livro.genero)
            editora = str(livro.editora)
            valor = str(livro.valor)
            quantidade = str(livro.quantidade)
            
            if livro.codigo not in codigos_livros_txt:
                arquivoEscrita.write(f"{codigo},{titulo},{ano},{genero},{editora},{valor},{quantidade}\n")
                
        arquivoEscrita.close()
        
                                        
if __name__ == "__main__":

        livraria1 = Livraria()
        
        run = True
        while(run):
        
            pergunta = input("Qual opção deseja realizar ?\n \n 1: Cadastrar novo livro\n 2: Listar todos os livros\n 3: Buscar livro por nome\n 4: Buscar livro por categoria\n 5: Buscar livro por preço\n 6: Buscar livro por quantidade em estoque\n 7: Mostrar valor total em estoque\n 8: Cadastar livros via .txt\n 9: Carregar livros no arquivo txt\n 0: Encerrar programa\n opção : ")
                    
            match pergunta:

                case "1":
                    livraria1.cadastrarLivro()
                    
                case "2":
                    livraria1.mostrarLivros()
                    
                case "3":
                    livraria1.buscarLivroNome()
                
                case "4":
                    livraria1.buscarLivroGenero()
                
                case "5":
                    livraria1.buscarLivroPreco()
                
                case "6":
                    livraria1.buscarLivroQtdEstoque()
                
                case "7":
                    livraria1.valorTotalEstoque()
                
                case "8":
                    livraria1.cadastrarViaTxt()
                    
                case "9":
                    livraria1.carregarLivrosTxt()
                
                case "0":
                    pergunta = input("Deseja salvar as alterações para o arquivo txt ? Sim ou Não ").lower()
                    
                    if pergunta == "sim":
                        livraria1.carregarLivrosTxt() 
                        run = False
                        
                    run = False              
                case _:
                    print("Insira um valor valido")
                    
                
                
    
    
    
    
            
    