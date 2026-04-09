import sys
import os
import importlib
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

# Adiciona a raiz do repositório ao path para importar os módulos exercicio*.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

class Autograder:
    
    @staticmethod
    def main(args):
        if len(args) == 0:
            Autograder.fail("Modo nao informado. Use: ex1 | ex2 | ex3 | ex4 | ex5 | ex6 | ex7")
        
        try:
            mode = args[0].strip().lower()
            if mode == "ex1":
                Autograder.test_ex1()
            elif mode == "ex2":
                Autograder.test_ex2()
            elif mode == "ex3":
                Autograder.test_ex3()
            elif mode == "ex4":
                Autograder.test_ex4()
            elif mode == "ex5":
                Autograder.test_ex5()
            elif mode == "ex6":
                Autograder.test_ex6()
            elif mode == "ex7":
                Autograder.test_ex7()
            else:
                Autograder.fail(f"Modo invalido: {mode}")
            
            Autograder.pass_test()
        
        except AssertionError as e:
            Autograder.fail(str(e))
        except Exception as e:
            cause = str(e.__cause__) if e.__cause__ else "sem causa"
            Autograder.fail(f"Erro ao executar avaliacao: {str(e)} | Causa: {cause}")
    
    @staticmethod
    def test_ex1():
        # Teste com notas válidas
        output1 = Autograder.capture_output("exercicio1", "Exercicio1", "calcular_media_notas", "8.5\n7.2")
        Autograder.assert_true("média aritmética: 7.8" in output1.lower() or "media aritmética: 7.8" in output1.lower(), "Deve calcular a média corretamente")

        # Teste com nota inválida
        output2 = Autograder.capture_output("exercicio1", "Exercicio1", "calcular_media_notas", "12.0\n8.5")
        Autograder.assert_true("erro" in output2.lower(), "Deve rejeitar notas fora do intervalo")
    
    @staticmethod
    def test_ex2():
        # Teste aprovação (16% de comprometimento)
        output1 = Autograder.capture_output("exercicio2", "Exercicio2", "analisar_credito", "5000\n800")
        Autograder.assert_true("aprovada" in output1.lower(), "Deve aprovar crédito dentro do limite")

        # Teste reprovação (30% de comprometimento)
        output2 = Autograder.capture_output("exercicio2", "Exercicio2", "analisar_credito", "2000\n600")
        Autograder.assert_true("negada" in output2.lower(), "Deve negar crédito acima de 20%")
    
    @staticmethod
    def test_ex3():
        # Teste aprovação (média >= 6.0)
        output1 = Autograder.capture_output("exercicio3", "Exercicio3", "calcular_desempenho_academico", "7.0\n6.5\n8.5")
        Autograder.assert_true("aprovado" in output1.lower(), "Deve aprovar com média >= 6.0")

        # Teste reprovação (média < 6.0)
        output2 = Autograder.capture_output("exercicio3", "Exercicio3", "calcular_desempenho_academico", "4.0\n5.0\n6.0")
        Autograder.assert_true("reprovado" in output2.lower(), "Deve reprovar com média < 6.0")
    
    @staticmethod
    def test_ex4():
        # Teste adição
        output1 = Autograder.capture_output("exercicio4", "Exercicio4", "menu_calculadora", "1\n10\n5\n5")
        Autograder.assert_true("15" in output1, "Deve calcular soma corretamente")

        # Teste multiplicação  
        output2 = Autograder.capture_output("exercicio4", "Exercicio4", "menu_calculadora", "3\n7\n3\n5")
        Autograder.assert_true("21" in output2, "Deve calcular multiplicação corretamente")
    
    @staticmethod
    def test_ex5():
        # Teste aposentadoria por idade (65 anos)
        output1 = Autograder.capture_output("exercicio5", "Exercicio5", "verificar_aposentadoria", "65\n20")
        Autograder.assert_true("apto" in output1.lower(), "Deve aprovar aposentadoria por idade")

        # Teste não apto
        output2 = Autograder.capture_output("exercicio5", "Exercicio5", "verificar_aposentadoria", "50\n15")
        Autograder.assert_true("não está apto" in output2.lower() or "nao esta apto" in output2.lower(), "Deve negar aposentadoria")
    
    @staticmethod
    def test_ex6():
        # Teste peso ideal (IMC normal)
        output1 = Autograder.capture_output("exercicio6", "Exercicio6", "calcular_imc", "70\n1.75")
        Autograder.assert_true("peso ideal" in output1.lower() or "peso normal" in output1.lower(), "Deve identificar peso ideal")

        # Teste IMC calculado
        output2 = Autograder.capture_output("exercicio6", "Exercicio6", "calcular_imc", "80\n1.80")
        Autograder.assert_true("24.7" in output2, "Deve calcular IMC corretamente")
    
    @staticmethod
    def test_ex7():
        # Teste categoria infantil
        output1 = Autograder.capture_output("exercicio7", "Exercicio7", "categorizar_nadador", "8")
        Autograder.assert_true("infantil" in output1.lower(), "Deve identificar categoria infantil")

        # Teste categoria juvenil
        output2 = Autograder.capture_output("exercicio7", "Exercicio7", "categorizar_nadador", "15")
        Autograder.assert_true("juvenil" in output2.lower(), "Deve identificar categoria juvenil")

        # Teste categoria sênior
        output3 = Autograder.capture_output("exercicio7", "Exercicio7", "categorizar_nadador", "25")
        Autograder.assert_true("sênior" in output3.lower() or "senior" in output3.lower(), "Deve identificar categoria sênior")

        # Teste sem categoria
        output4 = Autograder.capture_output("exercicio7", "Exercicio7", "categorizar_nadador", "3")
        Autograder.assert_true("não possui categoria" in output4.lower() or "nao possui categoria" in output4.lower(), "Deve identificar quando não há categoria definida")
    
    @staticmethod
    def capture_output(module_name, class_name, method_name, input_data):
        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            instance = cls()
            method = getattr(instance, method_name)
            
            # Capturar saída e simular entrada
            output_buffer = StringIO()
            input_lines = input_data.strip().split('\n')
            
            with redirect_stdout(output_buffer):
                with patch('builtins.input', side_effect=input_lines):
                    method()
            
            return output_buffer.getvalue()
        
        except Exception as e:
            cause = str(e.__cause__) if e.__cause__ else "sem causa"
            raise Exception(f"Erro ao executar {class_name}.{method_name}: {str(e)} | Causa: {cause}")
    
    @staticmethod
    def assert_true(condition, message):
        if not condition:
            raise AssertionError(message)
    
    @staticmethod
    def pass_test():
        print("OK!")
    
    @staticmethod
    def fail(message):
        print(f"FAIL: {message}")
        sys.exit(1)

if __name__ == "__main__":
    Autograder.main(sys.argv[1:])