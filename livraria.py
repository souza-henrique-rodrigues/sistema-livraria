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
    




if __name__ == "__main__":
    ano_atual = datetime.now().year
    
    
    livros = []
    run = True
    while (run):
        
        pergunta = input("Qual opção deseja realizar ? \n 1: Cadastrar novo cliente\n 2: Listar todos os livros\n 3: Buscar livro por nome\n 4: Buscar livro por categoria\n 5: Buscar livro por preço\n 6: Buscar livro por quantidade em estoque\n 7: Mostrar valor total em estoque\n 0: Encerrar programa ")
            

        match pergunta:

            case "1":
                titulo = input("Informe o nome do livro : ")                
                while True:
                    try: 
                        codigo = int(input("Digite um número: "))
                        break 
                    except ValueError:
                        print("Por favor, insira um valor númerico ")
                        
                editora = input("Informe qual editora publicou o livro : ")
                area = input("Informe de qual gênero é o livro :")
                
                while True:
                    try:
                        ano = int(input("Informe o ano : "))                        
                        if (ano > ano_atual):
                            print("O ano de lancçamento não pode ser maior que o ano atual")
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
                    print(f"A baixo lista de todos livros disponíveis :\n {livro.infoGeral()}  ")
                    print()
            
            case "3":
                print("caso 1")
            
            case "4":
                print("caso 1")
            
            case "5":
                print("caso 1")
            
            case "6":
                print("caso 1")
            
            case "7":
                print("caso 1")
            
            case "0":
                run = False
        
            case _:
                print("")
    