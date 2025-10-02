# Requisitos: pip install automata-lib graphviz
# O programa Graphviz também deve estar instalado no sistema operativo.

from automata.fa.dfa import DFA
from graphviz import Digraph
import os

# --- FUNÇÕES AUXILIARES ---

def generate_dfa_image(dfa, filename, title="DFA"):
    """Gera e salva uma imagem PNG representando o DFA."""
    dot = Digraph(comment=title, format='png', engine='dot')
    dot.attr(rankdir='LR') 

    # Nó invisível para a seta inicial
    dot.attr('node', shape='none', width='0', height='0')
    dot.node('start', label='')
    
    # Configuração padrão para os nós dos estados
    dot.attr('node', shape='circle', width='0.5', height='0.5')

    for state in dfa.states:
        if state in dfa.final_states:
            dot.node(str(state), str(state), shape='doublecircle')
        else:
            dot.node(str(state), str(state))

    dot.edge('start', str(dfa.initial_state))

    # Agrupa transições entre os mesmos dois estados
    edges = {}
    for from_state, transitions in dfa.transitions.items():
        for symbol, to_state in transitions.items():
            edge_key = (str(from_state), str(to_state))
            if edge_key not in edges:
                edges[edge_key] = []
            edges[edge_key].append(symbol)
    
    for (from_s, to_s), symbols in edges.items():
        label = ", ".join(sorted(symbols))
        dot.edge(from_s, to_s, label=label)
    
    output_folder = "automatos_minimizados"
    output_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_path, exist_ok=True)
    full_path = os.path.join(output_path, filename)
    
    try:
        dot.render(full_path, view=False, cleanup=True)
        print(f"-> Imagem '{filename}.png' gerada em '{output_folder}'")
    except Exception as e:
        print(f"ERRO ao gerar imagem: {e}")
        print("   Certifique-se que o Graphviz está instalado e no PATH do sistema.")

def display_transition_table(dfa, title):
    """Exibe no console uma tabela de transição formatada para o DFA."""
    print(f"\n--- Tabela de Transição para {title} ---")
    
    states_list = sorted(list(dfa.states), key=lambda s: ('z' if 'sink' in str(s) else 'a') + str(s))
    input_symbols_list = sorted(list(dfa.input_symbols))

    header = ["Estado"] + input_symbols_list
    print(f"{header[0]:<10}" + "".join(f"{s:^10}" for s in header[1:]))
    print("-" * (10 + len(input_symbols_list) * 10))

    for state in states_list:
        # Adiciona indicadores de estado inicial e final
        prefix = ""
        if state == dfa.initial_state:
            prefix += "->"
        if state in dfa.final_states:
            prefix += "*"
        
        state_str = f"{prefix}{str(state)}"
        row = f"{state_str:<10}"
        for symbol in input_symbols_list:
            next_state = dfa.transitions.get(state, {}).get(symbol, "-")
            row += f"{str(next_state):^10}"
        print(row)
    print("-" * (10 + len(input_symbols_list) * 10))

def test_dfa_interactively(dfa, title):
    """Inicia um loop para testar sequências de entrada no DFA."""
    print(f"\n--- Teste Interativo para {title} ---")
    while True:
        user_input = input("Digite uma sequência (ou 'sair' para terminar): ").strip()
        if user_input.lower() == 'sair':
            break
        try:
            if dfa.accepts_input(user_input):
                print(f"'{user_input}' -> ACEITA")
            else:
                print(f"'{user_input}' -> REJEITA")
        except Exception as e:
            print(f"Entrada inválida: {e}")
    print("Teste encerrado.")


# --- BLOCO PRINCIPAL DE EXECUÇÃO ---
if __name__ == "__main__":
    
    # --- Processamento do Autômato 1 ---
    # Implementação fiel ao autômato minimizado derivado da análise correta.
    # Mapeamento das classes de equivalência para os novos estados:
    # [q0]     -> 'q0'
    # [q1]     -> 'q1'
    # [q2]     -> 'q2'
    # [q3, q6] -> 'q3q6'
    # [q_sink] -> 'q_sink'
    
    dfa1_minimizado = DFA(
        states={'q0', 'q1', 'q2', 'q3q6', 'q_sink'},
        input_symbols={'a', 'b'},
        transitions={
            'q0':   {'a': 'q1', 'b': 'q2'},
            'q1':   {'a': 'q3q6', 'b': 'q_sink'},
            'q2':   {'a': 'q_sink', 'b': 'q3q6'},
            'q3q6': {'a': 'q3q6', 'b': 'q3q6'},
            'q_sink': {'a': 'q_sink', 'b': 'q_sink'}
        },
        initial_state='q0',
        final_states={'q0', 'q1', 'q3q6'}
    )

    print("\n" + "="*50)
    print("          ANÁLISE DO AUTÔMATO 1        ")
    print("="*50)

    display_transition_table(dfa1_minimizado, "Autômato 1 Minimizado")
    generate_dfa_image(dfa1_minimizado, "dfa1_minimizado", "Autômato 1 Minimizado")
    test_dfa_interactively(dfa1_minimizado, "Autômato 1 Minimizado")

    # --- Processamento do Autômato 2 ---
    # A análise correta mostrou que o autômato (sem o estado inalcançável q6)
    # já é mínimo. A implementação abaixo representa o autômato original
    # tornado completo com a adição de um estado de ralo (q_sink).
    
    dfa2_minimizado = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q_sink'},
        input_symbols={'a', 'b'},
        transitions={
            'q0': {'a': 'q1', 'b': 'q_sink'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q5', 'b': 'q_sink'},
            'q3': {'a': 'q3', 'b': 'q3'},
            'q4': {'a': 'q3', 'b': 'q_sink'},
            'q5': {'a': 'q5', 'b': 'q4'},
            'q_sink': {'a': 'q_sink', 'b': 'q_sink'}
        },
        initial_state='q0',
        final_states={'q1', 'q3'} # Estados finais corretos
    )

    print("\n\n" + "="*50)
    print("          ANÁLISE DO AUTÔMATO 2        ")
    print("="*50)

    display_transition_table(dfa2_minimizado, "Autômato 2 Minimizado")
    generate_dfa_image(dfa2_minimizado, "dfa2_minimizado", "Autômato 2 Minimizado")
    test_dfa_interactively(dfa2_minimizado, "Autômato 2 Minimizado")

    print("\n" + "="*50)
    print("Fim da Análise.")
    print("As imagens foram salvas na pasta 'automatos_minimizados'.")
    print("="*50)
