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

# Define gaji karyawan pertama untuk membandingkan dengan karyawan selanjutnya sampai terakhir
highest_salary = employee[0]['salary']
lowest_salary = employee[0]['salary']

# Looping data karyawan
for data in employee:
    
    # Define gaji
    salary = data['salary']
    
    # Gaji terbesar
    if salary > highest_salary:
        highest_salary = salary
        
    # Gaji terkecil
    if salary < lowest_salary:
        lowest_salary = salary
    
# Output
print(f"Gaji Terbesar: {highest_salary}\n")
print(f"Gaji Terkecil: {lowest_salary}\n")