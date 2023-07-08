# Bitcoin private key cracker
The program below is a experimental program that is designed to find balance on any given public key. A Bitcoin private key is a 256-bit number, meaning it can have 2^256 possible combinations. To put this into perspective, that is an astronomical number with roughly 10^77 possible combinations.

So using this program is a compleet waste of time and energy. But if you have time and energy and you want to give it a try, then follow the instuctions below.

## 1. So how does this work?
Download the data file from: http://addresses.loyce.club/ and make sure that it is named:

```
blockchair_bitcoin_addresses_and_balance_LATEST.tsv
```

After that run the file:
```
main.py
```

The program starts generating private keys and matches the public key to a dictionary where the used public keys with balance is stored. It is designed to run multi thread so to improve the performance add more threads. The default is 220 instances.

## 2. Donation and help

### 2.1 Donation

Crypto:

```
BTC (Bitcoin): bc1qulyuywjkeamqu0h9ctuj5cla8u0pagkaa83hf6
LTC (Litecoin): ltc1q25j4yxg9dkwknrh4a7fvndtt3358c4gjnsf9qv
BCH (Bitcoin Cash): qq9qd6gshp4n9gkk3zy9505p8j8jlhur4uv0lxv2d8
```
