import random
from jogo import JogoCafe, preparar_cafe, precos_cafe

resultado_txt = "resultado.txt"
jogo = JogoCafe(resultado_txt)

while True:
    print('Bem-vindo ao Coffee Time')
    print('1 - Começar o jogo')
    print('2 - Sair')
    print('3 - Mostrar Caixa')
    opcao = input('Escolha a opção (1/2): ')

    if opcao == '1':
        print('Iniciando o jogo...:')
        jogo.simular_dia()
        personagem = random.choice(jogo.personagens)
        print('1 - Bom dia, claro, irei preparar o seu pedido // 2 - Tenha mais educação e talvez eu prepare seu pedido // 3 - Ok')
        
           
        opcao1  = input('Escolha a opcao: ')
        if opcao1 == '1':
            print(f' Cliente: Vou ficar esperando 😁😁😍😍😍 ')
            print('Qual opção o cliente escolheu? ')
            print('1 - Café Gelado / 2 - Cappuccino // 3- Café com Leite')
            tipos_cafe = precos_cafe()
            opcao_cafe = int(input(""))
            if opcao_cafe == 1:
                cafe = tipos_cafe.get("Café Gelado")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)

                
                
            elif opcao_cafe == 2:
                cafe = tipos_cafe.get("Cappuccino")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
               
            elif opcao_cafe == 3:
                cafe = tipos_cafe.get("Café com Leite")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
                
            else:
                print("Escolha inválida")
        
        elif opcao1 == '2':
            print(f'Cliente: Opa, colega! Perdoai-me pelo modo bruto, rústico e sistemático o qual usei para o dialeto.😔😔😔😔😔😔')
            print('Qual opção o cliente escolheu? ')
            print('1 - Café Gelado / 2 - Cappuccino // 3- Café com Leite')
            tipos_cafe = precos_cafe()
            opcao_cafe = int(input(""))
            if opcao_cafe == 1:
                cafe = tipos_cafe.get("Café Gelado")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)

                
                
            elif opcao_cafe == 2:
                cafe = tipos_cafe.get("Cappuccino")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
               
            elif opcao_cafe == 3:
                cafe = tipos_cafe.get("Café com Leite")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
                
            else:
                print("Escolha inválida")
            
        
        elif opcao1 == '3':
            print(f'Cliente: Vou ficar no aguardo.👍')
            print('Qual opção o cliente escolheu? ')
            print('1 - Café Gelado / 2 - Cappuccino // 3 - Café com Leite')
            tipos_cafe = precos_cafe()
            opcao_cafe = int(input(""))
            if opcao_cafe == 1:
                cafe = tipos_cafe.get("Café Gelado")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)

                
                
            elif opcao_cafe == 2:
                cafe = tipos_cafe.get("Cappuccino")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
               
            elif opcao_cafe == 3:
                cafe = tipos_cafe.get("Café com Leite")
                preparar_cafe()
                jogo.cobrar_cafe(personagem)
                
            else:
                print("Escolha inválida")


    elif opcao == '2':
        print('Saindo do jogo.')
        jogo.escrever_resultado()
        break

    elif opcao == '3':
        print("1 - Caixa do dia")
        print("2 - Lucro Total")
        opcao_caixa = input("...")
        
        if opcao_caixa == '1':
            jogo.mostrar_caixa()
        elif opcao_caixa == '2':
            total_lucro = jogo.somar_lucros_do_arquivo(jogo.resultado_txt)
            print(f"O total do lucro é: ${total_lucro:.2f}")
        else:
            print("Escolha inválida")
    else:
        print('Opção inválida. Por favor, escolha 1 para começar o jogo ou 2 para sair.')
