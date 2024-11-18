from datetime import datetime




class Livraria:
    def __init__(self,titulo,codigo,editora,area,ano,valor,qtd_estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.qtd_estoque = qtd_estoque
    
    def infoGeral(self):
            print(f"Cod#: {self.codigo}")
            print(f"Titulo/Editora: {self.titulo}")
            print(f"Categoria: {self.area}")
            print(f"editora : {self.editora}")
            print(f"ano : {self.ano}")
            print(f"Valor: R$ {self.valor}")
            print(f"Estoque: {self.qtd_estoque}")
            print(f"O valor total em estoque: R$ {self.valor * self.qtd_estoque} ")
    
    
    def procurarLivroNome(self,nomeLivro):
        for livro in livros:
            if (livro.titulo == nomeLivro):
                print(livro.infoGeral())
                break
            else:
                print("Livro não encontrado")    
    
    def procurarLivroCat(self,categoria):
        for livro in livros:
            if (livro.area == categoria):
                print(livro.infoGeral())
        if livro not in livros:
            print("Nenhum livro encontrado. ")   
            
    def procurarLivroQtd(self,quantidade):
        for livro in livros:
            if (livro.qtd_estoque >= quantidade):
                print(livro.infoGeral())
        if livro not in livros:
            print("Livro não encontrado pela quantidade especificada.")
    
    def procurarLivroPreco(self,preco):
        for livro in livros:
            if (livro.valor <= preco):
                print(livro.infoGeral())
        
        if livro not in livros:
            print("Livro não encontrado pelo preço pesquisado.")
    
    def calcularEstoqueTotal(self):
         preco_total = 0
         for livro in livros:
             preco_total += livro.valor * livro.qtd_estoque
         
         print(f"O valor total do estoque é R$ {preco_total}")
         
    
    
    def cadastrarTxt(self):
        
        arquivo = open("livro.txt","r")
        linha = arquivo.readline().replace("\n","")

        while linha:
                info_linha = linha.split(",")
                livro = Livraria(info_linha[0],info_linha[1],info_linha[2],info_linha[3],info_linha[4],info_linha[5],info_linha[6])
                livros.append(livro)
                linha = arquivo.readline().replace("\n","")
        
           

if __name__ == "__main__":
    ano_atual = datetime.now().year
    
    livros = []
    run = True
    while (run):
        
        pergunta = input("Qual opção deseja realizar ?\n \n 1: Cadastrar novo livro\n 2: Listar todos os livros\n 3: Buscar livro por nome\n 4: Buscar livro por categoria\n 5: Buscar livro por preço\n 6: Buscar livro por quantidade em estoque\n 7: Mostrar valor total em estoque\n 8: Carregar  livros txt\n 0: Encerrar programa\n opção : ")
            
        match pergunta:

            case "1":
                titulo = input("Informe o nome do livro : ")                
                while True:
                    try: 
                        codigo = int(input("Informe o codigo : "))
                        break 
                    except ValueError:
                        print("Por favor, insira um valor númerico : ")
                        
                editora = input("Informe qual editora publicou o livro : ")
                area = input("Informe de qual gênero é o livro :")
                
                while True:
                    try:
                        ano = int(input("Informe o ano : "))                        
                        if (ano > ano_atual):
                            print("O ano de lançamento não pode ser maior que o ano atual.")
                        else:
                            break
                    except ValueError:
                        print("Insira um valor valido : ")
                
                while True:
                    try:
                        valor = float(input("Informe qual valor do livro : "))
                        break
                    except ValueError:
                        print("Informe um valor valido, como : 19.90 ")
                
                while True:
                    try:
                        qtd_estoque = int(input("Informe quantos livros serão adicionados ao sistema : "))
                        if (qtd_estoque <= 0):
                            print("Informe um valor inteiro maior que 0 : ")
                        else:
                            break
                    except ValueError:
                        print("Informe um valor inteiro maior que 0 : ")                        
                
                #insere as informações no objeto instanciado
                livro = Livraria(titulo,codigo,editora,area,ano,valor,qtd_estoque)
                livros.append(livro)
            
            case "2":
                if (len(livros) == 0):
                    print("Nehum livro adicionado ainda\n")
                else:
                    livro.infoGeral()
            
            case "3":
                if (len(livros)==0):
                    print("Nenhum livro adicionado até o momento")
                else:
                    pergunta = input("Qual nome do livro que deseja procurar ? ")
                    livro.procurarLivroNome(pergunta)
                
            case "4":
               pergunta = input("Informe a categoria que deseja procurar : ")
               livro.procurarLivroCat(pergunta)
            
            case "5":
                pergunta = float(input("Buscar livros com valor igual ou menor : "))
                livro.procurarLivroPreco(pergunta)
                
            case "6":
                pergunta = int(input("Buscar livro por quantidade em estoque :\n "))
                livro.procurarLivroQtd(pergunta)
                 
            case "7":
                livro.calcularEstoqueTotal()
                print()
            
            case "8":
                livro.cadastrarTxt()
                
                
            case "0":
                run = False
        
            case _:
                print("Por favor escolha uma das oppções disponíveis\n")
    