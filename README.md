# Blockchain praćenje lanca snabdijevanja ribom uz Merkle stabla i hash-liste

## Opis projekta

Ovaj projekat predstavlja simulaciju sistema za praćenje lanca snabdijevanja ribom korišćenjem blockchain tehnologije i naprednih struktura podataka.

Cilj sistema je omogućavanje transparentnog i sigurnog praćenja ribe kroz sve faze lanca snabdijevanja, od trenutka ulova pa do krajnjeg kupca. Na taj način se obezbjeđuje integritet podataka i smanjuje mogućnost manipulacije informacijama.

U projektu su implementirane sljedeće strukture podataka i algoritmi:

* SHA-256 hash funkcija
* Hash lista (Hash Chain)
* Merkle stablo (Merkle Tree)
* Blockchain

## Problem koji se rješava

U savremenim lancima snabdijevanja često postoji potreba za provjerom porijekla proizvoda i tačnosti podataka koji prate proizvod tokom transporta i distribucije.

Kod proizvoda kao što je riba posebno je važno znati:

* gdje je ulovljena,
* kada je transportovana,
* gdje je skladištena,
* kada je isporučena prodavnici,
* kada je prodata kupcu.

Blockchain omogućava da se svi ovi podaci čuvaju na način koji otežava njihovu naknadnu izmjenu.

## Korišćene strukture podataka

### Hash lista (Hash Chain)

Hash lista povezuje svaki zapis sa prethodnim zapisom korišćenjem hash vrijednosti. Ukoliko se promijeni jedan zapis, svi naredni hash-evi postaju neispravni.

### Merkle stablo (Merkle Tree)

Merkle stablo omogućava efikasnu provjeru integriteta većeg broja zapisa. Više hash vrijednosti se kombinuje u jednu završnu vrijednost poznatu kao Merkle Root.

### Blockchain

Blockchain povezuje više blokova u jedinstven lanac. Svaki blok sadrži hash prethodnog bloka, čime se obezbjeđuje povezanost i sigurnost podataka.

## Funkcionalnosti sistema

* Evidentiranje događaja u lancu snabdijevanja ribom
* Generisanje SHA-256 hash vrijednosti
* Kreiranje hash lanca
* Kreiranje Merkle stabla
* Formiranje blokova
* Kreiranje blockchain lanca
* Provjera integriteta blockchain-a

## Struktura projekta

```text
fish-supply-chain-blockchain/
│
├── fish_record.py
├── hash_chain.py
├── merkle_tree.py
├── block.py
├── blockchain.py
├── main.py
├── requirements.txt
└── README.md
```

## Primjer lanca snabdijevanja

1. Ulov ribe
2. Transport ribe
3. Skladištenje u hladnjači
4. Distribucija prodavnici
5. Prodaja krajnjem kupcu

## Pokretanje projekta

Nakon preuzimanja repozitorijuma projekat se pokreće komandom:

```bash
python main.py
```

## Autor

Imran Monić

## Predmet

Strukture podataka
