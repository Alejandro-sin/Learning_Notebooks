class caninos:
    def __init__(self, raza, nombre, dueo):
        self.raza = raza,
        self.nombre = nombre,
        self.dueo = dueo

    def ladrar(self):
        print("Wooof wooof")

    def _obedecer(self, dueo):
        if dueo:
            print("Ladrido de obedecimiento")
        else:
            print("Muerdo woof")


lazy = caninos("Lazy", "Lazy","Princesa")

print(lazy.ladrar())