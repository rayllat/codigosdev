#!/usr/bin/env python3

## ---------- AULA DE COMUNICACAO ENTRE APLICACOES ------------------------
# Para rodar o codigo, da o comando em dois terminais diferentes: 
# python .\udp_relogio.py servidor
# python .\udp_relogio.py cliente

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

# ----------- SERVIDOR -----------
def servidor(porta):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria o socket
    # port = random.randint(1024, 65535) -- Escolher uma porta aleatória (ajuste o intervalo se necessário)
    server_socket.bind(('localhost', porta)) #Vincula IP e porta 1060 ao servidor
    print(f"Servidor de tempo UDP iniciado na porta {porta}")


    while True:
        data, address = server_socket.recvfrom(1024) #Recebe dados e o endereco do cliente        
        hora_atual = datetime.now().strftime("%d/%m/%Y - %H:%M:%S") # Obtem hora atual e formata
        server_socket.sendto(hora_atual.encode(), address) # Envia hora para cliente
        

# ----------- CLIENTE ------------

def cliente(porta):
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria socket
    cliente_socket.sendto(b'',('localhost', porta)) # Envia mensagem vazia para servidor
    data, _ = cliente_socket.recvfrom(MAX_BYTES) # Recebe hora atual
    print("Hora recebida do servidor >>>> ", data.decode()) # Imprime hora atual

# ----------- MAIN -----------
# Permite escolher entre servidor e cliente e chama a funcao escolhida
if __name__ == '__main__':
    choices = {'cliente': cliente, 'servidor': servidor}
    parser = argparse.ArgumentParser(description='Enviar e receber UDP localmente')
    parser.add_argument('regra', choices=choices, help='Qual regra sera desempenhada.')
    parser.add_argument('-p', metavar='PORTA', type=int, default=1060, help='Porta UDP (padrao: 1060)')
    args = parser.parse_args()
    function = choices[args.regra]
    function(args.p)