import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",4221))
server.listen()
client,addr=server.accept()
done=False
while not done:
    msg=client.recv(1024).decode()
    if msg=='quit':
        done=True
    else:
        print(msg)
    client.send(input("Message: ").encode())