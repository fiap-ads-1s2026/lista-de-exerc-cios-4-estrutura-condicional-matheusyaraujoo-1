# Lista 4 - Algoritmos Python com Validações

## 📋 Sumário
- [Descrição](#descrição)
- [Como Utilizar](#como-utilizar)
- [Avaliação Automática](#avaliação-automática)
- [Exercícios Implementados](#exercícios-implementados)
  - [Exercício 1 - Média Aritmética](#exercício-1---média-aritmética)
  - [Exercício 2 - Análise de Crédito](#exercício-2---análise-de-crédito)
  - [Exercício 3 - Desempenho Acadêmico](#exercício-3---desempenho-acadêmico)
  - [Exercício 4 - Calculadora Interativa](#exercício-4---calculadora-interativa)
  - [Exercício 5 - Verificação Previdenciária](#exercício-5---verificação-previdenciária)
  - [Exercício 6 - Calculadora de IMC](#exercício-6---calculadora-de-imc)
  - [Exercício 7 - Categoria de Nadador](#exercício-7---categoria-de-nadador)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos de Implementação](#requisitos-de-implementação)
- [Execução Individual](#execução-individual)

---

## 📝 Descrição

Este projeto contém **7 algoritmos em Python** focados em:

- ✅ **Validação robusta de dados de entrada**
- 🔢 **Cálculos matemáticos e lógicos**
- 🎛️ **Estruturas condicionais complexas**
- 💬 **Interface amigável com o usuário**
- ⚡ **Tratamento de erros e exceções**

Cada exercício foi implementado seguindo boas práticas de programação, com classes organizadas e métodos bem definidos.

---

## 🚀 Como Utilizar

### Execução do Programa Principal
```bash
python app.py
```

### Avaliação Automática
```bash
python scripts/grade_python.py ex1
python scripts/grade.sh ex1
```

Modos válidos: `ex1`, `ex2`, `ex3`, `ex4`, `ex5`, `ex6`, `ex7`.

### Execução Individual por Exercício
```bash
python exercicio1.py  # Executa apenas o Exercício 1
python exercicio2.py  # Executa apenas o Exercício 2
# ... e assim por diante
```

---

## 🔍 Avaliação Automática

O autograder simula entradas e valida as saídas dos métodos:

- `Exercicio1.calcular_media_notas()`
- `Exercicio2.analisar_credito()`
- `Exercicio3.calcular_desempenho_academico()`
- `Exercicio4.menu_calculadora()`
- `Exercicio5.verificar_aposentadoria()`
- `Exercicio6.calcular_imc()`
- `Exercicio7.categorizar_nadador()`

---

## 📚 Exercícios Implementados

### Exercício 1 - Média Aritmética

**🎯 Enunciado:**
Crie um algoritmo que receba duas notas escolares e calcule a média aritmética entre elas. É necessário validar os dados de entrada, aceitando apenas valores no intervalo de 0.0 a 10.0. Se qualquer uma das notas estiver fora dessa faixa, exiba uma mensagem de erro e encerre a execução imediatamente.

**📊 Resultado Esperado:**
```
Digite a primeira nota (0.0 a 10.0): 8.5
Digite a segunda nota (0.0 a 10.0): 7.2
Nota 1: 8.5
Nota 2: 7.2
Média aritmética: 7.9
```

**❌ Caso de Erro:**
```
Digite a primeira nota (0.0 a 10.0): 12.0
Digite a segunda nota (0.0 a 10.0): 8.5
ERRO: As notas devem estar no intervalo de 0.0 a 10.0
```

---

### Exercício 2 - Análise de Crédito

**🎯 Enunciado:**
Crie um algoritmo que analise a viabilidade de um crédito financeiro. O sistema deve receber o salário bruto do colaborador e o valor mensal da parcela desejada. Aplique a regra de comprometimento de renda: se a prestação exceder 20% do salário, informe que a solicitação foi negada. Caso o valor esteja dentro do limite, confirme a aprovação.

**📊 Resultado Esperado - Aprovado:**
```
Digite o salário bruto (R$): 5000.00
Digite o valor mensal da parcela desejada (R$): 800.00
Salário bruto: R$ 5000.00
Valor da parcela: R$ 800.00
Comprometimento de renda: 16.0%

SOLICITAÇÃO APROVADA: O valor está dentro do limite permitido
```

**❌ Resultado Esperado - Negado:**
```
Digite o salário bruto (R$): 3000.00
Digite o valor mensal da parcela desejada (R$): 800.00
Salário bruto: R$ 3000.00
Valor da parcela: R$ 800.00
Comprometimento de renda: 26.7%

SOLICITAÇÃO NEGADA: A prestação excede 20% do salário
```

---

### Exercício 3 - Desempenho Acadêmico

**🎯 Enunciado:**
Crie um algoritmo que calcule o desempenho acadêmico que receba as notas de três avaliações. O cálculo deve seguir a regra de média ponderada, onde as duas primeiras notas possuem peso 1 e a terceira possui peso 2. Após o processamento, o programa deve exibir a média final e o status do estudante: "Aprovado" para médias iguais ou superiores a 6.0, e "Reprovado" para valores inferiores.

**📊 Resultado Esperado - Aprovado:**
```
Digite a nota da primeira avaliação (peso 1): 7.0
Digite a nota da segunda avaliação (peso 1): 6.5
Digite a nota da terceira avaliação (peso 2): 8.5

Notas das avaliações:
1ª avaliação (peso 1): 7.0
2ª avaliação (peso 1): 6.5
3ª avaliação (peso 2): 8.5

Média final: 7.6
Status: APROVADO
```

**❌ Resultado Esperado - Reprovado:**
```
Digite a nota da primeira avaliação (peso 1): 4.0
Digite a nota da segunda avaliação (peso 1): 5.0
Digite a nota da terceira avaliação (peso 2): 6.0

Notas das avaliações:
1ª avaliação (peso 1): 4.0
2ª avaliação (peso 1): 5.0
3ª avaliação (peso 2): 6.0

Média final: 5.2
Status: REPROVADO
```

---

### Exercício 4 - Calculadora Interativa

**🎯 Enunciado:**
Crie um algoritmo que apresente um menu interativo com as quatro operações aritméticas fundamentais: adição, subtração, divisão e multiplicação. O sistema deve capturar a escolha do usuário e, em seguida, solicitar dois operandos numéricos para processar o cálculo correspondente e exibir o quociente, produto, soma ou diferença resultante.

**📊 Resultado Esperado:**
```
=== CALCULADORA ====
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Sair

Escolha uma opção (1-5): 1
Digite o primeiro número: 15.5
Digite o segundo número: 8.2

Resultado: 15.5 + 8.2 = 23.7
```

**⚠️ Tratamento de Divisão por Zero:**
```
Escolha uma opção (1-5): 4
Digite o primeiro número: 10
Digite o segundo número: 0

ERRO: Divisão por zero não é permitida!
```

---

### Exercício 5 - Verificação Previdenciária

**🎯 Enunciado:**
Crie um algoritmo que realiza a verificação previdenciária, no qual receba a idade cronológica e o tempo de contribuição (serviço) de um colaborador. O algoritmo deve validar o direito à aposentadoria com base nos seguintes critérios alternativos:

- **Critério por Idade:** Mínimo de 65 anos
- **Critério por Tempo:** Mínimo de 30 anos de serviço  
- **Critério Misto:** Mínimo de 60 anos de idade combinados com 25 anos de serviço

O programa deve emitir um parecer final informando se o trabalhador está apto ou não para o benefício.

**📊 Resultado Esperado - Apto:**
```
Digite a idade cronológica (anos): 62
Digite o tempo de contribuição (anos): 27

Dados do colaborador:
Idade: 62 anos
Tempo de contribuição: 27 anos

Análise dos critérios:
• Critério por Idade (≥65 anos): ✗ NÃO ATENDE
• Critério por Tempo (≥30 anos): ✗ NÃO ATENDE
• Critério Misto (≥60 anos + ≥25 anos serviço): ✓ ATENDE

PARECER: O trabalhador ESTÁ APTO para aposentadoria
```

**❌ Resultado Esperado - Não Apto:**
```
Digite a idade cronológica (anos): 58
Digite o tempo de contribuição (anos): 20

Dados do colaborador:
Idade: 58 anos
Tempo de contribuição: 20 anos

Análise dos critérios:
• Critério por Idade (≥65 anos): ✗ NÃO ATENDE
• Critério por Tempo (≥30 anos): ✗ NÃO ATENDE
• Critério Misto (≥60 anos + ≥25 anos serviço): ✗ NÃO ATENDE

 PARECER: O trabalhador NÃO ESTÁ APTO para aposentadoria

Para se aposentar, é necessário atender pelo menos um dos critérios:
• Completar 7 anos (critério idade)
• Contribuir por mais 10 anos (critério tempo)
• Ou atingir 2 anos de idade e 5 anos de contribuição (critério misto)
```

---

### Exercício 6 - Calculadora de IMC

**🎯 Enunciado:**
Crie um algoritmo que peça o peso (kg) e a altura (m) de uma pessoa. Calcule o Índice de Massa Corporal (IMC) e informe se a pessoa está no peso ideal. (IMC = peso/altura²)

**📊 Resultado Esperado - Peso Ideal:**
```
Digite o peso em kg: 70.5
Digite a altura em metros: 1.75

Dados informados:
Peso: 70.5 kg
Altura: 1.75 m

Índice de Massa Corporal (IMC): 23.0
Classificação: Peso normal
Status: ESTÁ no peso ideal ✓

Referência OMS - Peso ideal: IMC entre 18,5 e 24,9
```

**⚠️ Resultado Esperado - Fora do Peso Ideal:**
```
Digite o peso em kg: 95.0
Digite a altura em metros: 1.70

Dados informados:
Peso: 95.0 kg
Altura: 1.70 m

Índice de Massa Corporal (IMC): 32.9
Classificação: Obesidade
Status: NÃO está no peso ideal

Referência OMS - Peso ideal: IMC entre 18,5 e 24,9
```

---

### Exercício 7 - Categoria de Nadador

**🎯 Enunciado:**
Crie um algoritmo que solicite a idade de um nadador e imprima sua categoria seguindo a lista abaixo:

- **Infantil:** 5 a 10 anos
- **Juvenil:** 11 a 17 anos
- **Sênior:** 18 anos ou mais
- Se a idade for inferior a 5 anos, informe que o atleta não possui categoria definida

**📊 Resultado Esperado - Infantil:**
```
Digite a idade do nadador: 8

Idade informada: 8 anos
Categoria: INFANTIL
Faixa etária: 5 a 10 anos
```

**📊 Resultado Esperado - Juvenil:**
```
Digite a idade do nadador: 15

Idade informada: 15 anos
Categoria: JUVENIL
Faixa etária: 11 a 17 anos
```

**📊 Resultado Esperado - Sênior:**
```
Digite a idade do nadador: 25

Idade informada: 25 anos
Categoria: SÊNIOR
Faixa etária: 18 anos ou mais
```

**⚠️ Idade Insuficiente:**
```
Digite a idade do nadador: 3

Idade informada: 3 anos
Categoria: O atleta não possui categoria definida
Motivo: Idade inferior a 5 anos
```

---

## 📁 Estrutura do Projeto

```
lista4-python/
├── app.py                    # Menu principal interativo
├── exercicio1.py            # Média aritmética de notas
├── exercicio2.py            # Análise de crédito financeiro
├── exercicio3.py            # Desempenho acadêmico
├── exercicio4.py            # Calculadora interativa
├── exercicio5.py            # Verificação previdenciária
├── exercicio6.py            # Calculadora de IMC
├── exercicio7.py            # Categoria de nadador
├── README.md                # Este arquivo
└── scripts/                 # Scripts de avaliação
    ├── grade_python.py
    └── grade.sh


## Requisitos de implementacao
- Use Python 3.6 ou superior
- Mantenha a estrutura de classes
- Use `input()` para entrada de dados
- Use `print()` para saida de dados
- Mantenha os nomes dos metodos esperados pelo autograder
