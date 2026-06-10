from block import Block


class Blockchain:
    """
    Predstavlja blockchain koji povezuje više blokova u jedan lanac.
    """

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis block"], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, records):
        previous_block = self.get_last_block()
        new_block = Block(
            index=len(self.chain),
            records=records,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_blockchain(self):
        for block in self.chain:
            block.display_block()
