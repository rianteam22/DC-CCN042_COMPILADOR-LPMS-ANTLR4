import sys
from antlr4 import *
from gen.GramaticaLexer import GramaticaLexer
from gen.GramaticaParser import GramaticaParser
from antlr4.tree.Trees import Trees

def main(arquivo_entrada):
    # Ler o arquivo de entrada
    input_stream = FileStream(arquivo_entrada, encoding='utf-8')
    
    # Criar o lexer e o token stream
    lexer = GramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # Criar parser e árvore de parsing
    parser = GramaticaParser(tokens)
    tree = parser.prog()
    
    # Dicionário de mapeamento de tokens
    token_map = {
        -1: 'EOF',
        1: 'PROGRAM',
        2: 'OPEN_BRACKET',
        3: 'CLOSE_BRACKET',
        4: 'COMMA',
        5: 'SEMICOLON',
        6: 'const',
        7: 'ASSIGN',
        8: 'break',
        9: 'PRINT',
        10: 'OP',
        11: 'CLP',
        12: 'input',
        13: 'if',
        14: 'else',
        15: 'while',
        16: 'ADD',
        17: 'SUB',
        18: 'MUL',
        19: 'DIV',
        20: 'EQTO',
        21: 'DIFF',
        22: 'LT',
        23: 'LTE',
        24: 'GT',
        25: 'GTE',
        26: 'NOT',
        27: 'VARTYPE',
        28: 'ID',
        29: 'VALBOOL',
        30: 'VALINT',
        31: 'VALFLOAT',
        32: 'STRING',
        33: 'WS',
        34: 'LINE_COMMENT',
        35: 'COMMENT'
    }
    
    # Preencher o token stream e imprimir os tokens no formato < tipo_token, token >
    tokens.fill()
    '''
    for token in tokens.tokens:
        tipo_token = token_map.get(token.type, "UNKNOWN") # Se o token não estiver no dicionário, retorna "UNKNOWN"
        texto_token = token.text
        print(f'<{tipo_token},{texto_token}>')'''

    # Imprimir a árvore de parsing
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    # Verificar se o nome do arquivo de entrada foi passado como argumento
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_entrada>")
        sys.exit(1)

    # Chamar a função principal com o nome do arquivo de entrada
    main(sys.argv[1])
