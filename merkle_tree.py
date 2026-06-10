import hashlib


class MerkleTree:
    """
    Kreira Merkle stablo od liste zapisa.
    """

    def __init__(self, records):
        self.records = records
        self.root = self.create_merkle_root(records)

    def hash_data(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def create_merkle_root(self, records):
        if not records:
            return None

        current_level = [self.hash_data(str(record)) for record in records]

        while len(current_level) > 1:
            next_level = []

            for i in range(0, len(current_level), 2):
                left = current_level[i]

                if i + 1 < len(current_level):
                    right = current_level[i + 1]
                else:
                    right = left

                combined_hash = self.hash_data(left + right)
                next_level.append(combined_hash)

            current_level = next_level

        return current_level[0]

    def get_root(self):
        return self.root
