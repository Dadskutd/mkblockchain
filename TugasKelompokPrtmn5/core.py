import hashlib  # cite: 1
import time  # cite: 1


class Block:  # cite: 1
    def __init__(self, index, data, previous_hash):  # cite: 1
        self.index = index  # cite: 1
        self.timestamp = time.time()  # cite: 1
        self.data = data  # cite: 1
        self.previous_hash = previous_hash  # cite: 1
        self.nonce = 0  # ATRIBUT BARU: Angka tebakan miner  # cite: 1
        self.hash = self.calculate_hash()  # cite: 1

    def calculate_hash(self):  # cite: 1
        # ATRIBUT BARU: nonce ikut dimasukkan ke dalam perhitungan hash  # cite: 1
        value = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )  # cite: 1
        return hashlib.sha256(value.encode()).hexdigest()  # cite: 1

    def mine_block(self, difficulty):  # cite: 1
        # Membuat target awalan nol, misal difficulty 3 -> "000"  # cite: 1
        target = "0" * difficulty  # cite: 1

        # Looping (PoW): Terus tebak nonce sampai hash diawali dengan "000"  # cite: 1
        while self.hash[:difficulty] != target:  # cite: 1
            self.nonce += 1  # cite: 1
            self.hash = self.calculate_hash()  # cite: 1

        print(
            f"Block Mined! Nonce: {self.nonce} | Hash: {self.hash}"
        )  # cite: 1


class Blockchain:  # cite: 1
    def __init__(self):  # cite: 1
        self.chain = [self.create_genesis_block()]  # cite: 1
        self.difficulty = 3  # ATRIBUT BARU: Tingkat kesulitan mining  # cite: 1

    def create_genesis_block(self):  # cite: 1
        return Block(0, "Genesis Block - Rantai Dimulai", "0")  # cite: 1

    def get_latest_block(self):  # cite: 1
        return self.chain[-1]  # cite: 1

    def add_block(self, new_block):  # cite: 1
        new_block.previous_hash = self.get_latest_block().hash  # cite: 1
        # ATRIBUT BARU: Panggil fungsi mining sebelum blok ditambahkan ke rantai  # cite: 1
        new_block.mine_block(self.difficulty)  # cite: 1
        self.chain.append(new_block)  # cite: 1

    def is_chain_valid(self):  # cite: 1
        # Fungsi untuk mengecek apakah ada data yang dimanipulasi  # cite: 1
        for i in range(1, len(self.chain)):  # cite: 1
            current_block = self.chain[i]  # cite: 1
            previous_block = self.chain[i - 1]  # cite: 1

            # 1. Cek apakah hash block saat ini masih valid (data tidak diubah)  # cite: 1
            if current_block.hash != current_block.calculate_hash():  # cite: 1
                return False  # cite: 1
            # 2. Cek apakah pointer ke block sebelumnya masih akurat  # cite: 1
            if current_block.previous_hash != previous_block.hash:  # cite: 1
                return False  # cite: 1
        return True  # cite: 1