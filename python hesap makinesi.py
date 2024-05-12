def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y

print("İşlem Seçenekleri:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    secim = input("Lütfen işlem seçeneğini girin (1/2/3/4): ")

    if secim in ('1', '2', '3', '4'):
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == '2':
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == '3':
            print("Sonuç:", carpma(sayi1, sayi2))
        elif secim == '4':
            print("Sonuç:", bolme(sayi1, sayi2))
        
        devam_et = input("Başka bir hesaplama yapmak ister misiniz? (Evet/Hayır): ")
        if devam_et.lower() != 'evet':
            break
    else:
        print("Geçersiz giriş!")
