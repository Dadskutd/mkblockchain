LAPORAN PRAKTIKUM BLOCKCHAIN
Sistem Traceability Tiket Konser Menggunakan Proof of Work & Hash Pointers
Nama Mahasiswa: Muhamad Haekal Bilal

NIM: 2530801087

Kelas: INF 3 D

Mata Kuliah: Praktikum Blockchain

SS
![alt text](<Screenshot 2026-10-05 132133.png>)

1. Pendahuluan
Praktikum ini bertujuan untuk mengimplementasikan konsep dasar teknologi blockchain pada sistem nyata, yaitu pelacakan dan verifikasi keaslian tiket konser (Ticket Traceability). Sistem ini dirancang untuk mencegah pemalsuan tiket dan pelacakan kepemilikan ganda melalui penerapan struktur data berantai menggunakan Hash Pointers, mekanisme Proof of Work (PoW) melalui Nonce, serta validasi integritas jaringan.

2. Arsitektur dan Komponen Sistem
Sistem blockchain ini dibagi menjadi dua modul utama agar modular dan mudah dikelola:

core.py: Berisi logika backend blockchain, termasuk definisi class Block, struktur hash SHA-256, fungsi penambangan (mining) dengan target tingkat kesulitan (difficulty), pembuatan genesis block, serta fungsi validasi integritas rantai (is_chain_valid).

app.py: Berisi antarmuka pengguna (frontend) berbasis web menggunakan framework Streamlit, yang mencakup form input data tiket, panel visualisasi payload, informasi kriptografi real-time, serta tombol verifikasi integritas rantai.

3. Pembahasan dan Analisis Sistem
Berdasarkan implementasi kode program yang telah dikembangkan di VS Code (terdiri dari file core.py dan app.py), cara kerja sistem dianalisis sebagai berikut:

Proof of Work & Nonce: Setiap kali penambahan data tiket baru dilakukan melalui antarmuka Streamlit, sistem menjalankan fungsi mine_block dengan tingkat kesulitan (difficulty = 3). Komputer melakukan iterasi perhitungan hash SHA-256 hingga ditemukan nilai Nonce yang menghasilkan hash berawalan tiga buah angka nol ('000'). Proses ini memberikan jeda komputasi simulasi penambangan blok.

Hash Pointers & Integritas Data: Setiap blok menyimpan nilai hash dari blok sebelumnya (previous_hash). Ketika tombol "Cek Integritas Rantai" ditekan, algoritma memverifikasi ulang seluruh rangkaian blok. Jika ada satu saja data di blok masa lalu yang diubah secara ilegal, hash blok tersebut akan berubah dan memutuskan rantai pointer, sehingga sistem langsung mendeteksi status BAHAYA.

4. Kesimpulan
Praktikum ini berhasil membuktikan bahwa teknologi blockchain dapat diterapkan untuk sistem pelacakan tiket konser guna mencegah pemalsuan dan penipuan tiket. Integrasi antara struktur data block, cryptographic hashing (SHA-256), Proof of Work, serta antarmuka web interaktif dengan Streamlit menghasilkan aplikasi yang fungsional, aman, dan mudah diverifikasi keasliannya.