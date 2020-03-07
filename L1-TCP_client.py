import socket

# Membuat socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Menghubungkan socket ke port server
server_address = ('localhost', 10000)
print('Terhubung dengan jaringan {} dan port {}'.format(*server_address))
sock.connect(server_address) #koneksi socket ke alamat server

try:

    # Kirimkan data
    message = b'Pesan ini dikirimkan dari klient ke server untuk dipecah menjadi potongan dengan ukuran 5 dalam sekali kirim'
    print(''.format(message))
    sock.sendall(message) #kirimkan seluruh pesan

    # Lihat hasil dari server
    amount_received = 0
    amount_expected = len(message)

	#mengecek kondisi potongan apakah sesuai dengan yang dikirimkan kembali oleh server
    while amount_received < amount_expected:
        data = sock.recv(5)#menyimpan data dari variabel received
        amount_received += len(data)
        print('menerima {!r}'.format(data))

finally:
	#tutup socket
    sock.close()