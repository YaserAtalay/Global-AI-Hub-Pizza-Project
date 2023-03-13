import csv  # csv ve datetime kütüphaneleri kullanımı
from datetime import datetime

an = datetime.now()  # sipariş anı

with open('Menu.txt') as Proje:  # Not defterinde oluşturulmuş bir Menu.txt belgesini
    contents = Proje.read()  # okutuyor.
pizza_fiyatlar = [20, 30, 50, 25]  # Pizza fiyatlarının listesi
sos_fiyatlar = [5, 10, 15, 20, 3, 5]  # Sos fiyatlarının listesi


def main():
    print(contents)  # main() metodu içinde menüyü ekrana yazdırıyor.


main()


class pizza():
    def __init__(self, pizza_int, pizza_adi, fiyat):  # Pizza açıklamaları
        self.pizza_int = pizza_int
        self.pizza_adi = pizza_adi
        self.fiyat = fiyat

    # pizzalar için nesneler
    def klasik(self, pizza_int, pizza_adi, fiyat):
        print(
            f"{pizza_int} no'lu pizzayı seçtiniz. {pizza_adi} : Tarih boyunca yediğiniz en klasik pizza! {fiyat} Türk lirası")

    def margarita(self, pizza_int, pizza_adi, fiyat):
        print(
            f"{pizza_int} no'lu pizzayı seçtiniz. {pizza_adi} : Tarih boyunca yediğiniz en peynirli pizza! {fiyat} Türk lirası")

    def turk_pizza(self, pizza_int, pizza_adi, fiyat):
        print(f"{pizza_int} no'lu pizzayı seçtiniz. {pizza_adi} : Pastırma ve sucuğa doyacaksınız! {fiyat} Türk lirası")

    def sade_pizza(self, pizza_int, pizza_adi, fiyat):
        print(
            f"{pizza_int} no'lu pizzayı seçtiniz. {pizza_adi} : Formunu korumak isteyenler için, minimal pizza. {fiyat} Türk lirası")


secilen_pizza = pizza("pizzaint", "secilen pizza", "fiyatı")


def pizzaint():  # pizza seçimi metodu
    global pizza_int
    pizza_int = int(input("Bir pizza seçiniz. Ekrana sadece numarasını tuşlayınız:"))


pizzaint()


def yanlispizza():  # pizza numarası yanlış tuşlanırsa doğru girdi almak için
    if (pizza_int > 4):  # zorlayan metot
        print("Yanlış girdi. Tekrar deneyin.")
        pizzaint()


yanlispizza()


def secili_pizza(pizza_int):
    if (1 <= pizza_int <= 4):  # 1 ile 4 arasında sayıları kabul eden if yapısı

        if (pizza_int == 1):  # girilen sayı değerine karşılık gelen pizzaya yönlendiren
            secilen_pizza.klasik(1, "Klasik", pizza_fiyatlar[0])  # if ve elif ifadeleri
        elif (pizza_int == 2):
            secilen_pizza.margarita(2, "Margarita", pizza_fiyatlar[1])
        elif (pizza_int == 3):
            secilen_pizza.turk_pizza(3, "Türk Pizza", pizza_fiyatlar[2])
        elif (pizza_int == 4):
            secilen_pizza.sade_pizza(4, "Sade Pizza", pizza_fiyatlar[3])


