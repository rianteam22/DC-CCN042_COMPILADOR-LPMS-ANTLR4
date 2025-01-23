from antlr4 import FileStream, CommonTokenStream
from gen.GramaticaLexer import GramaticaLexer
from gen.GramaticaParser import GramaticaParser
from construtorAST import ASTConstrutor, SemanticError

def main(file_path):
    try:
        lexer = GramaticaLexer(FileStream(file_path, encoding='utf-8'))
        tokens = CommonTokenStream(lexer)
        parser = GramaticaParser(tokens)
        
        tree = parser.prog()

        # Construção da AST
        builder = ASTConstrutor()
        ast = builder.visit(tree)

        # Exibição da árvore sintática abstrata formatada
        print("Árvore Sintática Abstrata (AST):\n")
        print(ast)
    except SemanticError as e:
        print(e)
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python main_AST.py <caminho_do_arquivo.lps>")
    else:
        main(sys.argv[1])
