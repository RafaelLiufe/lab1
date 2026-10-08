import socket
import threading
from datetime import datetime

def clt(conexao, endereco):
    print(f"{endereco} conectado.")
    try:
        msg = conexao.recv(1024).decode('utf-8')
        if msg:
            print(f"Mensagem recebida: {msg}")
            horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conexao.send(horario_atual.encode('utf-8'))
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conexao.close()
        print(f"{endereco} desconectado.")

def init():
    host = '127.0.0.1'
    porta = 8001
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"Escutando em {host}:{porta}")
    
    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=clt, args=(conexao, endereco))
        thread.start()
        print(f"Threads ativas: {threading.active_count() - 1}")

if __name__ == "__main__":
    init()