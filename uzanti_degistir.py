#Bu kod seçilen dizindeki tüm dosyaların uzantısını .abc yapar.Bu kod  true_file.py dosyasını denemek için yazılmıştır.
import os

def degistir(dizin_yolu):
    for dosya_adı in os.listdir(dizin_yolu):
        dosya_yolu = os.path.join(dizin_yolu, dosya_adı)

        if os.path.isfile(dosya_yolu):
            yeni_dosya_adı = dosya_adı.replace(os.path.splitext(dosya_adı)[1], ".abc")
            yeni_dosya_yolu = os.path.join(dizin_yolu, yeni_dosya_adı)

            os.rename(dosya_yolu, yeni_dosya_yolu)
            print(f"{dosya_adı} dosyasının uzantısı değiştirildi.")

# Kullanım örneği:
dizin_yolu = ""
degistir(dizin_yolu)
