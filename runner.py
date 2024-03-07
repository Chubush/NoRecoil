import keyboard
import time
import pyautogui

# Başlatıldığında, duraklatıldığında ve kapatıldığında mesajları yazdıran fonksiyon
def yazdir_durum(mesaj):
    print(mesaj)

# Tam ters hareketi gerçekleştiren fonksiyon
def tam_ters_hareket(yukseklik):
    # Yükseklik verisi alınıyor ve negatifine çevriliyor
    ters_yukseklik = -yukseklik
    # Fareyi ters hareket ettirme
    pyautogui.move(0, ters_yukseklik)

# Dosyadan veri okuyan ve ters hareketi gerçekleştiren fonksiyon
def runner():
    yazdir_durum("Başlatıldı.")
    with open("C:\\Users\\Safa\\Desktop\\recoil_kontrol\\recoil.txt", "r") as dosya:
        # Dosyadaki her satırı oku
        for satir in dosya:
            # Satırı ayır ve X ve Y pozisyonlarını al
            if "Fare Pozisyonu:" in satir:
                pozisyon = satir.strip().split(":")[1].strip()
                x, y = pozisyon.split(", ")
                # Y pozisyonu alınıyor ve tamsayıya çevriliyor
                y = int(y.split("=")[1])
                # Tam ters hareketi gerçekleştir
                tam_ters_hareket(y)
            # "x" tuşuna basıldığında işlemi durdur
            if keyboard.is_pressed("x"):
                yazdir_durum("Duraklatıldı.")
                break

# Programı çalıştırma
if __name__ == "__main__":
    yazdir_durum("Program Başladı.")
    # "x" tuşuna basılı olduğu sürece runner fonksiyonunu çalıştır
    while True:
        if keyboard.is_pressed("x"):
            runner()
            time.sleep(0.1)  # Her iterasyon arasında kısa bir bekleme ekleyerek CPU kullanımını azaltır
        # NumLock tuşuna basıldığında programı tamamen kapat
        if keyboard.is_pressed("num lock"):
            yazdir_durum("Program Kapatıldı.")
            break
