from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature

def sign_document(private_key, document):
    signature=private_key.sign(
        document.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH

        ),
        hashes.SHA256()
    )
    return signature

def verify_document(public_key, document, signature):
    try:
        public_key.verify(
            signature,
            document.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    
private_key=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key=private_key.public_key()

document="""
This is a legal document.
By signing this, you agree to the terms and conditions.
"""

signature=sign_document(private_key, document)

#문서검증
is_valid=verify_document(public_key, document, signature)
print(f"Document signature is valid: {is_valid}")

tampered_document=document+"\nThis line was added illegally"
is_valid=verify_document(public_key, tampered_document, signature)
print(f"Tampered document signature is valid: {is_valid}")