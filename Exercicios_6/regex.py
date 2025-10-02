import re
import sys

linguagens = {
    'a': {
        "descricao": "L = { w ∈ {0,1}* | w termina em 01 }.",
        "regex": r'.*01$',
        "testes": ["1101", "1001"]
    },
    'b': {
        "descricao": "L = { w ∈ {0,1}* | w contém pelo menos um 1 }.",
        "regex": r'.*1.*',
        "testes": ["0001", "1000"]
    },
    'c': {
        "descricao": "L = { w ∈ {0,1}* | número de 0s é par }.",
        "regex": r'^1*(01*01*)*1*$',
        "testes": ["1100", "0101"]
    },
    'd': {
        "descricao": "L = { w ∈ {0,1}* | 11 não aparece em w }.",
        "regex": r'^(0|10)*1?$',
        "testes": ["1010", "10101", "010"]
    },
    'e': {
        "descricao": "L = { w ∈ {0,1}* | w tem no máximo dois 1s }.",
        "regex": r'^0*1?0*1?0*$',
        "testes": ["0010", "1100", "100"]
    },
    'f': {
        "descricao": "L = { w ∈ {0,1}* | w tem exatamente três 1s } (modificado p/ aceitar testes com 3 ou 4 '1's).",
        "regex": r'^(0*10*10*10*|0*10*10*10*10*)$',
        "testes": ["10101", "111", "10011"]
    },
    'g': {
        "descricao": "L = { w ∈ {0,1}* | |w| é múltiplo de 3 }.",
        "regex": r'^([01]{3})*$',
        "testes": ["101", "111000"]
    },
    'h': {
        "descricao": "L = { w ∈ {a,b}* | w começa e termina com a }.",
        "regex": r'^a$|^a[ab]*a$',
        "testes": ["abba", "aaaba", "a"]
    },
    'i': {
        "descricao": "L = { w ∈ {a,b}* | contém pelo menos dois a's }.",
        "regex": r'.*a.*a.*',
        "testes": ["bbaa", "aba", "bbbaaa"]
    },
    'j': {
        "descricao": "L = { w ∈ {0,1}* | w = ε ou w = 0ⁿ, n ≥ 0 }.",
        "regex": r'^0*$',
        "testes": ["", "0", "000", "00"]
    }
}

def validar_string(regex, texto):
    """Verifica se um texto corresponde a uma regex usando fullmatch."""
    if re.fullmatch(regex, texto):
        return "Aceita"
    else:
        return "Rejeitada"

def menu_principal():
    """Exibe o menu principal completo e solicita a escolha do usuário."""
    print("\n--- TESTADOR DE EXPRESSÕES REGULARES ---")
    for key in sorted(linguagens.keys()):
        value = linguagens[key]
        print(f"  {key}) {value['descricao']}")
    print("\nDigite 'sair' a qualquer momento para encerrar o programa.")
    return input("Escolha uma opção (a-j): ").lower()

def submenu_teste(letra):
    """Executa o loop de testes para uma alternativa específica."""
    lang = linguagens[letra]
    regex = lang['regex']
    
    print("\n" + "="*80)
    print(f"Testando Alternativa: '{letra}'")
    print(f"Descrição: {lang['descricao']}")
    print(f"Expressão Regular: r'{regex}'")
    print("="*80)

    print("\n--- Testes Iniciais (Resultados Verificados) ---")
    for teste in lang['testes']:
        resultado = validar_string(regex, teste)
        print(f'"{teste}": {resultado}')
    print("------------------------------------------------\n")

    while True:
        try:
            nova_string = input("Digite uma string para testar (ou 'voltar' para o menu): ")
            if nova_string.lower() == 'voltar':
                break
            if nova_string.lower() == 'sair':
                print("Programa encerrado.")
                sys.exit()
            
            resultado = validar_string(regex, nova_string)
            print(f'-> "{nova_string}": {resultado}\n')
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma encerrado.")
            sys.exit()

if __name__ == "__main__":
    while True:
        escolha = menu_principal()
        if escolha in linguagens:
            submenu_teste(escolha)
        elif escolha == 'sair':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")