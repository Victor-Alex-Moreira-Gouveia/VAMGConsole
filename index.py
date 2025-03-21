import sys
import os
import time

"""Sistema principal"""
# Cores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
END = "\033[0m"
Text_Strong = "\033[1m"
Text_StrongWithUnderline = "\033[4m"
Text_StrongEnd = "\033[0m"


# Esqueleto do sistema
class Terminal:
    def __init__(self):
        self.cmd = f"<({BLUE}VAMGConsole{END}/{PURPLE}Home{END})> "
        
    def view(self):
        return input(self.cmd).lower()  # Corrigido: lower() é um método

    def clear(self):
        AtualOS = sys.platform
        
        try:
            if AtualOS == 'win32':
                os.system('cls')
            elif AtualOS in ('linux', 'darwin'):
                os.system('clear')
            else:
                print(f"{YELLOW}Seu sistema não foi reconhecido por favor de seu feedback{END}")
                
        except KeyboardInterrupt:
            print(f"{YELLOW}Sistema finalizado a força{END}")
    
    def help(self):
        print(f"{'-' * 50}")
        print(f"| {CYAN}help{END} - Listar comandos disponiveis{' ' * 13}|")
        print(f"| {CYAN}version{END} - Exibe as informações do software{' ' * 5}|")
        print(f"| {CYAN}clear{END} - limpa o terminal{' ' * 23}|")
        print(f"| {CYAN}exit{END} - Finaliza o programa{END}{' ' * 21}|")
        print(f"| {CYAN}time{END} - Exibe o horario atual{END}{' ' * 19}|")
        print(f"| {CYAN}list{END} - Lista os softwares disponiveis{END}{' ' * 10}|")
        print(f"{'-' * 50}")
        print("")
        
    def version(self):
        # Variaveis
        titulo = f"|{' ' * 13}{CYAN} VAMG Console {END}{' ' * 21}|"
        dev = f"|{YELLOW} Desenvolvedor: {CYAN}Victor Alex Moreira Gouveia {END}{' ' * 4}|"
        version = f"|{YELLOW} Versão: {CYAN}V0.1.0 {END}{' ' * 32}|"
        data = f"|{YELLOW} Data de criação: {CYAN}19/03/2025 {END}{' ' * 19}|"
        
        print("-"*50)
        print(titulo.center(50, " "))
        print("-"*50)
        
        print(data)
        print(version)  
        print(dev)
        
        print("-"*50)
        print("")
        
try:
    # Aplicação de toda a lógica
    call = Terminal()
    while True:
        user_input = call.view()  # Armazenando o valor retornado por view()
        
        if user_input == 'help':
            call.help()
        elif user_input == 'clear':
            call.clear()
        elif user_input == 'version':
            call.version()
        
        elif user_input == 'time':
            print(time.strftime("%H:%M:%S"))
        
        elif user_input == 'list':
            print(f"{RED}Sistema em construção{END}")
        
        elif user_input == 'exit':
            print("Fim de programa")
            print()
            break
        
        else:
            print(f"{RED}Comando não encontrado digite {YELLOW}'help'{RED} para listar comandos{END}")
        
except KeyboardInterrupt:
    print(f"\n{YELLOW}Programa finalizado a força{END}")