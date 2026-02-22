import os
import sys
from ColorSystem import FontColor as FC

"""Sistema principal"""
# Esqueleto do sistema
class Terminal:
    def __init__(self, cmd):
        self.cmd = cmd
        self.default = f"{FC('<(VAMGConsole', 'normal', 'blue')}/{FC('Home', 'normal', 'purple')}{FC(')> ', 'normal', 'blue')}"
        
    def view(self):
        if self.cmd != None:
            return input(self.cmd).lower()
        
        return input(self.default).lower()

    def clear(self):
        AtualOS = sys.platform
        
        try:
            if AtualOS == 'win32':
                os.system('cls')
            elif AtualOS in ('linux', 'darwin'):
                os.system('clear')
            else:
                print(f"{FC('Seu sistema não foi reconhecido por favor de seu feedback', 'normal', 'yellow')}")
                
        except KeyboardInterrupt:
            print(f"{FC('Sistema finalizado a força', 'normal', 'yellow')}")
    
    def help(self):
        print(f"{'-' * 50}")
        print(f"| {FC('help', 'normal', 'cyan')} {FC(' - Listar comandos disponiveis', 'normal', 'white')}{' ' * 13}|")
        print(f"| {FC('version', 'normal', 'cyan')} {FC(' - Exibe as informações do software', 'normal', 'white')}{' ' * 5}|")
        print(f"| {FC('clear', 'normal', 'cyan')} {FC(' - limpa o terminal', 'normal', 'white')}{' ' * 23}|")
        print(f"| {FC('exit', 'normal', 'cyan')} {FC(' - Finaliza o programa', 'normal', 'white')}{' ' * 21}|")
        print(f"| {FC('time', 'normal', 'cyan')} {FC(' - Exibe o horario atual', 'normal', 'white')}{' ' * 19}|")
        print(f"| {FC('list', 'normal', 'cyan')} {FC(' - Lista os softwares disponiveis', 'normal', 'white')}{' ' * 10}|")
        print(f"{'-' * 50}")
        print("")
        
    def version(self):
        # Variaveis
        
        titulo = f"|{' ' * 13}{FC('VAMG Console', 'normal', 'cyan')}{' ' * 23}|"
        dev = f"|{FC(' Desenvolvedor: ', 'normal', 'yellow')}{FC('Victor Alex Moreira Gouveia', 'normal', 'cyan')}{' ' * 5}|"
        version = f"|{FC(' Versão: ', 'normal', 'yellow')}{FC('V0.2.0', 'normal', 'cyan')}{' ' * 33}|"
        data = f"|{FC(' Data de criação: ', 'normal', 'yellow')}{FC('19/03/2025 ', 'normal', 'cyan')}{' ' * 19}|"
        
        print("-"*50)
        print(titulo.center(50, " "))
        print("-"*50)
        
        print(data)
        print(version)  
        print(dev)
        
        print("-"*50)
        print("")