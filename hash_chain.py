import hashlib


class HashChain:
    """
    Kreira hash lanac za događaje u lancu snabdijevanja.
    """

    def __init__(self):
        self.chain = []

    def generate_hash(self, data, previous_hash="0"):
        content = f"{data}{previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

    def add_record(self, data):
        if not self.chain:
            previous_hash = "0"
        else:
            previous_hash = self.chain[-1]["hash"]

        current_hash = self.generate_hash(data, previous_hash)

        record = {
            "data": data,
            "previous_hash": previous_hash,
            "hash": current_hash
        }

        self.chain.append(record)

    def display_chain(self):
        for index, record in enumerate(self.chain, start=1):
            print(f"\nZapis {index}")
            print(f"Podaci: {record['data']}")
            print(f"Prethodni hash: {record['previous_hash']}")
            print(f"Hash: {record['hash']}")
