# Implementação de Autômatos Finitos

Este projeto implementa uma coleção completa de autômatos finitos (AFDs, AFNs e AFN-ε) utilizando a biblioteca `automata-lib` em Python. O sistema inclui visualização de diagramas, tabelas de transição e testes interativos para fins educacionais.

## Funcionalidades

- **6 Autômatos Implementados**: 2 AFDs, 2 AFNs e 2 AFN-ε
- **Tabelas de Transição**: Visualização completa das transições incluindo ε-transições
- **Testes Automatizados**: Casos de teste predefinidos com validação
- **Modo Interativo**: Interface para testes manuais pelo usuário
- **Diagramas Visuais**: Geração automática de diagramas em PNG
- **Validação Inteligente**: Contagem precisa de padrões e feedback detalhado

## Autômatos Implementados

### Autômatos Finitos Determinísticos (AFD)
1. **Exatamente 4 símbolos**
   - **Alfabeto**: {a, b}
   - **Linguagem**: L = {w ∈ {a,b}* | |w| = 4}
   - **Descrição**: Aceita strings com exatamente 4 caracteres

2. **Começa com "aba"**
   - **Alfabeto**: {a, b}
   - **Linguagem**: L = {w ∈ {a,b}* | w começa com "aba"}
   - **Descrição**: Aceita strings que iniciam com o padrão "aba"

### Autômatos Finitos Não-Determinísticos (AFN)  
3. **Mínimo 3 ocorrências de "ab"**
   - **Alfabeto**: {a, b}
   - **Linguagem**: L = {w ∈ {a,b}* | w possui no mínimo 3 ocorrências de "ab"}
   - **Descrição**: Conta padrões "ab" não-sobrepostos usando estados intermediários

4. **Mínimo 3 a's OU b's OU c's**
   - **Alfabeto**: {a, b, c}
   - **Linguagem**: L = {w ∈ {a,b,c}* | |w|ₐ ≥ 3 ∨ |w|ᵦ ≥ 3 ∨ |w|ₓ ≥ 3}
   - **Descrição**: Usa contadores paralelos com ε-transições para implementar OR lógico

### Autômatos Finitos com ε-transições (AFN-ε)
5. **a's antecedem b's**
   - **Alfabeto**: {a, b}
   - **Linguagem**: L = {a*b*} = {w | w possui símbolos 'a' que antecedem símbolos 'b'}
   - **Descrição**: Implementa a linguagem regular a*b* usando ε-transições

6. **Contém "ab" ou "ba"**
   - **Alfabeto**: {a, b}
   - **Linguagem**: L = {w ∈ {a,b}* | w contém "ab" ∨ w contém "ba"}
   - **Descrição**: Busca não-determinística por qualquer um dos padrões usando ε-transições

## Requisitos

```bash
pip install automata-lib coloraide pygraphviz
```

### Dependências do Sistema
- **Ubuntu/Debian**: `sudo apt-get install graphviz graphviz-dev`
- **macOS**: `brew install graphviz`
- **Windows**: Instalar Graphviz do site oficial

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ClaudioAMF1/Exercicios-Automatos-em-Python.git
cd Exercicios-Automatos-em-Python
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o programa principal:
```bash
python automatos.py
```

O programa executará automaticamente:
1. Criação de cada autômato
2. Geração dos diagramas visuais (arquivos PNG)
3. Exibição das tabelas de transição
4. Execução dos testes predefinidos
5. Modo interativo para testes manuais

## Estrutura dos Arquivos

```
Exercicios-Automatos-em-Python/
├── automatos.py          # Arquivo principal
├── README.md            # Este arquivo
├── requirements.txt     # Lista de dependências
├── diagramas/           # Diagramas gerados
│   ├── afd_4_simbolos.png
│   ├── afd_comeca_aba.png
│   ├── afn_3_ab.png
│   ├── afn_3_abc.png
│   ├── afn_epsilon_ab.png
│   └── afn_epsilon_ab_ou_ba.png
└── .venv/               # Ambiente virtual
```

## Exemplos de Uso

### AFD - Exatamente 4 símbolos
```
Aceita: "abab", "aabb", "aaaa", "bbbb"
Rejeita: "", "a", "ab", "aba", "ababa"
```

### AFN - Mínimo 3 ocorrências de "ab"
```
Aceita: "ababab" (3 ab), "abababab" (4 ab)
Rejeita: "ab" (1 ab), "abab" (2 ab)
```

### AFN-ε - Linguagem a*b*
```
Aceita: "", "aaa", "bbb", "aabb", "aaabbb"
Rejeita: "ba", "aba", "abab", "aabba"
```

## Recursos Técnicos

### Validação de Padrões
O sistema inclui uma função de contagem manual que valida a precisão dos autômatos:
```python
def contar_ocorrencias_ab(string):
    # Conta ocorrências não-sobrepostas de 'ab'
```

### Detecção de ε-transições
As tabelas mostram automaticamente colunas epsilon quando detectadas:
```
Estado         a              b              ε              
q0             {...}          -              {...}          →*
```

### Feedback Detalhado
O modo de teste mostra informações específicas:
```
'ababab': ✓ ACEITA (3 ocorrências de 'ab')
'abab': ✗ REJEITADA (2 ocorrências de 'ab')
```

## Estrutura do Código

### Funções Principais
- `exibir_tabela_transicao()`: Gera tabelas formatadas
- `testar_strings_predefinidas()`: Executa baterias de teste
- `testar_automato_interativo()`: Interface do usuário
- `contar_ocorrencias_ab()`: Validação de padrões

### Organização por Tipo
1. **Definição do autômato** (estados, alfabeto, transições)
2. **Geração do diagrama** visual
3. **Exibição da tabela** de transições
4. **Testes automatizados** com casos predefinidos
5. **Modo interativo** para experimentação

## Casos de Teste

Cada autômato inclui casos de teste abrangentes:
- **Casos positivos**: Strings que devem ser aceitas
- **Casos negativos**: Strings que devem ser rejeitadas  
- **Casos extremos**: String vazia, símbolos únicos
- **Casos inválidos**: Símbolos fora do alfabeto

## Limitações Conhecidas

- Símbolos fora do alfabeto geram erros (comportamento esperado)
- Grandes strings podem afetar a performance de visualização
- Alguns terminais podem não exibir caracteres especiais (ε) corretamente

## Autor

Implementado por **ClaudioAMF1** como material didático para estudo de Autômatos Finitos e Linguagens Formais.

