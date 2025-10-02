# Trabalho 1: Minimização de Autômatos Finitos

**Alunos:**
* Claudio Meireles (2321070)
* Felipe Dutra (2321017)

## 🎯 Sobre o Projeto

Este trabalho acadêmico, desenvolvido para a disciplina de Teoria da Computação, aborda a aplicação prática do algoritmo de minimização de Autômatos Finitos Determinísticos (AFDs). O objetivo é, a partir de dois autômatos pré-definidos (Autômato C e Autômato G), aplicar as etapas teóricas para encontrar suas versões minimizadas e equivalentes.

O processo de minimização envolve:
1.  **Remoção de Estados Inalcançáveis:** Identificação e exclusão de estados que não podem ser alcançados a partir do estado inicial.
2.  **Remoção de Estados Mortos:** Identificação e exclusão de estados que não podem alcançar nenhum estado final.
3.  **Agrupamento de Estados Equivalentes:** Utilização do algoritmo de particionamento para agrupar estados indistinguíveis até que uma partição estável seja alcançada.

O projeto inclui um relatório detalhado em PDF, uma implementação em Python para simular os autômatos minimizados e uma apresentação de slides em formato web.

## 📁 Estrutura de Arquivos

O projeto está organizado da seguinte forma:

```
Trabalho_1/
│
├── 📄 relatorio/
│   └── Trabalho 1_ Minimização de Autômatos Finitos.pdf  (Relatório completo)
│
├── 💻 code/
│   └── automatos.py                (Script Python para simular os autômatos)
│
├── 🌐 apresentacao_web/
│   ├── index.html                  (Arquivo principal da apresentação)
│   ├── css/style.css               (Estilos da apresentação)
│   └── js/app.js                   (Lógica da apresentação)
│
└── 🖼️ assets/
    ├── Minimizacao_de_Automatos_Demonstracao.mp4 (Vídeo da apresentação)
    ├── automato_c.png              (Diagrama do Autômato C original)
    ├── automato_c_minimizado.png   (Diagrama do Autômato C minimizado)
    ├── automato_g.png              (Diagrama do Autômato G original)
    └── automato_g_minimizado.png   (Diagrama do Autômato G minimizado)
```

## 🚀 Como Executar o Código

O script `automatos.py` permite visualizar as tabelas de transição dos autômatos minimizados, gerar seus diagramas e testá-los interativamente.

#### **Pré-requisitos:**
1.  **Python 3.x** instalado.
2.  **Graphviz:** É necessário instalar o software Graphviz no seu sistema operacional para que os diagramas possam ser gerados. Você pode baixá-lo em [graphviz.org](https://graphviz.org/download/).
3.  **Bibliotecas Python:** Instale as dependências com o pip:
    ```bash
    pip install automata-lib graphviz
    ```

#### **Execução:**
1.  Navegue até a pasta `code`:
    ```bash
    cd Trabalho_1/code
    ```
2.  Execute o script:
    ```bash
    python automatos.py
    ```

O script irá:
* Exibir as tabelas de transição no terminal.
* Iniciar um modo interativo para testar cadeias de caracteres em cada autômato.
* Gerar as imagens dos diagramas (`dfa1_minimizado.png` e `dfa2_minimizado.png`) em uma nova pasta chamada `automatos_minimizados`.

## 🖥️ Como Visualizar a Apresentação

A apresentação de slides foi criada com HTML, CSS e JavaScript e pode ser aberta em qualquer navegador moderno.

1.  Navegue até a pasta `apresentacao_web`.
2.  Abra o arquivo `index.html` diretamente no seu navegador (ex: Chrome, Firefox, Edge).

Você pode navegar pelos slides usando as setas na tela, as setas do teclado ou deslizando a tela em dispositivos móveis.
