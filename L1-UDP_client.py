import socket

# Buat socket UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#tentukan jaringan dan port untuk socket
server_address = ('localhost', 10101)
message = b'Pesan ini akan dikirim ke server untuk diparsing. Hasilnya akan dikembalikan ke client' #definisikan pesan yang akan dikirim

try:

    # Kirim data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, (server_address))

    # Menerima response
    print('waiting to receive')
    data, server = sock.recvfrom(90) #data dapat menerima sejumlah 90
    print('received {!r}'.format(data))

finally:
	# Tutup socket
    print('closing socket')
    sock.close()