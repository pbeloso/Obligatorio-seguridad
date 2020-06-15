import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import bcrypt



def hashPass(msg):
    hashed = bcrypt.hashpw(msg.encode('utf-8'), bcrypt.gensalt(12))

    print(hashed.decode('utf-8'))
    return hashed.decode('utf-8')

def compararPass(msg, hashbd):
    result = bcrypt.checkpw(msg.encode('utf-8'), hashbd.encode('utf-8'))
    return result

"""   
msg = "1234"
hashbd= "$$2b$12$19oSdUjmjYrSksxOYyvDsOtr2EjyCKJOfRyjpP03fhfxR.WYEMnZ6"
    
res = compararPass(msg, hashbd)
print(res)
print (msg)
print ('')
hashed = bcrypt.checkpw(msg.encode('utf-8'), hashbd.encode('utf-8'))
print(hashed)
"""

def generar_claves():
    privateKey = RSA.generate(1024)
    publicKey = privateKey.publickey()

    return privateKey, publicKey

def encrypt(msg, publicKey):
    encryptor = PKCS1_OAEP.new(publicKey)
    encrypted = encryptor.encrypt(msg)

def decrypt(encrypt, privateKey):
    decryptor = PKCS1_OAEP.new(privateKey)
    decrypted = decryptor.decrypt(encrypted)
