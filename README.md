# DC-CCN042_COMPILADOR-LPMS-ANTLR4

Desenvolvimento de um compilador para a linguagem LPMS (Linguagem de Programação Muito Simplificada), com foco acadêmico. O projeto é dividido em três etapas: análise léxica, análise sintática/semântica e geração de código intermediário ou executável.

## Descrição do Projeto

Este projeto implementa um compilador para a linguagem LPMS utilizando **ANTLR4** e Python. A gramática da linguagem está descrita no arquivo `Gramatica.g4`.

## Estrutura do Projeto

- **Gramatica.g4**: Arquivo principal contendo a gramática da linguagem LPMS.
- **input0.lps** e **input1.lps**: Exemplos de código LPMS para testes.
- **requirements.txt**: Arquivo de dependências para o ambiente virtual.

---

## Configuração e Execução

### 1. Clone o Repositório

Abra o terminal no Windows e clone o projeto do GitHub:

```bash
git clone https://github.com/rianteam22/DC-CCN042_COMPILADOR-LPMS-ANTLR4.git
cd {pasta do repositorio}
```

### 2. Configure o Ambiente Python

Garanta que o Python esteja instalado no sistema e adicionado ao PATH global.

- Verifique a instalação do Python:
  ```bash
  python --version
  ```

- Instale o `virtualenv`:
  ```bash
  pip install virtualenv
  ```

- Crie um ambiente virtual:
  ```bash
  virtualenv {nome desejado}
  ```

- Ative o ambiente virtual:
  ```bash
  .\{nome da venv}\Scripts\activate
  ```

- Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

Agora, o ANTLR está instalado e configurado no ambiente virtual.

---

### 3. Gerar o Lexer e o Parser

Com o ambiente virtual ativado, execute o comando para gerar o lexer e parser no formato Python:

```bash
antlr4 -o gen/ -listener -visitor -Dlanguage=Python3 Gramatica.g4
```

- **`-o gen/`**: Define a pasta de saída para os arquivos gerados.
- **`-listener`** e **`-visitor`**: Geram arquivos adicionais para percorrer a árvore sintática.
- **`-Dlanguage=Python3`**: Define Python como linguagem de destino.

---

### 4. Como Testar o Compilador

Você pode executar os seguintes comandos no cmd para analisar os arquivos de entrada:

- **Exibir Tokens**:
  ```bash
  python main.py {nome do .lps de input}
  ```

Substitua `{nome do .lps de input}` pelo nome do arquivo de entrada, por exemplo, `input0.lps`.

---

## Execução Automática com `setup_and_run.bat`

Para facilitar o processo de configuração e execução, fornecemos um script chamado `setup_and_run.bat`. Ele automatiza as etapas de instalação, configuração do ambiente virtual, geração de arquivos com o ANTLR, e análise dos arquivos de entrada.

### Pré-requisitos
Certifique-se de que:
1. O **Python** está instalado e adicionado ao PATH global.
2. O **ANTLR4** foi baixado e o JAR está acessível no PATH.
   - Consulte [instruções de instalação do ANTLR](https://www.antlr.org/download.html) se necessário.

### Como Executar
1. Navegue até a pasta onde o projeto foi clonado:
   ```cmd
   cd {pasta do repositorio}
   ```

2. Execute o script:
   ```cmd
   setup_and_run.bat
   ```
---

## Referências

1. **ANTLR Documentation**: [https://www.antlr.org/](https://www.antlr.org/)
2. **ANTLR4-TOOL Documentation**: https://github.com/antlr/antlr4-tools
3. Material da disciplina **Compiladores**.

---
