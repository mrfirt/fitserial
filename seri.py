import serial
#from serial import serial
from time import sleep
print("""
+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+
|F|I|T| |S|E|R|I|A|L| |C|O|N|S|O|L|E| |V|1|.|0|.|0|
+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+
""")
a=int(input("Lütfen Com Degerinizi Giriniz : "))## Serial com 
ser=serial.Serial(port='com{}'.format(a),baudrate=9600)## if you want change your baudrate


secim=int(input("""Lütfen Cihaz Türü Seçiniz
(1) Cisco
(2) Brocade 
(3) Alcatel
(4) Huawei
"""))
vlan= input("Lütfen Managment  İp adresini Giriniz : ")## Your Managment ip address
subnet=input("Subnet Giriniz : ")## Your Subnet 
gateway=input("Gateway Adresi : ") ## Your Gateway 
sysname=input("Lütfen Hostname  Giriniz : ")## sysname for devices
if secim==1: ## Here Cisco Config
	domain=input("Lütfen Domain adresi Giriniz (cisco için ) : ")## Your Domain For Cisco
	ser.write(str.encode("\n en \n"))
	ser.write(str.encode("config t \n"))
	ser.write(str.encode("\n hostname {}".format(sysname)))
	ser.write(str.encode("\n int vlan 3 \n no shut    ")) ## İf you want you can change here your managment vlan 
	ser.write(str.encode("\n ip address {} {}".format(vlan,subnet)))
	ser.write(str.encode("\n ip domain name {}".format(domain)))
	ser.write(str.encode("\n ip default gateway {}".format(gateway)))## Your Gateway
	ser.write(str.encode("\n crypto key generate rsa \n 1024 \n  "))## here key rsa if you want change
	ser.write(str.encode("\n ip ssh version 2 "))
	ser.write(str.encode("\n end \n write memory \n"))
	print("Config Başarılı Şekilde Atıldı Lütfen Kontrol Ediniz")
	
elif secim==2: ## Here Brocade Config
	ser.write(str.encode("\n vlan 3 \n "))## your managment vlan 
	ser.write(str.encode("\n ip address {} {}  \n exit".format(vlan,subnet)))
	ser.write(str.encode("\n ip default-gateway {}".format(gateway)))
	ser.write(str.encode("\n crypto key generate rsa modulus 1024")) ## Here key rsa if you want change
	ser.write(str.encode("\n end \n write memory"))
elif secim==3 :## here alcatel config 
	ser.write(str.encode("\n system name  {}".format(sysname)))
	ser.write(str.encode("\n vlan 3 enable "))## Your managment vlan 
	ser.write(str.encode("\n ip interface vlan-3 address {} mask {} vlan 3".format(vlan,subnet)))
	ser.write(str.encode("\n ip static-route 0.0.0.0  mask 0.0.0.0 gateway {} ".format(gateway)))
	ser.write(str.encode("\n ssh enable "))
	ser.write(str.encode("\n copy certified working  \n write memory \n copy working certified"))
elif secim==4:
   print("Yapım Aşamasında")


	