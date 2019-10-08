def main():
    # membuat judul program
    print("PROGRAM PEMBAGIAN BILANGAN")
    
    # mendefinisikan blok try..except
    try:
      # meminta user memasukkan bilangan
      a =float(input("Masukkan a: "))
      b =float(input("masukkan b: "))
      
      hasil = a / b
      
      except ZeroDivinisionError:
          print("\nERROR: Nilai b tidak boleh nol")
          
       except ValuesError:
        print("\nERROR: a dan b harus berupa angka")
        
       except KeyboardInterrupt:
        print("\nERROR: Jangan tekan Ctrl+C!)
        
       else:
         print("na : ", a)
         print("b : ", b)
         print("a / b = ", hasil)
if __name__ == "__main__":
  main()
