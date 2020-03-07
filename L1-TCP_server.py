import socket

# Buat socket TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan dengan port socket yang sudah ditentukan
server_address = ('localhost', 10000 ) #tentukan jaringan dan portnya
print(''.format(*server_address)) #tunjukkan terjadi koneksi ke jaringan dan port yang dituju

#terjadi binding ke jaringan dan port yang dituju
sock.bind(server_address)

# Mendengarkan permintaan dari klien
sock.listen(1)

while True: #kondisi server terus mengecek permintaan koneksi
    # Menunggu koneksi
    print('menunggu koneksi')
    connection, client_address = sock.accept()
    try:
        print('tersambung dengan', client_address)

        # Menerima data dengan ukuran tertentu dan mengirimkan kembali
        while True:
            data = connection.recv(5) #tentukan ukuran data yang masuk
            print('Menerima {!r}'.format(data))
            if data:
                print('Mengirimkan kembali ke client')
                connection.sendall(data)
            else:
                print('tidak ada data dari', client_address) #kondisi tidak ada data dari client
                break

    finally:
        # Tutup koneksi yang sudah selesai
        connection.close()
        print("Tutup koneksi saat ini")