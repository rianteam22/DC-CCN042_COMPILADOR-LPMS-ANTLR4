@echo off
:: Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo Python não está instalado ou não foi adicionado ao PATH.
    exit /b
)

:: Configurar ambiente virtual
echo Criando ambiente virtual...
pip install virtualenv
virtualenv .venv

:: Ativar o ambiente virtual
echo Ativando o ambiente virtual...
call .\.venv\Scripts\activate

:: Instalar dependências
echo Instalando dependências...
pip install -r requirements.txt

:: Gerar lexer e parser com ANTLR
echo Gerando arquivos do ANTLR...
antlr4 -o .antlr/ -listener -visitor -Dlanguage=Python3 Gramatica.g4

:: Executar tokens e árvore sintática para input0.txt
echo Executando análise do arquivo input0.txt...
antlr4-parse Gramatica.g4 prog -tokens < input0.txt > output_tokens_input0.txt
antlr4-parse Gramatica.g4 prog -gui < input0.txt

:: Executar tokens e árvore sintática para input1.txt
echo Executando análise do arquivo input1.txt...
antlr4-parse Gramatica.g4 prog -tokens < input1.txt > output_tokens_input1.txt
antlr4-parse Gramatica.g4 prog -gui < input1.txt

:: Finalizar
echo Script concluído. Confira os arquivos de saída!
pause
