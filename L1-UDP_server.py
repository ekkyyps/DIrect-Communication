import socket

# Sambungkan socket ke port yang sudah ditentukan

# Buat socket UDP
server_address = ('localhost', 10101)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
print('starting up on {} port {}'.format(*server_address))
#(server_address) 

#buat binding ke server
sock.bind((server_address))
while True:
    print('menunggu menerima pesan')
    data, address = sock.recvfrom(90)

    print('Menerima data sebesar {} bytes dari {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address) #kirimkan data
        print('kirim {} bytes kembali ke {}'.format(
            sent, address))