class decorator():

    def __init__(self, sos_int, sos_adi, sos_fiyat):  # Sos açıklamaları
        self.sos_int = sos_int
        self.sos_adi = sos_adi
        self.sos_fiyat = sos_fiyat

    def zeytin(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : Ege'den topladık getirdik. Leziz! {sos_fiyat} Türk lirası")

    def mantar(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : Zehirli değil. {sos_fiyat} Türk lirası")

    def keci_peyniri(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : En inatçı keçilerden... {sos_fiyat} Türk lirası")

    def et(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : Kolestrolü çıkarmayandan! ;) {sos_fiyat} Türk lirası")

    def sogan(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : Ağzınızı kokutmaz. :) {sos_fiyat} Türk lirası")

    def misir(self, sos_int, sos_adi, sos_fiyat):
        print(f"{sos_int} no'lu sosu seçtiniz. {sos_adi} : Sıkılsa da patlamaz. :O {sos_fiyat} Türk lirası")


secilen_sos = decorator("sosint", "secilen sos", "sos fiyatı")


def sosint():  # sos girdisi için metot
    global sos_int
    sos_int = int(input("Bir sos seçiniz. Ekrana sadece numarasını tuşlayınız:"))


sosint()


def yanlissos():  # sos değeri yanlış girilirse doğru değer girmeye zorlayan metot
    if (sos_int < 11 or sos_int > 16):
        print("Yanlış girdi. Tekrar deneyin.")
        sosint()


yanlissos()


def secili_sos(sos_int):
    if (11 <= sos_int <= 16):  # 11 ile 16 arasında bir sayı girmesini isteyen if yapısı

        if (sos_int == 11):  # girilen sayı değerine karşılık gelen sosa yönlendiren
            secilen_sos.zeytin(11, "Zeytin", sos_fiyatlar[0])  # if ve elif ifadeleri
        elif (sos_int == 12):
            secilen_sos.mantar(12, "Mantar", sos_fiyatlar[1])
        elif (sos_int == 13):
            secilen_sos.keci_peyniri(13, "Keçi Peyniri", sos_fiyatlar[2])
        elif (sos_int == 14):
            secilen_sos.et(14, "Et", sos_fiyatlar[3])
        elif (sos_int == 15):
            secilen_sos.sogan(15, "Soğan", sos_fiyatlar[4])
        elif (sos_int == 16):
            secilen_sos.misir(16, "Mısır", sos_fiyatlar[5])


secili_pizza(pizza_int)
secili_sos(sos_int)


def get_cost():
    global pizza_f
    global sos_f
    global toplam


pizza_f = pizza_int - 1  # listelerin 0 değeriyle başladığı düşünülerek hazırlanan
sos_f = sos_int - 11  # formüller

toplam = pizza_fiyatlar[pizza_f] + sos_fiyatlar[sos_f]  # Seçilen pizza ve sosun
get_cost()
# fiyatlarını toplar
print(f"Seçtiğiniz pizza ve sosun fiyatı toplam {toplam} Türk Lirasıdır.")


# aşağıda kullanıcıya dair bilgiler isteniyor:

def kullanici():  # kullanıcı adının onayı
    global kullanici_adi  # değişkeni dışarda kullanmak için global ifadesi
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    print(f"Kullanıcı adınız: {kullanici_adi} .Onaylıyor musunuz? E/H")
    cevap1 = input()
    cevap1 = cevap1.lower()  # büyük küçük harf duyarlılığını ortadan kaldırmak için tercihen küçük harf
    if (cevap1 == "e"):  # yanıt evetse
        print("İşleminiz devam ediyor.")
    elif (cevap1 == "h"):  # yanıt hayırsa
        print("Tekrar deneyiniz:")
        kullanici()  # metodu tekrar çağırıyor

    else:
        print("Yanlış değer girdiniz.")
        print("Tekrar deneyiniz:", kullanici_adi)
        kullanici()  # metodu tekrar çağırıyor


kullanici()


def kimlik():  # TC kimlik numarasının onayı
    global kullanici_kimligi  # değişkeni dışarda kullanmak için global ifadesi
    kullanici_kimligi = int(input("11 haneli TC kimlik numaranızı giriniz:"))
    if (10000000000 <= kullanici_kimligi <= 99999999999):  # 11 haneli olma şartı
        print(f"Kimlik numaranız: {kullanici_kimligi} .Onaylıyor musunuz? E/H")
        cevap = input()
        cevap = cevap.lower()
        if (cevap == "e"):
            print("İşleminiz devam ediyor.")
        elif (cevap == "h"):
            print("Tekrar deneyiniz:")
            kimlik()

    else:
        print("Yanlış değer girdiniz.")
        print("Tekrar deneyiniz:")
        kimlik()


kimlik()


def kredi():  # Kredi kartı numarasının onayı
    global no_int  # değişkeni dışarda kullanmak için global ifadesi
    global no_str  # değişkeni dışarda kullanmak için global ifadesi
    no_int = int(input("16 haneli kredi kartı numaranızı boşluklar olmadan giriniz:"))
    no_str = str(no_int)
    if (len(no_str) == 16):  # 16 haneli olma şartı len kullanılarak
        print(f"Kredi kartı numaranız: {no_int} Onaylıyor musunuz? E/H")
        cevap2 = input()
        cevap2 = cevap2.lower()
        if (cevap2 == "e"):
            print("İşleminiz devam ediyor.")
        elif (cevap2 == "h"):
            print("Tekrar deneyiniz:")
            kredi()

    else:
        print("Yanlış değer girdiniz.")
        print("Tekrar deneyiniz:")
        kredi()


kredi()


def sifre():  # Şifrenin onayı
    global sifre_str  # değişkeni dışarda kullanmak için global ifadesi
    global no_sifre  # değişkeni dışarda kullanmak için global ifadesi
    sifre_str = input("4 haneli Kredi kartı şifrenizi giriniz:")
    no_sifre = int(sifre_str)
    if (1000 <= no_sifre <= 9999):  # 4 haneli olma şartı
        print(f"Şifreniz: {no_sifre} .Onaylıyor musunuz? E/H")
        cevap3 = input()
        cevap3 = cevap3.lower()
        if (cevap3 == "e"):
            print("İşleminiz devam ediyor.")
        elif (cevap3 == "h"):
            print("Tekrar deneyiniz:")
            sifre()
    else:
        print("Yanlış değer girdiniz.")
        print("Tekrar deneyiniz:")
        sifre()


sifre()

# aşağıda tüm bilgileri veritabanında toplamak için hazırlanan csv uzantılı database dosyası:
with open('Orders_Database.csv', mode='w') as yeni_dosya:  # database
    siparis_bilgisi = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    siparis_bilgisi.writerow(["Kişi", "TC no",
                              "kredi kartı no:", "sifre:", "pizza no:",
                              "sos no:", "toplam fiyat:", "tarih & saat:"])
    siparis_bilgisi.writerow([kullanici_adi, kullanici_kimligi
                                 , no_int, no_sifre, pizza_int, sos_int, toplam, an])
# aşağıda veritabanı oluşturduktan sonra okutma işlemi:
with open('Orders_Database.csv') as yeni_dosya:
    siparis = yeni_dosya.read()
    print(siparis) 