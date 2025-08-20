# 1. Kullanıcıdan adını, yaşını ve boyunu (float) input() ile alınız.
# Bu bilgileri uygun veri tiplerinde değişkenlerde saklayınız ve ekrana anlamlı bir şekilde yazdırınız.
print("1. sorunun cevabı")
name = input("Adınızı giriniz:  ")
surname = input("Soyadınızı giriniz: ")
age = int(input("Yaşınızı giriniz:  "))
height = float(input("Boyunuzu giriniz:  "))

print("KULLANICI BİLGİLERİ")
print("ad:" , name )
print("soyad:" , surname )
print("yaş:" , age )
print("boy:" , height )

#2. Bir öğrencinin notlarını (Matematik, Fizik, Kimya) int tipinde değişkenlere atayın. 
# Ortalamasını float tipinde hesaplayıp ekrana yazdırınız.
print("2. sorunun cevabı")
matematik_notu = 100
fizik_notu = 57
kimya_notu = 75
ortalama = float((matematik_notu + fizik_notu + kimya_notu)/ 3)
print(ortalama)

#3. Bir string değişkeni tanımlayın.
#Bu stringin ilk ve son karakterini, uzunluğunu ve ters çevrilmiş halini ekrana yazdırınız.
print("3. sorunun cevabı")
dersin_konusu = 'veri tipleri'
print(dersin_konusu[0])
print(dersin_konusu[-1])
print(len(dersin_konusu))
print(dersin_konusu[::-1])