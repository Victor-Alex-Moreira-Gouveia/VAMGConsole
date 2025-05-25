import time
from TerminalCenter import Terminal, RED, YELLOW, END


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