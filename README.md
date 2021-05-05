# UDP İle Rc Araç Kontrolü
Proje, linux tabanlı geliştirme kartları ile otonom araçlarda kullanılmak üzere planlanarak geliştirilmeye başlanmıştır. (Ekim2019)
##.
![alt text](https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/6.jpg)


## Araç üzerinde kullanılan metaryeler
1. Raspberry Pi 3 B+
2. 2 Adet 6V 500Rpm Redüktörlü Mikro DC Motor
3. SG90 RC Mini (9gr) Servo Motor
4. L298N Çift Motor Sürücü Kartı
5. 4 Adet 18650 3000 mAh Pil
6. 2S 18650 Pil Şarj Kartı
7. 7805 Voltaj Regülatör
8. Power Giriş Konnektörü Şase Tip (2.1mm)
9. Hazır Rc Araç Şase Ve Tekerleri

## Sistem Şeması
![alt text](https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/mm.png)

![alt text](https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/Sistem%C5%9Eema.png)

## Araç Fotoğrafları
![alt text](https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/Direksiyon_servo.jpg)

![alt text]https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/MotorS%C3%BCrc%C3%BC_motorGrubu.jpg)

![alt text](https://github.com/aatesyasin/UdpControl_RcCar/blob/main/Aracfoto/PilGrubu.jpg)

## Algoritma Adımları:
1. GamePad ile Oluşturulan sinyaller belirlenen katsayılarla çarpılır.
2. Yeni oluşturulan sinyaller paket haline getirilip, UDP protocol ile alıcıya iletilir.
3. UDP protocol ile iletilen sinyaller alıcı tarafından işlenerek motor sürücü ve motor grubuna işlenir.

## Kullanılan Python Sürüm Ve Paketleri
### WindowsContrellerUDP.py
1. Python 3.6
2. pygame
3. Twisted/socket
### RaspberryAracUdp.py
1. Python 3.6
2. Rpi GPIO
3. Twisted/socket 
