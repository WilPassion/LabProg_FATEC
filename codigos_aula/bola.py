class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor
    
b = Bola("Amarela", 10, "couro")
print(b.mostraCor())
b.trocaCor("Azul")
print(b.mostraCor())