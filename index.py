import time
from TerminalCenter import Terminal
from ColorSystem import FontColor as FC

try:
    # Aplicação de toda a lógica
    call = Terminal(None) # Defini formato do terminal
    while True:
        user_input = call.view()  # Armazenando o valor retornado por view()
        parametros = user_input.split(" ")
        
        match parametros[0]:
            
            # Comandos gerais do sistema
            case 'help':
                call.help()
            
            case 'clear':
                call.clear()
                
            case 'version':
                call.version()
                
            case 'time':
                print(time.strftime("%H:%M:%S"))
        
            case 'list':
                print(f"{FC('V-Economist', 'normal', 'yellow')} - ainda em criação")
                
            case 'exit':
                print("Fim de programa")
                print()
                break
            
            ### Comandos de seleção de programas internos
            case 'v-economist':
                string_CLI = f"{FC('<(V-Economist', 'normal', 'blue')}/{FC('Home', 'normal', 'purple')}{FC(')> ', 'normal', 'blue')}"
                program_CLI = Terminal(string_CLI)
                
                while True:
                    user_input = program_CLI.view()
                    paraments = user_input.split(" ")
                    
                    match paraments[0]:
                        case 'help':
                            print(f"{FC('Sistema em construção', 'normal', 'red')}")
                            
                        case 'exit':
                            print("Fim de programa")
                            break
                            
                        case _:
                            print(f"{FC('Comando não encontrado digite ', 'normal', 'red')}{FC('help', 'normal', 'yellow')}{FC(' para listar comandos', 'normal', 'red')}")
                                        

            case _:
                print(f"Resultado dos parametros: {parametros}, Input do usuário {user_input}")
                print(f"{FC('Comando não encontrado digite ', 'normal', 'red')}{FC('help', 'normal', 'yellow')}{FC(' para listar comandos', 'normal', 'red')}")
        
except KeyboardInterrupt:
    print(f"\n{FC('Programa finalizado a força', 'normal', 'yellow')}")
