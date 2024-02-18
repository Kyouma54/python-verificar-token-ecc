import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def obter_chaves_jwks():
    # Obtém o conjunto de chaves JWKs da URL
    jwks_url = "https://firebaseappcheck.googleapis.com/v1/jwks"
    jwks_response = requests.get(jwks_url)
    jwks = jwks_response.json()
    return jwks

def converter_jwk_para_pem(jwk):
    chave_rsa = rsa.RSAPublicNumbers(
        int(jwk['n'], 64),
        int(jwk['e'], 64)
    ).public_key()

    chave_pem = chave_rsa.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return chave_pem.decode('utf-8')

# Exemplo de uso
jwks = obter_chaves_jwks()

# Escolha uma chave JWK específica (pode haver várias)
chave_jwk = jwks['keys'][0]

# Converte a chave JWK para formato PEM
chave_pem = converter_jwk_para_pem(chave_jwk)

print("Chave PEM:")
print(chave_pem)