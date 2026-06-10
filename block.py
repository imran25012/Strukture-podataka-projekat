import hashlib
from datetime import datetime
from merkle_tree import MerkleTree


class Block:
    """
    Predstavlja jedan blok u blockchain-u.
    """

    def __init__(self, index, records, previous_hash):
        self.index = index
        self.records = records
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.merkle_root = MerkleTree(records).get_root()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = (
            str(self.index)
            + str(self.records)
            + str(self.previous_hash)
            + str(self.timestamp)
            + str(self.merkle_root)
        )

        return hashlib.sha256(block_content.encode()).hexdigest()

    def display_block(self):
        print(f"\nBlok #{self.index}")
        print(f"Vrijeme: {self.timestamp}")
        print(f"Merkle Root: {self.merkle_root}")
        print(f"Prethodni hash: {self.previous_hash}")
        print(f"Hash bloka: {self.hash}")
        print("Zapisi:")

        for record in self.records:
            print(f"- {record}")
