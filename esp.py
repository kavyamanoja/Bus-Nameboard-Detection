import socket
'''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.4.1', 80))
s.send(str.encode('CROSS'))

msg = s.recv(1024)
print(msg.decode("utf-8"))'''
#decoded_input = client_input.decode("utf8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.4.1', 80))
s.send(str.encode('CROSS'))
flag = True
while flag == True :
    msg = s.recv(1024)
    smsg = str(msg.decode("utf-8"))
    print(smsg)
    if smsg == 'GO':
        flag = False
        print("cross the road")