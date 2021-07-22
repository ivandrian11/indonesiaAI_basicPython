theory = float(input("Masukkan nilai ujian teori: "))
practice = float(input("Masukkan nilai ujian praktek: "))

if theory >= 70 and practice >= 70:
    print("Selamat, anda lulus!")
elif theory >= 70 and practice < 70:
    print("Anda harus mengulang ujian praktek.")
elif theory < 70 and practice >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")