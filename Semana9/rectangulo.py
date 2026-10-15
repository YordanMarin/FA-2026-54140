class rectangulo:
    def __init__(self):
        self.baase = float(input("\nIngrese la base: "))
        self.altura = float(input("Ingrese la altura: "))

    def area(self)->float:
        return self.baase * self.altura

    def perimetro(self)->float:
        return (2*self.baase) + (2*self.altura)
