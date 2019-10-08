def main():
    # membuat judul program
    print("PROGRAM PEMBAGIAN BILANGAN")
    
    # meminta user memasukkan bilangan
    a = float(input("Masukkan a: "))
    b = float(input("Masukkan b: "))
    
    # mendefinisikan blok try...except
    try:
      hasil = a / b
     except ZeroDivinisionError:
      print("nERROR: Nilai b tidak boleh kosong nol")
    else:
      print("\na : ",a)
      print(b : ", b)
      print("a / b = ", hasil)
      
  if __name__ == "__main__":
    main()
