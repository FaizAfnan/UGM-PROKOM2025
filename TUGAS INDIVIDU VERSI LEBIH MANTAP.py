import random
import time
import os

angka_kata = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]

def simpan_pity(pity): # FUNGSI UNTUK SIMPAN 
    with open("data_pity.txt", "w") as file:
        file.write(str(pity))

def muat_pity(): # FUNGSI UNTUK MUAT
    if os.path.exists("data_pity.txt"):
        with open("data_pity.txt", "r") as file:
            isi = file.read().strip()
            if isi.isdigit():
                return int(isi)
    return 0 

def mulai_gacha(): # INPUT JUMLAH GACHA 
    while True:
        jumlah_gacha = (input("Masukkan jumlah gacha yang ingin dilakukan (max 10): ")).strip().lower()

        if jumlah_gacha.isdigit(): # KEMUNGKINAN INPUT ANGKA
            jumlah_gacha = int(jumlah_gacha)
            if 1 <= jumlah_gacha <= 10:
                return jumlah_gacha
            elif jumlah_gacha > 10:
                print("Maksimal 10 bang")
                continue
            elif jumlah_gacha < 1:
                print("Minimal 1 gacha bos")
                continue

        found = False
        for i in range(len(angka_kata)): # KEMUNGKINAN INPUT KATA
            if jumlah_gacha == angka_kata[i]:
                jumlah_gacha = i + 1
                found = True
                break
        if found:
            return jumlah_gacha
        else:
            print("Yang bener bos, angka atau kata antara satu sampai sepuluh aja.")
            continue

def proses_gacha(jumlah_gacha, pity): # PROSES GACHA
    while True:
        jenis_item = input("Pilih jenis item yang ingin digacha\n[1] Karakter\n[2] Senjata\n[3] Skin\nPilih salah satu (1-3): ").strip()
        if not jenis_item.isdigit(): # VALIDASI INPUT
            print("Masukkan angka antara 1 sampai 3.\n")
            continue
        jenis_item = int(jenis_item)
        if jenis_item == 1:
            jenis_item = "karakter"
        elif jenis_item == 2:
            jenis_item = "senjata"
        elif jenis_item == 3:
            jenis_item = "skin"
        else:
            print("Hanya ada pilihan 1-3 bos.\n")
            continue
        break

    hasil_gacha = []
    for i in range(jumlah_gacha): # PROSES GACHA PER ITEM
        time.sleep(1)
        print(f"Gacha ke-{i+1} ({jenis_item})...")
        time.sleep(1)
        pity += 1

        if pity >= 90: # BATAS GARANSI PITY
            hasil_gacha.append(f"5 star {jenis_item} (Guarantee pity)")
            print(f"Pity mencapai 90! Kamu dijamin mendapat {jenis_item} 5 star!")
            pity = 0
            simpan_pity(pity)
            continue

        rand = random.randint(1, 100) # PROBABILITAS GACHA
        if rand <= 70:
            hasil_gacha.append(f"3 star {jenis_item}")
            print(f"Kamu mendapat {jenis_item} 3 star.")
        elif rand <= 95:
            hasil_gacha.append(f"4 star {jenis_item}")
            print(f"Kamu mendapat {jenis_item} 4 star.")
        else:
            hasil_gacha.append(f"5 star {jenis_item}")
            print(f"Kamu mendapat {jenis_item} 5 star!")
            pity = 0
            simpan_pity(pity)
            break

    simpan_pity(pity) # SIMPAN PITY TERBARU
    return hasil_gacha, pity


def lanjut_gacha(): # LANJUT GACHA ATAU TIDAK
    for percobaan in range(3):
        jawaban = input("\nMau lanjut gacha lagi? (y/n): ").strip().lower()
        if jawaban in ["y", "ya", "yes"]:
            return True
        elif jawaban in ["n", "no", "tidak"]:
            return False
        else:
            print("Masukkan hanya y atau n.")
    print("Kesempatan input habis.")
    return False

# MULAI PROGRAM 
print("Kesempatan setiap item:")
print("3 star (70%)")
print("4 star (25%)")
print("5 star (5%)")
print("Sistem pity aktif (90x tanpa 5-star = dijamin 5-star)\n")

pity = muat_pity() # MUAT PITY TERAKHIR
print(f"Pity terakhir kamu: {pity}\n") # TAMPILKAN PITY TERAKHIR

while True: # LOOP UTAMA PROGRAM
    jumlah_gacha = mulai_gacha() 
    hasil, pity = proses_gacha(jumlah_gacha, pity)

    print("\nHasil gacha kamu:")
    for i, item in enumerate(hasil):
        print(f"{i+1}. {item}")
    print(f"\nTotal pity sekarang: {pity}")
    simpan_pity(pity)

    if not lanjut_gacha():
        print("\nTerima kasih!.")
        break