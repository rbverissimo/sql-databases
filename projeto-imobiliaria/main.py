from inquilinoDAO import *
from contasInquilinosDAO import *

def main():
    lista = [(110, 100, 2023, 2, 1), (150, 105, 2023, 2, 3), (140, 110, 2023, 2, 4), (140, 110, 2023, 2, 5)]
    inserirNovosRegistrosDeContasInquilinosPorLista(lista)
    buscarTodasContasInquilinos()


if __name__ == "__main__":
    main()
