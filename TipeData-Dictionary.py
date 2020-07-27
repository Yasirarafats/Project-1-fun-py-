"""
Tipe data dictionary sekedar menghubungkan KEY ke Value
KVP = Key Value Pair
dictionary= kamus

"""

kamus_ind_to_eng = {'anak': 'son', 'roti': 'bread', 'nasi': 'rice', 'dua': 'two'}
print(kamus_ind_to_eng['anak'])
print(kamus_ind_to_eng['dua'])

print('\nData Judul dan Buku yang dipinjam di Perpustakaan UGM')
data_dari_perpus_ugm = {
    'tanggal peminjaman': '27 Juli 2020',
    'List Buku Pemerograman': [
        {'Judul':'Python Fundamental','Dipinjam': 40},
        {'Judul':'Pemerograman 1','Dipinjam': 24},
        {'Judul':'Komunikasi Data','Dipinjam': 45},
        {'Judul':'C++','Dipinjam': 13}
]
}
print(data_dari_perpus_ugm)
print(f"\nBuku #1 {data_dari_perpus_ugm['List Buku Pemerograman'][0]}")
print(f"Buku #2 {data_dari_perpus_ugm['List Buku Pemerograman'][1]}")
print(f"Buku #3 {data_dari_perpus_ugm['List Buku Pemerograman'][2]}")
print(f"Buku #4 {data_dari_perpus_ugm['List Buku Pemerograman'][3]}")

print(f"\nBuku #1 Berjudul: {data_dari_perpus_ugm['List Buku Pemerograman'][0]['Judul']}")
print(f"Buku #2 Berjudul: {data_dari_perpus_ugm['List Buku Pemerograman'][1]['Judul']}")
print(f"Buku #3 Berjudul: {data_dari_perpus_ugm['List Buku Pemerograman'][2]['Judul']}")
print(f"Buku #4 Berjudul: {data_dari_perpus_ugm['List Buku Pemerograman'][3]['Judul']}")



print(f"\nBuku #1 dipinjam {data_dari_perpus_ugm['List Buku Pemerograman'][0]['Dipinjam']} kali")
print(f"Buku #2 dipinjam {data_dari_perpus_ugm['List Buku Pemerograman'][1]['Dipinjam']} kali")
print(f"Buku #3 dipinjam {data_dari_perpus_ugm['List Buku Pemerograman'][2]['Dipinjam']} kali")
print(f"Buku #4 dipinjam {data_dari_perpus_ugm['List Buku Pemerograman'][3]['Dipinjam']} kali")