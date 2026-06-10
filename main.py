from fish_record import FishRecord
from hash_chain import HashChain
from blockchain import Blockchain


def main():
    print("BLOCKCHAIN PRACENJE LANCA SNABDIJEVANJA RIBOM")

    # Kreiranje događaja za jednu ribu kroz lanac snabdijevanja
    record1 = FishRecord("RIBA-001", "Ulcinj", "Ulovljena")
    record2 = FishRecord("RIBA-001", "Bar", "Transportovana")
    record3 = FishRecord("RIBA-001", "Podgorica", "Skladistena u hladnjaci")
    record4 = FishRecord("RIBA-001", "Podgorica", "Isporucena prodavnici")
    record5 = FishRecord("RIBA-001", "Podgorica", "Prodata kupcu")

    records = [record1, record2, record3, record4, record5]

    # Hash lanac pokazuje kako se svaki događaj povezuje sa prethodnim
    hash_chain = HashChain()

    for record in records:
        hash_chain.add_record(str(record))

    print("\nHASH LANAC DOGADJAJA")
    hash_chain.display_chain()

    # Blockchain čuva zapise u blokovima
    blockchain = Blockchain()
    blockchain.add_block(records[:3])
    blockchain.add_block(records[3:])

    print("\nBLOCKCHAIN")
    blockchain.display_blockchain()

    print("\nPROVJERA ISPRAVNOSTI BLOCKCHAIN-A")

    if blockchain.is_chain_valid():
        print("Blockchain je ispravan.")
    else:
        print("Blockchain nije ispravan.")


if __name__ == "__main__":
    main()
