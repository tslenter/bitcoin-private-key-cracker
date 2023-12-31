# Bitcoin private key cracker
The program below is a experimental program from 2018 - 2019 that is designed to find balance on any given public key. A Bitcoin private key is a 256-bit number, meaning it can have 2^256 possible combinations. To put this into perspective, that is an astronomical number with roughly 10^77 possible combinations.

So using this program is a compleet waste of time and energy. While it is true that the effectiveness of the program for cracking Bitcoin private keys is limited and may not yield significant results, if you still wish to proceed and have the time and energy to spare, you can follow the instructions outlined below.

## 1. So how does this work?

### 1.1 Instuctions

Download the data file from: http://addresses.loyce.club/ and make sure that it is named:

```
blockchair_bitcoin_addresses_and_balance_LATEST.tsv
```

After that run the file:
```
main.py
```

The program initiates the generation of private keys and matches them with corresponding public keys stored in a dictionary, which contains information about used public keys and their associated balances. To enhance performance, the program is designed to run using multiple threads. By adding more threads, the overall performance can be further improved. The default setting is configured with 220 instances, but this can be adjusted based on specific requirements and system capabilities.

### 1.2 History

In the early days of experimenting with cryptocurrencies, this idea came to my mind. As anticipated, the program couldn't find any private key. This program is a component of Jafar Remote Syslog Trading and was intended to obtain a lucky ticket for some free money ;-). Typically, everything from Jafar Remote Syslog is closed source, but because of the fun and experimental nature of this useless code, it might be enjoyable to share.

## 2. Donation and help

### 2.1 Donation

Crypto:

```
BTC (Bitcoin): bc1qulyuywjkeamqu0h9ctuj5cla8u0pagkaa83hf6
LTC (Litecoin): ltc1q25j4yxg9dkwknrh4a7fvndtt3358c4gjnsf9qv
BCH (Bitcoin Cash): qq9qd6gshp4n9gkk3zy9505p8j8jlhur4uv0lxv2d8
```
