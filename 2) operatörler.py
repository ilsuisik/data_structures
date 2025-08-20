#4. Kullanıcıdan iki sayı alınız.
#  Bu sayılar üzerinde toplama, çıkarma, çarpma, bölme ve mod işlemleri yapınız.
print("4. sorunun cevabı")
sayi1 = 27
sayi2 = 11
print(sayi1 + sayi2)
print(sayi1 - sayi2)
print(sayi1 * sayi2)
print(sayi1 / sayi2)
print(sayi1 % sayi2)

#5. Bir öğrencinin ortalaması 50’den büyükse 'Geçti', değilse 'Kaldı' çıktısını veren bir program yazınız. (Karşılaştırma ve mantıksal operatörler kullanılacak.)
print("5. sorunun cevabı")
ortalama = float(input("Öğrencinin ortalamasını giriniz: "))

if ortalama > 50:
    print("Geçti")
else:
    print("Kaldı")

#6. Kullanıcıdan yaşını alınız. Eğer yaş 18’den büyükse 'Ehliyet alabilirsiniz', değilse 'Ehliyet alamazsınız' çıktısı veriniz.
print("6. sorunun cevabı")
yas = int(input("Yaşınızı giriniz: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")


#7. Bir ürünün fiyatını (float) ve indirim oranını (yüzde) alınız. İndirimli fiyatı hesaplayıp ekrana yazdırınız. (Aritmetik operatörler kullanılacak.)
print("7. sorunun cevabı")
fiyat = float(input("Ürünün fiyatını giriniz: "))
indirim_orani = float(input("İndirim oranını (%) giriniz: "))

indirimli_fiyat = fiyat - (fiyat * indirim_orani / 100)
print("İndirimli fiyat:", indirimli_fiyat)



#8. True ve False değerlerini içeren değişkenlerle mantıksal operatörleri (and, or, not) uygulayarak örnekler yapınız ve sonuçlarını ekrana yazdırınız.
print("8. sorunun cevabı")
a = True
b = False

print("a AND b:", a and b)   
print("a OR b:", a or b)    
print("NOT a:", not a)      
print("NOT b:", not b)       