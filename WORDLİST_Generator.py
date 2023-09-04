import random
import datetime
import itertools



print("-" * 80)
print("\n")
print("WordList Generator'a hoş geldiniz")
print('\n')
print("-" * 80)

print("\n\n İşlemler: ")
print("[1] Kelime Öbekli")
print("[2] Karışık")
print('\n')
islem = int(input("Lütfen İşlem Seçiniz: "))

if (islem == 1):
      print("-" * 80)

      nouns = []
      while True:
            kelime = input("\n Değer Giriniz: ")
            if(kelime == "-"):
                  break
            else:
                  nouns.append(kelime)
      print("\n[!] Lütfen Dosya Adresini çift '\' kullanarak yazınız. örn: '\\'")
      adres = input("\n Dosya Adresini Yazınız: ")
      dosya = open(adres, 'w')
      sayi = int(input("\n Kaç Adet Satır Oluşturulsun: "))
      print("-" * 80)
      
      for i in range(sayi):
            random.shuffle(nouns)
            sonuc = "\n".join(nouns)
            dosya.write(sonuc)
            print("\n".join(nouns))

      print("-" * 80)
      print("\n[!] İşlem Tamamlandı...")
if (islem == 2):
      print("-" * 80)
      print("\n[!] Lütfen Dosya Adresini çift '\' kullanarak yazınız. örn: '\\'")
      adres_oku = input("\nLütfen Elemanların Bulunduğu Dosya Adresini Yazın: ")
      dosya_oku = open(adres_oku, 'r')
      elemanlar = str(dosya_oku.read())
      uzunluk = int(input("\n Lütfen Oluşturmak İstediğiniz Şifre Uzunluğunu Giriniz: "))
      adet = int(input("\n Lütfen Oluşturmak İstediğiniz Adedi Giriniz: "))
      print("-" * 80)
      print("\n[!] Lütfen Dosya Adresini çift '\' kullanarak yazınız. örn: '\\'")
      adres_yaz = input("\n Dosya Adresini Yazınız: ")
      dosya_yaz = open(adres_yaz, 'w')
      sifre = ""
      print("-" * 80)
      for i in range(adet):
            
            for i in range(uzunluk):
                  index = random.randrange(len(elemanlar))
                  sifre = sifre + elemanlar[index]
                  
            dosya_yaz.write("\n" + sifre)
            print("\n" + sifre)
            sifre = ""
            
      dosya_oku.close()
      dosya_yaz.close()
      
      
      
            
            
            

      
            

     


