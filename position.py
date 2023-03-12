# Data Karyawan berdasarkan tabel pada soal
employee = [
    {'gender': 'Laki-Laki', 'age': 20, 'salary': 8000000, 'transportation': 'Kendaraan pribadi'},
    {'gender': 'Laki-Laki', 'age': 35, 'salary': 14000000, 'transportation': 'Kendaraan umum'},
    {'gender': 'Perempuan', 'age': 26, 'salary': 10000000, 'transportation': 'Kendaraan umum'},
    {'gender': 'Perempuan', 'age': 27, 'salary': 12000000, 'transportation': 'Kendaraan pribadi'},
    {'gender': 'Laki-Laki', 'age': 21, 'salary': 9000000, 'transportation': 'Kendaraan pribadi'},
    {'gender': 'Laki-Laki', 'age': 22, 'salary': 11000000, 'transportation': 'Kendaraan pribadi'},
    {'gender': 'Perempuan', 'age': 32, 'salary': 15000000, 'transportation': 'Kendaraan umum'},
    {'gender': 'Perempuan', 'age': 26, 'salary': 8000000, 'transportation': 'Kendaraan umum'},
    {'gender': 'Laki-Laki', 'age': 25, 'salary': 9000000, 'transportation': 'Kendaraan umum'},
    {'gender': 'Perempuan', 'age': 20, 'salary': 10000000, 'transportation': 'Kendaraan pribadi'}
]

# Looping data karyawan
for data in employee:
    
    # Define gaji
    salary = data['salary']
    
    # a. Gaji = 8 juta – 9 juta, jabatan = officer
    if salary >= 8_000_000 and salary <= 9_000_000:
        position = "Officer"
    
    # b. Gaji = 10 juta – 11 juta, jabatan = supervisor
    elif salary >= 10_000_000 and salary <= 11_000_000:
        position = "Supervisor"
    
    # c. Gaji = 12 juta – 14 juta, jabatan = asisten manajer
    elif salary >= 12_000_000 and salary <= 14_000_000:
        position = "Asisten Manajer"
        
    # d. Gaji >= 15 juta, jabatan = manager
    elif salary >= 15_000_000:
        position = "Manager"
        
    # Jika tidak sesuai
    else:
        position = "Belum ditentukan"
    
    # Output
    print(f"Jenis Kelamin: {data['gender']}\n")
    print(f"Umur: {data['age']}\n")
    print(f"Gaji: {salary}\n")
    print(f"Transportasi: {data['transportation']}\n")
    print(f"Jabatan: {position}\n\n")