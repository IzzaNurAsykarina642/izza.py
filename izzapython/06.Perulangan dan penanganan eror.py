# for 
angka = [1,2,3,4,5]
for i in angka:
    print(i)

#range
for i in range(5):
    print(f'Perulangan ke-{i}')

#while
i = 0
while i < 5:
    print(f'i bernilai {i}')
    i += 1

#try-except
try:
    a= int(input('Masukkan angka pertama: '))
    b= int(input('Masukkan angaka kedua: '))
    hasil = a/b
    print(f'Hasil: ',{hasil})
except ZeroDivisionError:
    print('Error: Tidak bisa membagi dengan nol!')
except ValueError:
    print('Eroor: Input harus berupa angka!')

    #menggabungkan perulangan & penangganan error
    while True:
        try: 
            angka = int(input('masukkan angka: '))
            print(f'Angka yang dimasukkan: {angka}')
            break
        except ValueError: 
            print('Error: Harap masukkan angka yang valid!')