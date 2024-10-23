def criar_mult(mult):
    def multiplicar(numero):
        return numero * mult
    return multiplicar

duplicar = criar_mult(2)
triplicar = criar_mult(3)
