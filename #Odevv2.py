# Odev2



def ogrenciEkleme():
    isim = input("Adınısı Giriniz ")
    soyisim = input("Soyisim Giriniz ")
    list.append(isim + soyisim)
    print("Başarıyla eklendi")


def ogrenciSilme():
    isim = input("Adınızı Giriniz ")
    soyisim = input("Soyisim Giriniz ")
    list.remove(isim + soyisim)
    print("Başarıyla Silindi")


def cokluOgrEkleme():
    no = int(input("Eklenecek Ogrenci Sayısı? "))
    count = 0
    while count < no:
        isim = input("Adınızı Giriniz ")
        soyisim = input("Soyisim Giriniz ")
        list.append(isim + soyisim)
        print("Başarıyla eklendi")


def cokluOgrSilme():
    no = int(input("Silinecek Ogrenci Sayısı?"))
    count = 0
    while count < no:
        isim = input("Adınızı Giriniz ")
        soyisim = input("Soyisim Giriniz ")
        list.remove(isim + soyisim)
        print("Başarıyla Silindi")


def ogrenciBul():
    isim = input("Adınızı Giriniz ")
    soyisim = input("Soyadını Giriniz ")
    if isim + soyisim in list:
        num = list.index(isim + soyisim)
        print(str(isim + soyisim), "Öğrenci Bul ", str(num))
    else:
        print("Tekrar Deneyiniz")

print(""" 
Öğrenci Eklemek İçin --->1
Öğrenci Silmek İçin --->2
Birden Fazla Öğrenci Eklemek İçin --->3 
Birden Fazla Öğrenci Silmek İçin ---->4
Öğrenci Bulmak İçin ----5
""")

while True:
    numara= int(input("Numara Giriniz"))

    if numara ==1:
       ogrenciEkleme()

    elif numara ==2:
        ogrenciSilme

    elif numara ==3:
        cokluOgrEkleme

    elif numara ==4:
        cokluOgrSilme

    elif numara==5:
        ogrenciBul

        break            

    


