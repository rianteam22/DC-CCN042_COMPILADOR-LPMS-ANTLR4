# DC-CCN042_COMPILADOR-LPMS-ANTLR4

Desenvolvimento de um compilador para a linguagem LPMS (Linguagem de Programação Muito Simplificada), com foco acadêmico. O projeto é dividido em três etapas: análise léxica, análise sintática/semântica e geração de código intermediário ou executável.

## Descrição do Projeto

Este projeto implementa um compilador para a linguagem LPMS utilizando **ANTLR4** e Python. A gramática da linguagem está descrita no arquivo `Gramatica.g4`.

## Estrutura do Projeto

- **Gramatica.g4**: Arquivo principal contendo a gramática da linguagem LPMS.
- **inputs.txt**: Exemplos de código LPMS para testes.
- **requirements.txt**: Arquivo de dependências para o ambiente virtual.

---

## Configuração e Execução

### 1. Clone o Repositório

Abra o terminal no Windows e clone o projeto do GitHub:

```bash
git clone {link do repositorio}
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
antlr4 -o .antlr/ -listener -visitor -Dlanguage=Python3 Gramatica.g4
```

- **`-o .antlr/`**: Define a pasta de saída para os arquivos gerados.
- **`-listener`** e **`-visitor`**: Geram arquivos adicionais para percorrer a árvore sintática.
- **`-Dlanguage=Python3`**: Define Python como linguagem de destino.

---

### 4. Testar o Compilador

Você pode executar os seguintes comandos para analisar os arquivos de entrada:

- **Exibir Tokens**:
  ```bash
  antlr4-parse Gramatica.g4 prog -tokens < {nome do txt de input} > output_tokens_input.txt
  ```

- **Exibir Parse Tree**:
  ```bash
  antlr4-parse Gramatica.g4 prog -gui < {nome do txt de input}
  ```

Substitua `{nome do txt de input}` pelo nome do arquivo de entrada, por exemplo, `inputs.txt`.

---

### Saída da Parse Tree:
- O comando `-gui` abre uma janela exibindo a árvore sintática abstrata.

---

Aqui está a seção do **README.md** com instruções para usar o script `setup_and_run.bat`:

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

## Estrutura do Projeto

```plaintext
├── Gramatica.g4          # Arquivo com a gramática da linguagem LPMS
├── inputs.txt            # Arquivo de entrada de exemplo
├── requirements.txt      # Dependências para o ambiente virtual
└── README.md             # Documentação do projeto
```

---

## Referências

1. **ANTLR Documentation**: [https://www.antlr.org/](https://www.antlr.org/)
2. Material da disciplina **Compiladores**.

---