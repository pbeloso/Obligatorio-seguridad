import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import bcrypt

msg = 'pelado boton'
hashbd= '$2b$12$l9XyD4K/MIaPFCCJtySQl../BEtEhDg2YfuXftdi8Jfjqr/zDd/3i'

print (msg)
print ('')

hashed = bcrypt.hashpw(msg.encode('utf-8'), bcrypt.gensalt(12))

print(hashed)

print('Comparación con la bd:   ' , bcrypt.checkpw(msg.encode('utf-8'), hashbd.encode('utf-8')))

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
    