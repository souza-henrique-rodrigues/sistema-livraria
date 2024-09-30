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
            print(f"Titulo : {self.titulo}")
            print(f"codigo : {self.codigo}")
            print(f"editora : {self.editora}")
            print(f"area : {self.area}")
            print(f"ano : {self.ano}")
            print(f"valor: R$ {self.valor}")
            print(f"quantidade em estoque : {self.qtd_estoque}")
            print(f"O valor total em estoque é {self.valor * self.qtd_estoque:2.f} ")
    
    def procurarLivroNome(self,nomeLivro):
        livro_encontrado = False
        for livro in livros:
            if (livro.titulo == nomeLivro):
                print(livro.infoGeral())
                livro_encontrado = True
                break
        if not livro_encontrado:
            print("Livro não encontrado.")
    
    def procurarLivroCat(self,categoria):
        for livro in livros:
            if (livro.area == categoria):
                print(livro.infoGeral())
        if livro not in livros:
            print("Nenhum livro encontrado. ")   
            
    def procurarLivroQtd(self,quantidade):
        for livro in livros:
            if (livro.qtd_estoque == quantidade):
                print(livro.infoGeral())
        if livro not in livros:
            print("Livro não encontrado pela quantidade especificada.")
    
    def procurarLivroPreco(self,preco):
        for livro in livros:
            if (livro.preco == preco):
                print(livro.infoGeral())
        
        if livro not in livros:
            print("Livro não encontrado pelo preço pesquisado.")
    
    def calcularEstoqueTotal(self):
         preco_total = 0
         for livro in livros:
             preco_total += livro.valor * livro.qtd_estoque
         
         print(f"O valor total do estoque é R$ {preco_total:.2f}")
           

if __name__ == "__main__":
    ano_atual = datetime.now().year
    
    livros = []
    run = True
    while (run):
        
        pergunta = input("Qual opção deseja realizar ? \n 1: Cadastrar novo livro\n 2: Listar todos os livros\n 3: Buscar livro por nome\n 4: Buscar livro por categoria\n 5: Buscar livro por preço\n 6: Buscar livro por quantidade em estoque\n 7: Mostrar valor total em estoque\n 0: Encerrar programa ")
            
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
                for livro in livros:
                    print(f"{livro.infoGeral()}")
            
            case "3":
                pergunta = input("Qual nome do livro que deseja procurar ? ")
                livro.procurarLivroNome(pergunta)
                
            case "4":
               pergunta = input("Informe a categoria que deseja procurar : ")
               livro.procurarLivroCat(pergunta)
            
            case "5":
                pergunta = float(input("Buscar livro por preço : "))
                
            case "6":
                pergunta = int(input("Buscar livro por quantidade em estoque : "))
                livro.procurarLivroQtd(pergunta)
                 
            case "7":
                livro.calcularEstoqueTotal()
                
            case "0":
                run = False
        
            case _:
                print("Por favor, insira um valor correspondente")
    