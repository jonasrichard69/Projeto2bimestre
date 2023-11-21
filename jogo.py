import random
from personagem import Personagem, ClienteFrequente

import time

caixa = 0.0



class JogoCafe:
    def __init__(self, resultadotxt):
        self.personagens = [Personagem("Bob Marley"), Personagem("Ana Maria Braga"), Personagem("Regina Cazé"), Personagem("Pablo Vittar"),
                            ClienteFrequente("Padre Marcelo Rossi"), ClienteFrequente("Gustavo Lima"), ClienteFrequente("Thais Carla"), ClienteFrequente("Gloria Groove"),]
        #self.personagens = [Personagem("Bob Marley"), Personagem("Ana Maria Braga"), Personagem("Regina Cazé"), Personagem("Pablo Vittar"),]
        #self.personagensvip = [ClienteFrequente("Padre Marcelo Rossi"), ClienteFrequente("Gustavo Lima"), ClienteFrequente("Thais Carla"), ]
        self.resultado_txt = resultadotxt
        self.dia = 1
        self.caixa = 0.0

    def simular_dia(self):
        personagem = random.choice(self.personagens)
        personagem.definir_humor()
        pedido = personagem.fazer_pedido()
        mensagem = self.criar_mensagem(personagem.humor, pedido)

        if isinstance(personagem, ClienteFrequente):
            print("Cliente frequente, aplicação de 20% de desconto no café! ")
        
        print(f"{personagem.nome}: {mensagem}")

        self.dia += 1

    
    def criar_mensagem(self, humor, pedido):
        mensagens = {
            "feliz": f" 😃 Bom diaaaa, quero um {pedido} por favorzinho! ",
            "bravo": f" 😠 Me dá logo um {pedido}! ",
            "neutro": f" 😐 Oi, me dê um {pedido}, por favor. "
        }
        return mensagens.get(humor, "Não sei o que pedir.")
    
    '''def simular_dia(self):
        escolha_tipo_personagem = random.choice(["comum", "vip"])

        if escolha_tipo_personagem == "comum":
            personagem = random.choice(self.personagens)
        else:
            personagem = random.choice(self.personagensvip)

        personagem.definir_humor()
        pedido = personagem.fazer_pedido()
        mensagem = self.criar_mensagem(personagem.humor, pedido)

        if isinstance(personagem, ClienteFrequente):
            print("Cliente frequente, aplicação de 20% de desconto no café! ")
        
        print(f"{personagem.nome}: {mensagem}")

        self.dia += 1'''

        
    def cobrar_cafe(self, personagem):
        print("Cliente: Quanto custou? 🤔")
        precos = {
            "1": 3.0,
            "2": 3.5,
            "3": 2.0,
        }

        print("1 - café gelado, R$ 3,0")
        print("2 - cappuccino R$ 3,50")
        print("3 - café com leite R$ 2,0")

        escolha_cliente = input("... ")

        if escolha_cliente in precos:
            preco_original = precos[escolha_cliente]

            if personagem.tipo_cliente == "frequente":
                preco_final = personagem.desconto_frequente(preco_original)
                print(f"A sua conta deu: ${preco_final:.2f}")
                self.caixa += preco_final
            else:
                print(f"A sua conta deu: ${preco_original:.2f}")
                self.caixa += preco_original
            
            

            print("Cliente: Valeu! 😎👍")

        else:
            print("Escolha inválida. Não foi possível cobrar.")
    
    def cobraaar_cafe(self, personagem):
        print("Cliente: Quanto custou? 🤔")
        precos = {
            "1": 3.0,
            "2": 3.5,
            "3": 2.0,
        }

        print("1 - café gelado, R$ 3,0")
        print("2 - cappuccino R$ 3,50")
        print("3 - café com leite R$ 2,0")

        escolha_cliente = input("... ")

        if escolha_cliente in precos:
            preco_original = precos[escolha_cliente]
            print("Aplicar desconto?")
            sim_nao = input("s/n ")
            if sim_nao == 's':
                preco_final = preco_original - (preco_original * 0.2)
                print(f"A sua conta deu: ${preco_final:.2f}")
                self.caixa += preco_final
            elif sim_nao == 'n':
                print(f"A sua conta deu: ${preco_original:.2f}")
                self.caixa += preco_original
            
            print("Cliente: Valeu! 😎👍")
        else:
            print("invalido")


    def mostrar_caixa(self):
        print(f"Lucro total: ${self.caixa:.2f}")

    def escrever_resultado(self):
        with open(self.resultado_txt, "a") as file:
            file.write(f"Lucro total neste dia: ${self.caixa:.2f}\n")

    
    @staticmethod
    def somar_lucros_do_arquivo(resultado_txt):
        try:
            with open(resultado_txt, 'r') as arquivo:
                lucros = [float(line.split("$")[1].replace(",", "").strip()) for line in arquivo if "Lucro total" in line]
                total_lucro = sum(lucros)
                return total_lucro
        except FileNotFoundError:
            print(f"O arquivo {resultado_txt} não foi encontrado.")
            return 0
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return 0
            



def precos_cafe():
    precos_cafe = {
        "café gelado": 3.0,
        "cappuccino": 3.5,
        "café com leite": 2.0,
    }

    return precos_cafe

def preparar_cafe():
        print ("Preparando um cafezinho no capricho")
        time.sleep(5)
        print ("O pedido está pronto")
