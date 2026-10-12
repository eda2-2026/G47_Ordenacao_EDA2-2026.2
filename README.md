# Organizador de Despesas Pessoais — EDA2

Projeto desenvolvido para a disciplina de **Estruturas de Dados 2 (ED2)**, com foco na aplicação de algoritmos de ordenação utilizando Python.

## Integrantes

| Nome | Matrícula |
|---|---|
| Evellyn de Sousa Rocha | 202045400 |


## Objetivos do projeto

- Implementar algoritmos de ordenação em Python.
- Aplicar conceitos de estruturas de dados e análise de complexidade.
- Comparar o desempenho de diferentes algoritmos para conjuntos de dados de tamanhos variados.
- Desenvolver uma aplicação web simples para demonstrar o funcionamento dos algoritmos.
- Apresentar os resultados de forma visual e acessível.
- 
## Demonstração em vídeo

Vídeo de demonstração: [Inserir link do vídeo aqui]


## Funcionalidades

- **Cadastro de despesas:** registro de uma descrição e de um valor.
- **Listagem de despesas:** visualização dos registros cadastrados em uma tabela.
- **Cálculo do total:** soma dos valores das despesas.
- **Ordenação com Bubble Sort:** organiza as despesas em ordem crescente de valor.
- **Ordenação com Merge Sort:** utiliza a estratégia de divisão e conquista para ordenar os registros.
- **Medição de desempenho:** mede o tempo de execução dos algoritmos para diferentes quantidades de dados.

## Tecnologias utilizadas

- **Python:** implementação dos algoritmos e da lógica da aplicação.
- **Flask:** criação do servidor e integração entre Python e a interface web.
- **HTML5:** estruturação da página.
- **CSS3:** estilização e organização visual da interface.

## Algoritmos de ordenação

### 1. Bubble Sort

O Bubble Sort é um algoritmo de ordenação baseado na comparação de elementos adjacentes. Quando dois elementos estão fora da ordem desejada, suas posições são trocadas.

Esse processo é repetido até que os elementos estejam ordenados.

**Funcionamento:**

1. Percorre a lista comparando elementos vizinhos.
2. Troca os elementos quando estão na ordem incorreta.
3. Repete as passagens até concluir a ordenação.

**Complexidade assintótica:**

| Caso | Complexidade |
|---|---|
| Melhor caso, com implementação otimizada | O(n) |
| Caso médio | O(n²) |
| Pior caso | O(n²) |
| Espaço auxiliar do algoritmo tradicional | O(1) |

Na implementação deste projeto, a lista de despesas é copiada antes da ordenação. Por isso, considerando também essa cópia, o consumo adicional de memória é O(n).

O Bubble Sort é simples de implementar e compreender, mas tende a apresentar baixo desempenho para conjuntos grandes de dados.

### 2. Merge Sort

O Merge Sort utiliza a estratégia de **divisão e conquista**. Em vez de ordenar toda a lista de uma só vez, divide o conjunto em partes menores, ordena essas partes recursivamente e depois combina os resultados.

**Funcionamento:**

1. Verifica se a lista possui zero ou um elemento. Nesse caso, ela já está ordenada.
2. Divide a lista em duas partes.
3. Ordena recursivamente cada metade.
4. Intercala as duas partes ordenadas, formando uma lista final em ordem crescente.

**Complexidade assintótica:**

| Caso | Complexidade |
|---|---|
| Melhor caso | O(n log n) |
| Caso médio | O(n log n) |
| Pior caso | O(n log n) |
| Espaço auxiliar | O(n) |

O Merge Sort apresenta desempenho assintótico mais eficiente para conjuntos maiores de dados. Em contrapartida, utiliza memória adicional para armazenar as listas intermediárias durante a intercalação.

### Comparação entre os algoritmos

