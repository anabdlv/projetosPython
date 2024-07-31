from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # um metodo de classe para criar um objeto Pessoa atraves do ano de nascimento
		# permite o usuario passar ano de nasc ao inves de idade
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    # metodo estático: verificar se é maior de idade

    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18


pessoa1 = Pessoa('Maria', 26) #passando idade
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006) #chamando o metodo p/ passar apenas o ano
print(pessoa1.idade)
print(pessoa2.idade)
# imprimir resultado

print(Pessoa.ehMaiorIdade(17))