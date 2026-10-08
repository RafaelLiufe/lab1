import socket

def enviar():
    host = '127.0.0.1'
    porta = 8000
    
    clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clt.connect((host, porta))
    
    msg = "Olá, Mundo Distribuído"
    print(f"Enviando: {msg}")
    clt.send(msg.encode('utf-8'))
    
    r = clt.recv(1024).decode('utf-8')
    print(f"Resposta: {r}")
    
    clt.close()

if __name__ == "__main__":
    enviar()