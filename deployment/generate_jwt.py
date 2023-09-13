#!/usr/bin/env python3
import jwt
import time
import sys

print("Starting generation of JWT...")

pem = sys.argv[1]
app_id = sys.argv[2]

# LOCAL USE: Open PEM
# with open(pem, 'rb') as pem_file:
#     signing_key = jwt.jwk_from_pem(pem_file.read())
signing_key = jwt.jwk_from_pem(pem)

payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minutes maximum)
    'exp': int(time.time()) + 600,
    # GitHub App's identifier
    'iss': app_id
}

# Create JWT
jwt_instance = jwt.JWT()
encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

# LOCAL USE
# print(f"JWT:  {encoded_jwt}")