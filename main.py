#load modules
import os
import hashlib
import threading

#Download files from:
#http://addresses.loyce.club/

#Preload all bitcoin addresses to memory
a_dict = {}
#Change for test file
print("Load data to memory, this may take a while ... ")
a_tsv = open("blockchair_bitcoin_addresses_and_balance_LATEST.tsv")
#a_tsv = open("test.tsv")
for line in a_tsv:
    key, value = line.split()
    a_dict[key] = value
print("Load data to memory is done ... ")
#Use this to display the dictionary
#print(a_dict)

#Functions to generate bitcoin address:
def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return digest.digest()

def ripemd160(x):
    d = hashlib.new("ripemd160")
    d.update(x)
    return d.digest()

def b58(data):
    B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    if data[0] == 0:
        return "1" + b58(data[1:])

    x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
    ret = ""
    while x > 0:
        ret = B58[x % 58] + ret
        x = x // 58

    return ret

class Point:
    def __init__(self,
        x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, other):
        return self.__radd__(other)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        n = self
        q = None

        for i in range(256):
            if other & (1 << i):
                q = q + n
            n = n + n

        return q

    def __radd__(self, other):
        if other is None:
            return self
        x1 = other.x
        y1 = other.y
        x2 = self.x
        y2 = self.y
        p = self.p

        if self == other:
            l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
        else:
            l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

        newX = (l ** 2 - x2 - x1) % p
        newY = (l * x2 - l * newX - y2) % p

        return Point(newX, newY)

    def toBytes(self):
        x = self.x.to_bytes(32, "big")
        y = self.y.to_bytes(32, "big")
        return b"\x04" + x + y


def getPublicKey(privkey):
    SPEC256k1 = Point()
    pk = int.from_bytes(privkey, "big")
    hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
    address = b"\x00" + hash160

    address = b58(address + sha256(sha256(address))[:4])
    return address


def getWif(privkey):
    wif = b"\x80" + privkey
    wif = b58(wif + sha256(sha256(wif))[:4])
    return wif

def combine():
    while True:
        randomBytes = os.urandom(32)
        publickey = getPublicKey(randomBytes)
        privatekey = getWif(randomBytes)
        #print("Checking: " + publickey)

        # Print data if something is found
        if a_dict.get(publickey) != None:
            print("Address found: " + publickey + ": %s" % a_dict.get(publickey))
            print("Private_key: "+ privatekey)
            file = open('result.csv', 'a')
            file.write("Privatekey:" + privatekey + ": " + publickey + " | " + "Balance: " +  a_dict.get(publickey) + "\n")
            file.close()

if __name__ == "__main__":
    threads = list()
    print("Start cracking ...")

    publickey = "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo"
    privatekey = "Test_private_key"

    #Print test value
    if a_dict.get(publickey) != None:
        print("Print test value, the value should be: 25259722706415")
        print("Address found: " + publickey + ": %s" % a_dict.get(publickey))
        file = open('result.csv', 'a')
        file.write("Test_Privatekey:" + privatekey + ": " + publickey + " | " + "Balance: " + a_dict.get(publickey) + "\n")
        file.close()

    for index in range(220):
        x = threading.Thread(target=combine)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
