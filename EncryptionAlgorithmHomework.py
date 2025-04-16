import random
import string
# TR
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
# ENG
# Code Written By Rüzgar Batu Kurt
# This code uses a randomly generated key to encrypt messages provided by the user.
# The input provided by the user is encrypted with the use of a list of characters.
# The key is formed by shuffling the character list in a random order.
# The Key is used to encrypt and decrypt messages in an organised combination
# This code was written in phyton (if that wasnt obvious)
# Will work on any version 3.10.0 and above.
# Im new to phyton and programming in general, please DO NOT question far too beyond the quality of the code, I am aware of the complicated elements.
# Im still learning and developing my skills at this time.
# Most of the language used in this code is turkish, (variables etc.) If you don't know turkish, I recommend using an ai to translate such things.
# I wish you a fun experience,


chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)


print("Anahtar Seçimi:")
print("1. Rastgele bir anahtar oluştur")
print("2. Kendi anahtarını gir")
print("Programdan çıkmak için 3'e basın")

while True: 
    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == "1":
        
        anahtar = chars.copy()
        random.shuffle(anahtar)
        print("Oluşturulan Rastgele Anahtar:")
        print("".join(anahtar))

    elif choice == "2":
        
        anahtar_input = input("Lütfen kendi anahtarınızı giriniz: ")
        if len(anahtar_input) != len(chars):
            print("Hatalı anahtar! Anahtar, karakter kümesiyle aynı uzunlukta olmalıdır.")
            exit()
        anahtar = list(anahtar_input)

    elif choice == "3":
        print("Program kapatılıyor...")
        exit()

    
    mesaj = input("Lütfen şifrelenecek mesajı giriniz: ")
    sifreli_mesaj = ""

    for letter in mesaj:
        index = chars.index(letter)
        sifreli_mesaj += anahtar[index]

    print("Şifreli mesaj: ", sifreli_mesaj)
    print("Orijinal mesaj:", mesaj)

    
    print("\n--- Çözümleme Kısmı ---")
    anahtar_input = input("Lütfen çözümleme için anahtarı giriniz: ")
    if len(anahtar_input) != len(chars):
        print("Hatalı anahtar! Lütfen doğru anahtarı giriniz.")
        exit()

    anahtar = list(anahtar_input)

    sifreli_mesaj = input("Lütfen çözümlenecek mesajı giriniz: ")
    mesaj = ""

    for letter in sifreli_mesaj:
        index = anahtar.index(letter)
        mesaj += chars[index]

    print("Çözümlenmiş mesaj: ", mesaj)
