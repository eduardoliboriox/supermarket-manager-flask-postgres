class ProdutoService:

    @staticmethod
    def validar(nome, preco):
        if not nome:
            raise ValueError("Nome obrigatório")

        if preco <= 0:
            raise ValueError("Preço inválido")

    @staticmethod
    def normalizar(nome):
        return nome.strip().title()
