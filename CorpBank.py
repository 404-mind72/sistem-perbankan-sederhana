import datetime
import os

class Bank_Akun:
    daftarNasabah = {}
    jumlahNasabah = 0
    nomorRekening = 400010

    def __init__(self, nama, no_hp, depo_awal, pin):
        self.nama = nama
        self.no_hp = no_hp
        self.depo_awal = depo_awal
        self.pin = pin
        Bank_Akun.jumlahNasabah += 1
        Bank_Akun.nomorRekening += 1
        self.no_rek = Bank_Akun.nomorRekening
        # Menambahkan info ke daftarNasabah
        Bank_Akun.daftarNasabah[self.nomorRekening] = [self.nama, self.no_hp, self.depo_awal, self.pin]
        print("Nasabah ditambahkan!")
        print(f"Selamat datang {self.nama}! Nomor rekening kamu {self.nomorRekening}")


class Nasabah:
    def Menu(no_rek):
        os.system("cls")
        print(f'''
            ===============================================
            ===============  BANK SEDERHANA ================
            ===============================================
                    SELAMAT DATANG DI BANK SEDERHANA
            Nama                : {Bank_Akun.daftarNasabah[no_rek][0]}
            Nomor Akun          : {no_rek}
            Tanggal             : {datetime.datetime.now().strftime('%H:%M %d/%m/%Y')}
            Saldo Saat ini      : Rp.{Bank_Akun.daftarNasabah[no_rek][2]}
            ===============================================
            ||||||||||||||||||||||||||||||||||||||||||||||||
        ''')
        print('''[1] DEPOSIT :
[2] PENARIKAN :
[3] TRANSFER UANG :
[4] KELUAR\n''')
        opsi = input("Pilihan : ")
        if opsi == "1":
            Nasabah.Simpanan(no_rek)
        elif opsi == "2":
            Nasabah.Tarikan(no_rek)
        elif opsi == "3":
            Nasabah.Transfer(no_rek)
        elif opsi == "4":
            MenuUtama()
        else:
            print("Salah Pilih Nomor Inputan Bos!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Menu(no_rek)
    
    def Simpanan(no_rek):
        try:
            jumlah_setoran = int(input("Masukkan Jumlah Setoran : Rp."))
        except:
            print("Salah Pilih Inputan Bos!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Simpanan(no_rek)
        if jumlah_setoran <= 0:
            print("Uang Mu Kurang Woy!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Simpanan(no_rek)
        Bank_Akun.daftarNasabah[no_rek][2] += jumlah_setoran
        print(f"Transaksi Selesai! Saldo anda saat ini : Rp.{Bank_Akun.daftarNasabah[no_rek][2]}")
        input("Tekan [ENTER] untuk melanjutkan..")
        Nasabah.Menu(no_rek)

    def Tarikan(no_rek):
        try:
            jumlah_tarikan = int(input("Masukkan   Jumlah Tarikan : Rp."))
        except:
            print("Salah Pilih Inputan Bos!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Simpanan(no_rek)
        if jumlah_tarikan <= 0:
            print("Uang Mu Kurang Woy!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Simpanan(no_rek)
        Bank_Akun.daftarNasabah[no_rek][2] -= jumlah_tarikan
        print(f"Transaksi Selesai! Saldo anda saat ini : Rp.{Bank_Akun.daftarNasabah[no_rek][2]}")
        input("Tekan [ENTER] untuk melanjutkan..")
        Nasabah.Menu(no_rek)

    def Transfer(no_rek):
        try:
            no_rek_penerima = int(input("Nomor Rekening Penerima : "))
        except KeyboardInterrupt:
            Nasabah.Menu(no_rek)
        except:
            print("Salah Pilih Inputan Bos!")
            Nasabah.Transfer(no_rek)
        # Pengecekan
        if no_rek_penerima in Bank_Akun.daftarNasabah.keys():
            try:
                jumlah_transfer = int(input("Masukkan Jumlah Transfer : Rp."))
            except:
                print("Salah Pilih Inputan Bos!")
                input("Tekan [ENTER] untuk melanjutkan..")
                Nasabah.Transfer(no_rek)
            if jumlah_transfer <= 0 or jumlah_transfer > Bank_Akun.daftarNasabah[no_rek][2]:
                print("Uang Mu Kurang Sodara")
                input("Tekan [ENTER] untuk melanjutkan..")
                Nasabah.Transfer(no_rek)
            # Validasi
            try:
                no_pin = int(input("Masukkan PIN : "))
                if Bank_Akun.daftarNasabah[no_rek][3] == no_pin:
                    Bank_Akun.daftarNasabah[no_rek_penerima][2] += jumlah_transfer
                    Bank_Akun.daftarNasabah[no_rek][2] -= jumlah_transfer
                    print(f"Transaksi sukses! Saldo anda saat ini : Rp.{Bank_Akun.daftarNasabah[no_rek][2]}")
                    
                    print(f'''
            ===============================================           
            ===============  BANK TEKOM A1 ================
            ===============================================
            Transfer Kepada     : {no_rek_penerima}
            Sebesar             : Rp.{jumlah_transfer}
            ===============================================
            Info Penerimaan
            Nama Penerima       : {Bank_Akun.daftarNasabah[no_rek_penerima][0]}
            Tanggal             : {datetime.datetime.now().strftime('%H:%M %d/%m/%Y')}
            Metode Pembayaran   : BANK CORPORATE
            ||||||||||||||||||||||||||||||||||||||||||||||||
            Total Transaksi     : Rp.{jumlah_transfer}
            Sisa Saldo Saat ini : Rp.{Bank_Akun.daftarNasabah[no_rek][2]} ''')
                    
                    input("Tekan [ENTER] untuk melanjutkan..")
                    Nasabah.Menu(no_rek)
                else:
                    print("PIN salah! Transaksi dibatalkan!")
                    input("Tekan [ENTER] untuk melanjutkan..")
                    Nasabah.Transfer(no_rek)
            except:
               print("Salah Pilih Inputan Bos!")
               input("Tekan [ENTER] untuk melanjutkan..")
               Nasabah.Transfer(no_rek)
        else:
            print("Nomor Rekening tidak terdaftar!")
            input("Tekan [ENTER] untuk melanjutkan..")
            Nasabah.Transfer(no_rek)
        

def MenuUtama():
    os.system("cls")        # Bersihkan layar
    print('''
    ===============================================
    ===============  BANK TEKOM A1 ================
    ===============================================
                SELAMAT DATANG DI BANK
    ''')
    print('''[1] Membuat Nasabah Baru :
[2] Masuk Sebagai Nasabah Yang Sudah Terdaftar :
[3] Menampilkan Jumlah Nasabah Dan Uang Nasabah :
[4] Keluar \n''')
    opsi_menu = input("Pilih : ")
    if opsi_menu == "1":
        namaNasabah = input("Nama Nasabah : ")
        try:
            no_hpNasabah = int(input("Nomor HP : "))
            depo_awalNasabah = int(input("Setoran Awal : "))
            pinNasabah = int(input("Masukkan PIN : "))
        except:
            print("Masukkan Angka Abangku!")
            input("Tekan [ENTER] untuk melanjutkan..")
            MenuUtama()
        # Membuat objek
        objNasabah = Bank_Akun(namaNasabah, no_hpNasabah, depo_awalNasabah, pinNasabah)
        
        input("Tekan [ENTER] untuk melanjutkan..")
        MenuUtama()
    elif opsi_menu == "2":
        try:
            no_rek = int(input("Nomor Rekening : "))
            pin = int(input("Kode PIN : "))
        except:
            print("Salah Pilih Inputan Bos!")
            input("Tekan [ENTER] untuk melanjutkan..")
            MenuUtama()
        # Pengecekan
        if no_rek in Bank_Akun.daftarNasabah.keys():
            if Bank_Akun.daftarNasabah[no_rek][3] == pin:
                Nasabah.Menu(no_rek)
            else:
                print("Salah Pilih Inputan Bos!")
                input("Tekan [ENTER] untuk melanjutkan..")
                MenuUtama()
        else:
            print("Nomor Rekening tidak terdaftar!")
            input("Tekan [ENTER] untuk melanjutkan..")
            MenuUtama()
    elif opsi_menu == "3":
        os.system("cls")
        total_uang_nasabah = 0
        for key,value in Bank_Akun.daftarNasabah.items():
            print(f"Nomor Rekening : {key} ---> Info Nasabah : {value}")
            total_uang_nasabah += value[2]
        print()
        print(f"Jumlah Nasabah : {Bank_Akun.jumlahNasabah}")
        print(f"Total Uang Nasabah : Rp.{total_uang_nasabah}")
        print()
        input("Tekan [ENTER] untuk melanjutkan..")
        MenuUtama()
    elif opsi_menu == "4":
        print("Menutup program..")
        return
    else:
        MenuUtama()
        
MenuUtama()