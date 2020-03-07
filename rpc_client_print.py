import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')



print("================================================== ")

x1= int(input("masukkan x1= "))
x2= int(input("masukkan x2= "))

#Eksekusi
print()
print("Pangkat : ",s.pow(x1,x2))  
print("Tambah  : ",s.add(x1,x2))  
print("Kali    : ",s.mul(x1,x2))  
print("Bagi    : ",s.div(x1,x2))  
print("Kurang  : ",s.sub(x1,x2))  
print("FPB	   : ",s.fpb(x1,x2))

print("==================================================")

# Print semua operasi yang dapat dilakukan
print(s.system.listMethods())