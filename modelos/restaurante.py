class Restaurante:
    # Padrão é "self", mas o Python aceita o "this" ou qualquer outro nome que se queira dar
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Pizzaria')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)