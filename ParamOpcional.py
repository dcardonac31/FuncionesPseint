def CalcularAreaRectangulo(base, altura, unidadMedida = ""):
    resultado = str(base * altura) + " " + unidadMedida
    return resultado

if __name__ == "__main__":
    baseRectangulo = float(input("Base: "))
    alturaRectangulo = float(input("Altura: "))
    areaRectangulo = CalcularAreaRectangulo(baseRectangulo, alturaRectangulo)
    print("Área rectángulo: " + areaRectangulo)

    unidadMed = "cm"
    baseRectangulo = float(input("Base: "))
    alturaRectangulo = float(input("Altura: "))
    areaRectangulo = CalcularAreaRectangulo(baseRectangulo, alturaRectangulo, unidadMed)
    print("Área rectángulo: " + areaRectangulo)