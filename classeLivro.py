class Livro:
    def __init__(self,codigo,titulo,ano,genero,editora,valor,quantidade):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.editora = editora
        self.valor = valor
        self.quantidade = quantidade
    
    
    def __str__(self):
        return f"{self.codigo}\n {self.titulo}\n {self.ano}\n  {self.genero}\n {self.genero}\n  {self.editora}\n  {self.valor}\n {self.quantidade}" 
    
    
    def infoLivro(self):
        print(f"\nCodigo : {self.codigo}")
        print(f"Titulo : {self.titulo}")
        print(f"Ano : {self.ano}")
        print(f"Gênero : {self.genero}")
        print(f"Editora : {self.editora}")
        print(f"Valor R$ : {self.valor}")
        print(f"quantidade : {self.quantidade}\n")        
    
        
        