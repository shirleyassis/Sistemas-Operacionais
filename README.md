# Sistemas-Operacionais
# Simulador FIFO de Substituição de Páginas
## Descrição

Este projeto implementa um simulador didático do algoritmo **FIFO (First In, First Out)** para substituição de páginas em sistemas operacionais.

O simulador recebe uma sequência de referências a páginas e a quantidade de frames disponíveis na memória RAM, executando o algoritmo FIFO passo a passo e exibindo:

* Estado da memória após cada acesso;
* Ocorrência de Page Fault ou Hit;
* Total de Page Faults;
* Total de Hits.

O objetivo é demonstrar na prática o funcionamento da gerência de memória virtual estudada na disciplina de Sistemas Operacionais.

---

## Algoritmo Utilizado

### FIFO (First In, First Out)

O algoritmo FIFO remove da memória a página que está há mais tempo carregada.

Características:

* Fácil implementação;
* Baixo custo computacional;
* Não considera o uso recente das páginas;
* Pode sofrer a Anomalia de Bélády.

---

## Estrutura do Projeto

├── simulador.py
└── README.md

---

## Requisitos

* Python 3.8 ou superior

Verificar instalação:

```bash
python --version
```

---

## Como Executar

No terminal:

```bash
python simulador.py
```

ou

```bash
py simulador.py
```

---

## Exemplo de Entrada

```text
Digite a sequência de páginas separadas por espaço:
1 2 3 4 1 2 5 1 2 3 4 5

Digite a quantidade de frames da RAM:
3
```

---

## Exemplo de Saída

=== SIMULAÇÃO FIFO ===

Página 1 -> [1] | PAGE FAULT
Página 2 -> [1, 2] | PAGE FAULT
Página 3 -> [1, 2, 3] | PAGE FAULT
...

=== RESULTADO ===

Total de Page Faults: 9
Total de Hits: 3
```

---

## Conceitos Aplicados

* Sistemas Operacionais
* Memória Virtual
* Paginação
* Page Fault
* Algoritmos de Substituição de Páginas
* FIFO (First In, First Out)

---

## Integrantes

Shirley Rocha de Assis 1
Jardson Yan dos Santos 2

---

## Disciplina

Sistemas Operacionais

Universidade Federal do Oeste do Pará (UFOPA)

2026

