# 🚢 Space Wars

Um jogo de **batalha naval desenvolvido em Python**, onde o jogador deve localizar e destruir as naves inimigas utilizando um número limitado de tiros.
O jogo permite jogar **contra a máquina (computador)** ou **contra outro jogador**.

---

## 🎮 Sobre o projeto

O **Space Wars** é um jogo inspirado no clássico conceito de **Batalha Naval**, adaptado para uma temática espacial.

Cada jogador possui um tabuleiro onde as naves são posicionadas. Durante a partida, o jogador escolhe uma posição para realizar um disparo, utilizando coordenadas como:

```text
A1
B4
C7
```

O objetivo é descobrir onde estão as naves adversárias e acertá-las antes que os seus próprios tiros acabem.

---

## 🚀 Como jogar

Durante o jogo, o jogador deve indicar a posição onde deseja disparar.

Por exemplo:

```text
Digite a posição: A1
```

O jogo verifica a posição escolhida e informa se o disparo:

- 💥 **Acertou uma nave**
- 🌊 **Errou**
- 🎯 **A posição já foi escolhida anteriormente**

O jogador possui uma quantidade limitada de tiros, sendo necessário utilizar as tentativas de forma estratégica para tentar localizar as naves no tabuleiro.

---

## 🗺️ Sistema de coordenadas

As posições do tabuleiro são identificadas utilizando letras e números.

Exemplo:

```text
    1   2   3   4   5
A   ■   ■   ■   ■   ■
B   ■   ■   ■   ■   ■
C   ■   ■   ■   ■   ■
D   ■   ■   ■   ■   ■
E   ■   ■   ■   ■   ■
```

Uma posição como:

```text
A1
```

representa a primeira coluna da primeira linha.

O jogador utiliza essas coordenadas para escolher onde deseja realizar o próximo disparo.

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 📦 Bibliotecas nativas do Python
- 💾 **JSON** para armazenamento de dados
- 💻 Execução através do terminal/console

---

### 📄 Principais arquivos

#### `main.py`

Arquivo principal responsável por iniciar o jogo e controlar o fluxo geral da partida.

#### `funcoes.py`

Contém funções auxiliares utilizadas durante o funcionamento do jogo.

#### `naves.py`

Responsável pela lógica relacionada às naves utilizadas no jogo.

#### `tabuleiro.py`

Contém a lógica relacionada ao tabuleiro, posições e coordenadas utilizadas durante a partida.

#### `save.json`

Arquivo utilizado para armazenar dados relacionados ao jogo.

---

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido para praticar conceitos importantes de programação em Python, como:

- Funções
- Estruturas condicionais
- Estruturas de repetição
- Listas e estruturas de dados
- Manipulação de arquivos
- Leitura e escrita de arquivos JSON
- Organização de código em diferentes módulos
- Criação de sistemas de jogo
- Lógica de turnos
- Validação de entradas do usuário
- Desenvolvimento do modo contra a máquina

---

## 💾 Sistema de salvamento

O projeto possui um arquivo `save.json`, utilizado para guardar informações relacionadas ao estado ou aos dados do jogo.

O formato **JSON** permite armazenar informações de maneira estruturada e facilita a leitura e escrita dos dados pela aplicação.

---

## 📚 Objetivo do projeto

O **Space Wars** foi desenvolvido como um projeto de aprendizagem em **Python**, com o objetivo de colocar em prática conceitos de programação através da criação de um jogo funcional.

Durante o desenvolvimento foram trabalhados conceitos como:

- **Lógica de programação**
- **Modularização**
- **Manipulação de dados**
- **Funções**
- **Estruturas de controle**
- **Validação de entradas**
- **Desenvolvimento de sistemas interativos**

---

## 👨‍💻 Autor

Desenvolvido por **Renan Straquicini**.
