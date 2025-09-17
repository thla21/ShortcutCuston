## ShortcutCuston

Automatize tarefas no Windows com um atalho de teclado personalizado. Este projeto usa `pyautogui` e `keyboard` para, ao pressionar um atalho, abrir o navegador Google Chrome, acessar o Google Meet e entrar na reunião automaticamente. Pressione `Esc` para encerrar o script.

### Principais recursos
- **Atalho padrão**: `Ctrl + Alt + F`
- **Ação padrão**: abre o Chrome, vai para `https://meet.google.com` e confirma a entrada
- **Encerramento**: `Esc`
- **Totalmente personalizável**: edite a função `task()` e/ou o atalho em `main.py`

## Requisitos
- **Sistema**: Windows 10 ou superior
- **Python**: 3.12+
- **Navegador**: Google Chrome instalado e acessível pelo menu Iniciar (nome "chrome")
- Permissões para automação de teclado e mouse (pode exigir executar o terminal como Administrador)

## Instalação

### Opção A) Usando uv (recomendado)
O projeto já contém `pyproject.toml` e `uv.lock`.

```bash
# Instalar o uv (se necessário)
pip install uv

# Sincronizar dependências (cria venv automaticamente)
uv sync
```

### Opção B) Usando pip/venv

```powershell
# Na raiz do projeto
python -m venv .venv
.\.venv\Scripts\activate

# Instalar dependências
pip install --upgrade pip
pip install keyboard pyautogui requests
```

## Uso

### Com uv
```bash
uv run python main.py
```

### Com Python diretamente
```powershell
python main.py
```

Enquanto o script estiver rodando:
- Pressione **Ctrl + Alt + F** para executar a automação (abrir Chrome → Google Meet → entrar).
- Pressione **Esc** para encerrar o script.

## Personalização

Edite `main.py` para alterar o que o atalho faz. Os dois pontos principais são:

```python
def task():
    # Altere os passos de automação aqui
    ...

keyboard.add_hotkey("ctrl+alt+f", task)  # Altere o atalho aqui
```

Exemplos de personalização:
- **Mudar o site**: substitua a URL `https://meet.google.com` por outro endereço.
- **Mudar o navegador**: troque a palavra escrita após abrir o menu iniciar (por exemplo, "edge" ou "firefox").
- **Ajustar tempos**: modifique `time.sleep(...)` para adequar ao desempenho do seu computador.
- **Atalho**: use combinações como `"ctrl+shift+m"`, `"alt+f9"`, etc. Veja a documentação de `keyboard` para nomes de teclas suportados.

## Como funciona

O script:
1. Monitora um atalho com a biblioteca `keyboard`.
2. Quando acionado, usa `pyautogui` para simular teclas:
   - Abre o menu Iniciar, digita "chrome" e confirma (abre o Chrome).
   - Digita a URL do Google Meet e confirma.
   - Aguarda o carregamento e pressiona Enter para entrar na sala.
3. Fica aguardando até que você pressione `Esc` para sair.

## Dicas e solução de problemas

- **Executar como Administrador**: no Windows, `keyboard` e `pyautogui` podem exigir privilégios elevados para capturar/emitir eventos do sistema.
- **Escalas de tela e foco**: a automação depende do foco da janela. Evite mover o mouse/teclado durante a execução e ajuste `time.sleep` se necessário.
- **Chrome no PATH/Iniciar**: certifique-se de que o atalho "chrome" abre o Google Chrome via menu Iniciar. Caso contrário, adapte a sequência (por exemplo, fixando o Chrome na barra de tarefas e usando `win+<n>`).
- **Layouts de teclado**: nomes de teclas podem variar conforme o layout/idioma. Verifique a documentação de `keyboard` e teste combinações.
- **Antivírus/políticas corporativas**: algumas políticas bloqueiam automação de entrada. Pode ser necessário configurar exceções.

## Estrutura do projeto

```
ShortcutCuston/
├─ main.py           # Script principal com a automação e o atalho
├─ pyproject.toml    # Metadados do projeto e dependências
├─ uv.lock           # Lockfile do uv (se usar uv)
└─ README.md         # Este arquivo
```

## Dependências
Definidas em `pyproject.toml`:
- `keyboard`
- `pyautogui`
- `requests` (reservado para usos futuros)

## Boas práticas de segurança
- Evite armazenar senhas em texto digitado automaticamente.
- Revise ações automatizadas antes de usar em ambientes de produção/trabalho.
- Tenha como interromper rapidamente (`Esc`).

## Contribuindo
Contribuições são bem-vindas! Abra uma issue com sugestões/melhorias ou envie um pull request.

## Licença
Defina a licença do projeto conforme sua preferência (por exemplo, MIT). Se desejar, crie um arquivo `LICENSE` na raiz.


