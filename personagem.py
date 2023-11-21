import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.humor = "normal"
        self.tipo_cliente = "comum"

    def definir_humor(self):
        probabilidades = ["feliz", "bravo", "neutro"]
        self.humor = random.choice(probabilidades)

    def fazer_pedido(self):
        tipos_cafe = ["café gelado", "cappuccino", "café com leite"]
        cafe_aleatorio = random.choice(tipos_cafe)
        return cafe_aleatorio

class ClienteFrequente(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo_cliente = "frequente"

    def desconto_frequente(self, preco_cafe):
        desconto = 0.2 
        return preco_cafe - (preco_cafe * desconto)

