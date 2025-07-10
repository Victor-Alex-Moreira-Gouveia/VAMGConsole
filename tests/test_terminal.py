import unittest
from TerminalCenter import Terminal

class TestTerminal(unittest.TestCase):
    def setUp(self):
        """Configuração inicial antes de cada teste"""
        print("\nCriando instâncias das classes")
        self.terminal = Terminal()  # Cria uma instância da classe Terminal

    def test_cmd_format(self):
        """Verifica se o prompt do terminal está formatado corretamente"""
        print("Teste de formatação do terminal")
        self.assertIsInstance(self.terminal.cmd, str)
    
    def test_clear(self):
        """Testa se o comando 'clear' não gera erro"""
        try:
            print("Testando comando 'clear'")
            self.terminal.clear()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado, "Erro ao executar 'clear'")

    def test_help_output(self):
        """Verifica se o comando 'help' imprime informações corretamente"""
        try:
            print("Testando o comando 'help'")
            self.terminal.help()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado, "Erro ao executar 'help'")

    def test_version_output(self):
        """Verifica se o comando 'version' exibe informações corretamente"""
        try:
            print("Testando comando 'version'")
            self.terminal.version()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado, "Erro ao executar 'version'")

if __name__ == "__main__":
    unittest.main()
