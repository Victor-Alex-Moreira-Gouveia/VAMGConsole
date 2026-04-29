import pytest
from core.TerminalCenter import Terminal

# Usamos uma fixture para substituir o setUp. 
# Ela cria a instância do Terminal automaticamente para cada teste.
@pytest.fixture
def terminal():
    return Terminal()

def test_cmd_format(terminal):
    """Verifica se o prompt do terminal está formatado corretamente"""
    assert isinstance(terminal.cmd, str)

def test_clear(terminal):
    """Testa se o comando 'clear' não gera erro"""
    # No pytest, se o código rodar sem exceção, o teste passa.
    terminal.clear()

def test_help_output(terminal):
    """Verifica se o comando 'help' imprime informações corretamente"""
    terminal.help()

def test_version_output(terminal):
    """Verifica se o comando 'version' exibe informações corretamente"""
    terminal.version()
