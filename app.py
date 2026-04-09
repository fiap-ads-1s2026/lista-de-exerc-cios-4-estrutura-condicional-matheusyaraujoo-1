from exercicio1 import Exercicio1
from exercicio2 import Exercicio2
from exercicio3 import Exercicio3
from exercicio4 import Exercicio4
from exercicio5 import Exercicio5
from exercicio6 import Exercicio6
from exercicio7 import Exercicio7

def main():
    print("\n--- Exercício 1: Média Aritmética de Duas Notas ---")
    ex1 = Exercicio1()
    ex1.calcular_media_notas()

    print("\n--- Exercício 2: Análise de Viabilidade de Crédito ---")
    ex2 = Exercicio2()
    ex2.analisar_credito()

    print("\n--- Exercício 3: Desempenho Acadêmico ---")
    ex3 = Exercicio3()
    ex3.calcular_desempenho_academico()

    print("\n--- Exercício 4: Calculadora Interativa ---")
    ex4 = Exercicio4()
    ex4.menu_calculadora()

    print("\n--- Exercício 5: Verificação Previdenciária ---")
    ex5 = Exercicio5()
    ex5.verificar_aposentadoria()

    print("\n--- Exercício 6: Calculadora de IMC ---")
    ex6 = Exercicio6()
    ex6.calcular_imc()

    print("\n--- Exercício 7: Categoria de Nadador ---")
    ex7 = Exercicio7()
    ex7.categorizar_nadador()

if __name__ == "__main__":
    main()