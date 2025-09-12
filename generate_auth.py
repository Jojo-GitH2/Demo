import base64, hmac, hashlib, struct, time

EMAIL = "jonahuka001@gmail.com"

def generate_totp(email: str, digits: int = 10, step: int = 30) -> str:
    secret = (email + "HENNGECHALLENGE004").encode("utf-8")
    counter = int(time.time() // step)
    msg = struct.pack(">Q", counter)
    hmac_digest = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    code_int = (
        ((hmac_digest[offset] & 0x7F) << 24)
        | ((hmac_digest[offset + 1] & 0xFF) << 16)
        | ((hmac_digest[offset + 2] & 0xFF) << 8)
        | (hmac_digest[offset + 3] & 0xFF)
    )
    return str(code_int % (10**digits)).zfill(digits)

totp = generate_totp(EMAIL)
auth_str = f"{EMAIL}:{totp}"
# print(auth_str)
auth_token = base64.b64encode(auth_str.encode()).decode()

# print("Email + TOTP string:", auth_str)
# print("Base64:", auth_token)


print(auth_token)   # only the token, no extra text
