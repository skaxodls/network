import socket
import ssl
import hashlib
import OpenSSL.crypto
from cryptography.hazmat.primitives import serialization

def pin_public_key(cert):
    public_key=cert.get_pubkey()
    key_der=public_key.to_cryptography_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return hashlib.sha256(key_der).digest()

def secure_ssl_client_with_pinning():
    context=ssl.create_default_context()
    context.set_ciphers('ECDHE+AESGCM')
    context.minimum_version=ssl.TLSVersion.TLSv1_2
    context.check_hostname=True
    context.verify_mode=ssl.CERT_REQUIRED

    #예상되는 공개키의 SHA-256 해시 (개인마다 입력)
    expected_pin=b'>hK\xfdE\x8eXt\xe2\x92i\x13%\xb6p\xe0\xb3)~)\xf5F\xc8c\x87\xa8\xca4\xabEDA'
    try:
        with socket.create_connection(('www.python.org', 443)) as sock:
            with context.wrap_socket(sock, server_hostname='www.python.org') as secure_sock:
                cert=secure_sock.getpeercert(binary_form=True)
                cert_obj=OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1,cert)
                actual_pin=pin_public_key(cert_obj)
                print(f"actual_pin:{actual_pin}")

                if actual_pin != expected_pin:
                    raise ssl.SSLError("공개키 핀 불일치")
                print("공개키 핀 검증 완료")

    except ssl.SSLError as e:
        print(f"SSL 오류 발생 : {e}")

if __name__=="__main__":
    secure_ssl_client_with_pinning()