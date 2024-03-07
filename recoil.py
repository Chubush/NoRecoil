import keyboard
import pyautogui

# Dosya yolu
dosya_yolu = "C:/Users/Safa/Desktop/recoil_kontrol/recoil.txt"

# X tuşuna basıldığında başlayacak olan fonksiyon
def recoil_kontrol():
    # Dosyayı açma ve yazma modunda açma
    with open(dosya_yolu, "w",encoding="utf-8") as dosya:
        # X tuşuna basıldığında
        keyboard.wait("x")
        dosya.write("Recoil Kontrolü Başladı:\n")
        # Fare hareketlerini takip etme
        kayit_durumu = True
        while True:
            # X tuşuna basıldığında kaydı durdurma
            if keyboard.is_pressed("x"):
                if kayit_durumu:
                    kayit_durumu = False
                    dosya.write("Recoil Kontrolü Durduruldu.\n")
                else:
                    kayit_durumu = True
                    dosya.write("Recoil Kontrolü Devam Ediyor:\n")
            # Fare hareketlerini kaydetme
            if kayit_durumu:
                x, y = pyautogui.position()
                dosya.write(f"Fare Pozisyonu: X={x}, Y={y}\n")
                # Hızlı bir şekilde dosyaya yazmak için bufferı boşalt
                dosya.flush()
            # Programı kapatmak için q tuşuna basılması
            if keyboard.is_pressed("q"):
                break

# Programı çalıştırma
if __name__ == "__main__":
    recoil_kontrol()
