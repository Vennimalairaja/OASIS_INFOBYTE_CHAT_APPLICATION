import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",4221))
done=False
while not done:
    client.send(input("Message: ").encode())
    msg=client.recv(1024).decode()
    if msg=="quit":
        done=True
    else:
        print(msg)