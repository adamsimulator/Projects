import random
import string

# Rüzgar Batu Kurt tarafından yazılmıştır.
# Bu kod, bir mesajı şifrelemek ve çözmek için bir anahtar kullanır.
# Kullanıcıdan alınan mesaj, belirli bir karakter kümesi kullanılarak şifrelenir ve daha sonra çözülür.
# Anahtar, karakter kümesinin karıştırılmasıyla oluşturulur.
# Kullanıcıdan alınan mesaj, anahtar kullanılarak şifrelenir ve daha sonra çözülür.
# Kullanıcıdan alınan anahtar, şifreleme ve çözme işlemlerinde kullanılır.
# Bu kod, Python programlama dilinde yazılmıştır ve temel şifreleme algoritmalarını anlamak için bir örnek teşkil eder.
# Phyton 3.10.0 ve üzeri sürümlerde çalıştırılabilir.
# Phyton ve genel anlamda yazılımda yeniyim, lütfen kodun kalitesini çok fazla sorgulamayın. karışık olduğunun farkındayım.
# Öğrenmeye ve geliştirmeye devam ediyorum.
# Eğlenceli bir deneyim olması dileğiyle.
# :)-------------------------------------------------------------------------------------------------------------------


chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)

# Anahtar oluşturma
anahtar = chars.copy()
random.shuffle(anahtar)

# Anahtarı ekrana yazdırma
print("Anahtar:")
print("".join(anahtar))

# Şifreleme Kısmı
mesaj = input("Lütfen şifrelenecek mesajı giriniz: ")
sifreli_mesaj = ""

for letter in mesaj:
    index = chars.index(letter)
    sifreli_mesaj += anahtar[index]

print("Şifreli mesaj: ", sifreli_mesaj)
print("Orijinal mesaj:", mesaj)

# Çözümleme Kısmı
print("\n--- Çözümleme Kısmı ---")
anahtar_input = input("Lütfen çözümleme için anahtarı giriniz: ")
if len(anahtar_input) != len(chars):
    print("Hatalı anahtar! Lütfen doğru anahtarı giriniz.")
    exit()

anahtar = list(anahtar_input)  # Kullanıcıdan alınan anahtarı kullan

sifreli_mesaj = input("Lütfen çözümlenecek mesajı giriniz: ")
mesaj = ""

for letter in sifreli_mesaj:
    index = anahtar.index(letter)
    mesaj += chars[index]

print("Çözümlenmiş mesaj: ", mesaj)