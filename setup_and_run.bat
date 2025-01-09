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
antlr4 -o gen/ -listener -visitor -Dlanguage=Python3 Gramatica.g4

:: Finalizar
echo Script concluído. Ambiente pronto para uso.
pause
