import random
import time

angka_kata = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]

def mulai_gacha():
    while True:
        jumlah_gacha = (input("Masukkan jumlah gacha yang ingin dilakukan (max 10): ")).strip().lower()

        # Jika input angka
        if jumlah_gacha.isdigit():
            jumlah_gacha = int(jumlah_gacha)
            if 1 <= jumlah_gacha <= 10:
                return jumlah_gacha
            elif jumlah_gacha > 10:
                print("Kakean to bos, maksimal 10")
                continue
            elif jumlah_gacha < 1:
                print("Minimal 1 gacha bos")
                continue

        # Jika input string (contoh: 'dua', 'tiga')
        found = False
        for i in range(len(angka_kata)):
            if jumlah_gacha == angka_kata[i]:
                jumlah_gacha = i + 1
                found = True
                break
        if found:
            return jumlah_gacha
        else:
            print("Arep gacha ora jane?")
            continue

def proses_gacha(jumlah_gacha, pity):
    hasil_gacha = []
    berhenti_dini = False  # tambahkan flag untuk cek jika user stop di tengah

    for i in range(jumlah_gacha):
        time.sleep(1)
        print(f"Gacha ke-{i+1}...")
        time.sleep(1)
        pity += 1

        if pity >= 90:
            hasil_gacha.append("5 star (Guarantee pity)")
            print("Pity mencapai 90! Kamu dijamin mendapat item 5 star!")
            pity = 0
            continue

        rand = random.randint(1, 100)
        if rand <= 70:
            hasil_gacha.append("3 star")
            print("Selamat! Kamu mendapatkan item 3 star!")
        elif rand <= 95:
            hasil_gacha.append("4 star")
            print("Selamat! Kamu mendapatkan item 4 star!")
        else:
            hasil_gacha.append("5 star")
            print("Selamat! Kamu mendapatkan item 5 star!")
            pity = 0  # reset pity

        # setiap 5x gacha tanya lanjut
        if (i + 1) % 5 == 0 and i + 1 != jumlah_gacha:
            lanjut = input("Lanjut gacha berikutnya? (y/n): ").strip().lower()
            if lanjut not in ["y", "ya", "yes"]:
                print("Gacha dihentikan sementara.")
                berhenti_dini = True
                break

    return hasil_gacha, pity


def lanjut_gacha():
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

# ===== PROGRAM UTAMA =====
print("Kesempatan setiap item:")
print("3 star (70%)")
print("4 star (25%)")
print("5 star (5%)")
print("Sistem pity aktif (90x tanpa 5-star = dijamin 5-star)\n")

pity = 0

while True:
    jumlah_gacha = mulai_gacha()
    hasil, pity = proses_gacha(jumlah_gacha, pity)

    print("\nHasil gacha kamu:")
    for i, item in enumerate(hasil):
        print(f"{i+1}. {item}")
    print(f"\nTotal pity sekarang: {pity}")

    if not lanjut_gacha():
        print("\nTerima kasih!")
        break
