import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash='0'):
        self.index = index
        self.timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Menghitung nilai SHA-256 hash untuk block saat ini."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class TicketBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Block awal pembuatan/penerbitan tiket oleh Promotor."""
        genesis_data = {
            "nama_pemilik": "Promotor Resmi (Genesis)",
            "kategori_tiket": "SYSTEM INITIATOR",
            "nomor_kursi": "STAGE-00",
            "status_tiket": "Penerbitan Resmi"
        }
        return Block(0, genesis_data, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)
        return new_block