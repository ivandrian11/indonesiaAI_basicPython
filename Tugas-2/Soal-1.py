print("Selamat datang!")

contacts = []

while(True):
  print("--- Menu ---")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Keluar")

  choice = int(input("Pilih menu: "))

  if choice == 1:
    if len(contacts) > 0:
      print("Daftar kontak:")
      for contact in contacts:
        print(f"Nama: {contact['name']}")
        print(f"No. Telepon: {contact['phone']}")
    else:
      print("Belum ada kontak. Silahkan isi terlebih dahulu!")

  elif choice == 2:
    new_contact = {}
    new_contact['name'] = input("Nama: ")
    new_contact['phone'] = input("No. Telepon: ")
    contacts.append(new_contact)
    print("Kontak berhasil ditambahkan")

  elif choice == 3:
    print("Program selesai, sampai jumpa!")
    break # out

  else:
    print("Menu tidak tersedia")