| Característica | Bubble Sort | Merge Sort |
|---|---|---|
| Estratégia | Comparações e trocas adjacentes | Divisão e conquista |
| Melhor caso | O(n), com otimização | O(n log n) |
| Caso médio | O(n²) | O(n log n) |
| Pior caso | O(n²) | O(n log n) |
| Memória auxiliar tradicional | O(1) | O(n) |
| Adequação a grandes conjuntos | Menos eficiente | Geralmente mais eficiente |

A notação O descreve como o custo computacional cresce em função da quantidade de elementos, não um tempo fixo em segundos.

## Comparação de desempenho

O projeto também possui uma rotina de comparação que gera despesas de teste com valores aleatórios e mede o tempo de execução de cada algoritmo.

Os tamanhos utilizados são:

- 100 despesas;
- 500 despesas;
- 1.000 despesas;
- 2.000 despesas.

Em uma execução registrada durante o desenvolvimento, foram obtidos os seguintes resultados:

| Quantidade de despesas | Bubble Sort | Merge Sort |
|---:|---:|---:|
| 100 | 0,001428 s | 0,000456 s |
| 500 | 0,039686 s | 0,003582 s |
| 1.000 | 0,165723 s | 0,006029 s |
| 2.000 | 0,700692 s | 0,013881 s |

Nessa execução, o Merge Sort apresentou menor tempo de execução em todos os tamanhos testados. A diferença ficou mais evidente à medida que a quantidade de elementos aumentou.

**Observação:** os valores são resultados de uma execução específica. O tempo medido pode variar de acordo com o computador, o ambiente de execução e os dados utilizados. A comparação deve ser interpretada em conjunto com a análise teórica das complexidades.

## Estrutura do projeto

```text
G01_Ordenacao2_EDA2-2026.2/
├── main.py
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

**Descrição dos arquivos:**

- `main.py`: contém os algoritmos de ordenação e as funcionalidades desenvolvidas inicialmente para o terminal.
- `app.py`: inicializa o servidor Flask, processa o cadastro de despesas e integra os algoritmos à interface web.
- `templates/index.html`: apresenta o painel, o formulário, a tabela de despesas e as opções de ordenação.
- `static/style.css`: define a aparência visual da aplicação.
- `README.md`: documenta os objetivos, os algoritmos, as complexidades e as instruções de execução.

## Como executar o projeto

### Pré-requisitos

- Python instalado.
- pip disponível para instalar as dependências.
- Terminal ou terminal integrado do VS Code.

### 1. Clonar o repositório

```bash
git clone https://github.com/eda2-2026/G01_Ordenacao2_EDA2-2026.2.git
cd G01_Ordenacao2_EDA2-2026.2
```

Se o projeto já estiver na sua máquina, entre diretamente na pasta existente.

### 2. Criar um ambiente virtual (opcional, mas recomendado)

No Windows, usando PowerShell:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o ambiente `.venv` já existir, não é necessário criá-lo novamente.

### 3. Instalar o Flask

Com o ambiente virtual ativado, execute:

```powershell
python -m pip install flask
```

### 4. Iniciar a aplicação web

Na pasta principal do projeto, execute:

```powershell
python app.py
```

### 5. Acessar no navegador

Abra o endereço local:

http://127.0.0.1:5000

O terminal deverá permanecer aberto enquanto a aplicação estiver em execução. Para encerrá-la, pressione `Ctrl + C`.

## Como demonstrar o projeto

Uma demonstração pode seguir esta sequência:

1. Iniciar a aplicação pelo terminal.
2. Abrir o painel no navegador.
3. Mostrar o total e as despesas de exemplo.
4. Cadastrar uma nova despesa e verificar sua inclusão na tabela.
5. Selecionar o Bubble Sort e observar a ordenação.
6. Selecionar o Merge Sort e comparar o resultado.
7. Apresentar a funcionalidade de comparação de desempenho disponível no programa de terminal.

## Considerações sobre o uso de Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio durante o desenvolvimento da aplicação web, principalmente na organização e estruturação da interface, na elaboração dos elementos visuais com HTML e CSS e no auxílio à integração da interface com o código Python.
