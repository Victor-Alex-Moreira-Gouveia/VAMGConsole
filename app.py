import time
from core.TerminalCenter import Terminal
from core.ColorSystem import FontColor as FC

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
            print(f"{FC('Sistema em construção', 'normal', 'red')}")
        
        elif user_input == 'exit':
            print("Fim de programa")
            print()
            break
        
        else:
            print(f"{FC('Comando não encontrado digite ', 'normal', 'red')}{FC('help', 'normal', 'yellow')}{FC(' para listar comandos', 'normal', 'red')}")
        
except KeyboardInterrupt:
    print(f"\n{FC('Programa finalizado a força', 'normal', 'yellow')}")