import Configs_Colors as Colors
import sys
import os

#Esqueleto do sistema
class Terminal:
    def __init__(self):
        self.cmd = "<(VAMGConsole/Null)> "
        
    def view(self):
        
        return input(self.cmd).lower

    def clear(self):
        AtualOS = sys.platform()
        
        try:
            if (AtualOS == 'win32'):
                os.system('cls')
                
            elif (AtualOS == 'linux'):
                os.system('clear')
                
            elif (AtualOS == 'darwin'):
                os.system('clear')
                
            else:
                print("Seu sistema não foi reconhecido por favor de seu feedback")
                
        except KeyboardInterrupt:
            print("Sistema finalizado a força")
    
    def help(self):
        print("")
        print("help - Listar comandos disponiveis")
        print("version - Exibe as informações do software")    
        print("clear - limpa o terminal")
        
    def version(self):
        # Variaveis
        titulo = f"|{' ' * 13}{Colors.FONT_CIANO} VAMG Console {Colors.END}{' ' * 18}|"
        dev = f"|{Colors.FONT_AMARELO} Desenvolvedor: {Colors.FONT_AZUL}Victor Alex Moreira Gouveia {Colors.END}{' ' * 4}|"
        version = f"|{Colors.FONT_AMARELO} Versão: {Colors.FONT_AZUL}V0.0.1 {Colors.END}{' ' * 35}|"
        data = f"|{Colors.FONT_AMARELO} Data de criação: {Colors.FONT_AZUL}19/03/2025 {Colors.END}{' ' * 19}|"
        
        print("-"*50)
        print(titulo.center(50, " "))
        print("-"*50)
        
        print(data)
        print(version)  
        print(dev)
        
        print("-"*50)
        
# Aplição de toda a lógica
call = Terminal()
try:
    while True:
        cmd = Terminal().view()
        
        if (cmd == 'help'):
            cmd.help()
            
        elif (cmd == 'clear'):
            cmd.clear()
        
        elif (cmd == 'version'):
            cmd.version()
        
        else:
            print("Comando não encontrado digite 'help' para listar comandos")
        
except KeyboardInterrupt:
    print("\n Programa finalizado a força")