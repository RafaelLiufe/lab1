import socket
import threading

def clt(conn, endereco):
    print(f"{endereco} conectado.")
    try:
        msg = conn.recv(1024).decode('utf-8')
        if msg:
            print(f"Mensagem recebida: {msg}")
            revert = msg[::-1]
            conn.send(revert.encode('utf-8'))
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()
        print(f"{endereco} desconectado.")

def init():
    host = '127.0.0.1'
    porta = 8000
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"Escutando em {host}:{porta}")
    
    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=clt, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    init()