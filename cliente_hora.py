import socket

def pedir():
    host = '127.0.0.1'
    porta = 8001
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))
    
    cliente.send("Que horas são, mano???".encode('utf-8'))
    
    r = cliente.recv(1024).decode('utf-8')
    print(f"resposta: {r}")
    
    cliente.close()

if __name__ == "__main__":
    pedir()