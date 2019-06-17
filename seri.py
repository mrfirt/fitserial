import serial
#from serial import serial

from time import sleep
a=int(input("Lütfen Com Degerinizi Giriniz"))
ser=serial.Serial(port='com{}'.format(a),baudrate=9600)## if you want change your baudrate
print("Merhaba Fit Serial Console Beta V.1.0 Hoşgeldiniz")

secim=int(input("""Lütfen Cihaz Türü Seçiniz
(1) Cisco
(2) Brocade 
(3) Alcatel
(4) Huawei
"""))
vlan= input("Lütfen Managment  İp adresini Giriniz")

subnet=input("Subnet Giriniz")## Your Subnet 
gateway=input("Gateway Adresi") ## Your Gateway 
domain=input("Lütfen Domain Adresini Giriniz")## Your Domain For Cisco
if secim==1: ## Here Cisco Config You Can Change Evrything
	ser.write(str.encode('\n en \n'))
	ser.write(str.encode('config t \n'))
	ser.write(str.encode('\n int vlan 2 \n no shut    ')) ## İf you want you can change here your managment vlan 
	ser.write(str.encode("\n ip address {} {}".format(vlan,subnet)))
	ser.write(str.encode("\n ip domain name {}".format(domain)))
	ser.write(str.encode("\n crypto key generate rsa \n 1024 \n  "))## here key rsa if you want change
	ser.write(str.encode("\n ip ssh version 2 "))
	ser.write(str.encode("\n "))
	
elif secim==2: ## Here Brocade Config
	ser.write(str.encode("\n vlan 2 \n "))
	print(" ")


