""""================ MEMBUAT SEBUAH PROGRAM BIODATA DENGAN MENGGUNAKAN METODE INPUT VARIABEL 
YANG BERTIPE STRING, INTERGER DAN BOOLEAN ================="""

print("Hallo tolong masukan data anda dibawah ini!")
name = str(input("Siapa nama anda? "))
age = int(input("Berapa umur anda? "))
live = str(input("Dimana anda tinggal? "))
status = str(input("Apakah anda sudah punya pacar? (sudah/belum) "))

print("\n")
print("===================================================================================================================")
print("========================================== BIODATA DIRI ANDA ======================================================")
print("===================================================================================================================")

print("\n")
print(f"NAMA = {name}")
print(f"UMUR = {age}")
print(f"TINGGAL = {live}")
print(f"STATUS = {status}")

if status == "sudah" :
    print("iya Wahyu")
elif status == "belum" :
    print("single")
else :
    print("undefined")

print("\n")

print("===================================================================================================================")
print("============================================= TERIMA KASIH ========================================================")
print("===================================================================================================================")