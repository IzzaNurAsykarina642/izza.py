#List


# Menambahkan Elemen
# Menggunakan Append
angka = [1,2,3]
angka.append (4)
print('Angka (menggunakan append): ', angka) # output = [1,2,3,4]
# menggunakan insert
angka2 = [1,2,4,5]
angka2.insert (2,3)
print('Angka (menggunakan insert): ',angka2) # output = [1, 2, 3, 4, 5]

# menghapus elemen 
# menggunakan Remove
angka_remove = angka.remove(1)
print('Angka (menggunakan remove): ', angka) # output = [2, 3, 4]
# menggunakan Pop
elemen = angka.pop(2)
print('Angka(menggunakan pop): ', angka) # output =  [2, 3]

# pencarian elemen 
indeks = angka.index(3)
print('Indeks angka 3: ', indeks) # output 1

#Dictionary

# menambahkan & mengubah elemen
murid = {'nama':'Izza','umur':15}
murid['jurusan'] = 'RPL' # menambahkan elemen
murid['jurusan'] = 'PPLG' # mengubah elemen
print('Murid: ', murid)
# menghapus elemen
umur = murid.pop('umur')
print('Murid (setelah umur dihapus): ', murid)
# del murid
# pencarian elemen
ada = 'nama' in murid
print('Apakah ada key nama pada variabel murid? ', ada) #output = True

# Set 


# menambah elemen
set_saya = {1,2,3}
set_saya.add(4)
print('Set: ', set_saya) #output = {1, 2, 3, 4}
#Menghapus elemen 
set_remove = set_saya.remove(3)
print('Hapus set menggunakan remove: ', set_saya)
set_discard = set_saya.discard(3)
print('Hapus set menggunakan discard: ', set_saya)

# Operasi himpunan pada set
set_A = {1,2,3,4,5}
set_B = {4,5,6,7,8}

#gabungan (union)
union_set = set_A.union(set_B)
print('Gabungan: ', union_set)
# irisan (interseccion)
intersection_set = set_A.intersection(set_B)
print('Irisan: ', intersection_set)
# selisih (difference) untuk set A
difference_set_A = set_A.difference(set_B)
print('Selisih set A: ', difference_set_A)
# selisih (difference) untuk set B 
difference_set_B = set_B.difference(set_A)
print('Selisih set B: ', difference_set_B)