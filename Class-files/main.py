import sys

def sum_fourth_power(values):
    if len(values) == 0:
        return 0
    first = values[0]
    rest = values[1:]
    if first < 0:
        return first ** 4 + sum_fourth_power(rest)
    return sum_fourth_power(rest)

def handle_cases(lines, pos, output):
    if pos >= len(lines):
        return output

    try:
        x = int(lines[pos].strip())
    except Exception:
        output.append(-1)
        return output

    if pos + 1 >= len(lines):
        output.append(-1)
        return output

    numbers = lines[pos + 1].strip().split()
    try:
        numbers = list(map(int, numbers))
    except Exception:
        output.append(-1)
        return handle_cases(lines, pos + 2, output)

    if len(numbers) != x:
        output.append(-1)
    else:
        output.append(sum_fourth_power(numbers))

    return handle_cases(lines, pos + 2, output)

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    try:
        t = int(data[0].strip())
    except Exception:
        return

    results = handle_cases(data[1:], 0, [])
    sys.stdout.write("\n".join(str(r) for r in results[:t]))

# if __name__ == "__main__":
    # main()


import hmac, struct, time, hashlib

def generate_totp(user_id, interval=30, digits=10):
    # Shared secret: userid + "HENNGECHALLENGE004"
    secret = (user_id + "HENNGECHALLENGE004").encode("utf-8")

    # Compute time counter T
    counter = int((time.time()) // interval)

    # Pack counter into 8-byte big-endian
    counter_bytes = struct.pack(">Q", counter)

    # Compute HMAC-SHA-512
    hmac_digest = hmac.new(secret, counter_bytes, hashlib.sha512).digest()

    # Dynamic truncation (RFC4226 section 5.3)
    offset = hmac_digest[-1] & 0x0F
    code = struct.unpack(">I", hmac_digest[offset:offset+4])[0] & 0x7fffffff

    # Generate 10-digit code
    return str(code % (10 ** digits)).zfill(digits)

def main():
    user_id = "vishnukumarbhandari.work@gmail.com"  # Replace with your email
    totp = generate_totp(user_id)
    print("10-digit TOTP password:", totp)

    # Generate Basic Auth header
    import base64
    user_pass = f"{user_id}:{totp}".encode("utf-8")
    auth_header = base64.b64encode(user_pass).decode("utf-8")
    print("Authorization:", f"Basic {auth_header}")

# if __name__ == "__main__":
#     main()


# Basic dmlzaG51a3VtYXJiaGFuZGFyaS53b3JrQGdtYWlsLmNvbToxNjI1OTI0Nzg2
# 1625924786


# 0433585393