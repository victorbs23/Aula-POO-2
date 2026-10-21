class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_mensalidade(self):
        return self.mensalidade

    def get_idade(self):
        return self.idade

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def aumento_mensalidade_valor(self, valor_aumento):
        self.mensalidade = self.mensalidade + valor_aumento

if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    #print('Endereço hexadecimal do objeto 1:', aluno1)

    aluno2 = Aluno('Emily', 1300.00, 17)
    #print('Endereço hexadecimal do objeto 2:', aluno2)

    print('Nome:', aluno1.get_nome())
    print('Mensalidade:', aluno1.get_mensalidade())
    print('Idade:', aluno1.get_idade())

    aluno1.set_nome('Ailton')
    print('\nNome atualizado:', aluno1.get_nome())

    print('\nNome:', aluno2.get_nome())
    print('Mensalidade:', aluno2.get_mensalidade())
    print('Idade:', aluno2.get_idade())

    aluno2.set_nome('Alice')
    print('\nNome atualizado:', aluno2.get_nome())