import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

privateKey = RSA.generate(3072)

print 'private key:', privateKey
print ''
publicKey = privateKey.publickey()

print 'public key:', publicKey
print ''

msg = b'maicool puto'
print msg
print ''

encryptor = PKCS1_OAEP.new(publicKey)
encrypted = encryptor.encrypt(msg)
print ''
print 'encrypted:', encrypted

decryptor = PKCS1_OAEP.new(privateKey)
decrypted = decryptor.decrypt(encrypted)
print ''
print 'Decrypted:', decrypted