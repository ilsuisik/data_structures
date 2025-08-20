#9. Küçük bir alışveriş sepeti uygulaması yapınız:
# Kullanıcıdan 3 ürünün fiyatını alınız.
# Toplam fiyatı hesaplayınız.
# Eğer toplam fiyat 200 TL’den fazlaysa %10 indirim uygulayınız.
# Son fiyatı ekrana yazdırınız.
print("9. sorunun cevabı")
print("ALIŞVERİŞ SEPETİ UYGULAMASI")
urun1 = float(input("1. ürünün fiyatını giriniz: "))
urun2 = float(input("2. ürünün fiyatını giriniz: "))
urun3 = float(input("3. ürünün fiyatını giriniz: "))

toplam = urun1 + urun2 + urun3

print("Toplam fiyat:", toplam)

if toplam > 200:
    toplam = toplam - (toplam * 10 / 100)  
    print("200 TL'yi geçtiğiniz için %10 indirim uygulandı.")

print("Ödenecek son fiyat:", toplam)


#10. Kullanıcıdan doğum yılını alınız. Bu yıl ile güncel yılı kullanarak yaşını hesaplayınız. Yaşına göre şu mesajlardan birini veriniz:
# 0-12: 'Çocuksunuz'
# 13-17: 'Ergensiniz'
# 18 ve üzeri: 'Yetişkinsiniz'

print("10. sorunun cevabı")
dogum_yili = int(input("Doğum yılınızı giriniz: "))
guncel_yil = 2025  

yas = guncel_yil - dogum_yili
print("Yaşınız:", yas)

if yas >= 0 and yas <= 12:
    print("Çocuksunuz")
elif yas >= 13 and yas <= 17:
    print("Ergensiniz")
elif yas >= 18:
    print("Yetişkinsiniz")
else:
    print("Geçersiz yaş girdiniz!")