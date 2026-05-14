import os
import socket
import sys
import time
from des_socket_utils import encrypt_des_cbc, build_packet

SERVER_IP = os.getenv('SERVER_IP', '26.182.185.145')
SERVER_PORT = int(os.getenv('SERVER_PORT', '6000'))
MESSAGE_ENV = os.getenv('MESSAGE')
LOG_FILE = os.getenv('SENDER_LOG_FILE', '')


def get_message() -> bytes:
    if MESSAGE_ENV is not None:
        return MESSAGE_ENV.encode('utf-8')
    plain = input("Nhập bản tin: ")
    return plain.encode('utf-8')


def main() -> None:
    try:
        plain = get_message()
        key, iv, cipher_bytes = encrypt_des_cbc(plain)
        overall = build_packet(key, iv, cipher_bytes)

        # Retry logic for connection
        max_retries = 3
        for attempt in range(max_retries):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((SERVER_IP, SERVER_PORT))
                    s.sendall(overall)
                break  # Connection successful
            except (ConnectionRefusedError, socket.timeout) as e:
                if attempt < max_retries - 1:
                    print(f"[-] Kết nối thất bại (lần {attempt + 1}), thử lại...", file=sys.stderr)
                    time.sleep(0.5)
                else:
                    print(f"[-] Kết nối thất bại sau {max_retries} lần: {e}", file=sys.stderr)
                    raise

        lines = [
            "[+] Đã gửi bản mã.",
            f"Key: {key.hex()}",
            f"IV: {iv.hex()}",
            f"Ciphertext: {cipher_bytes.hex()}",
        ]
        for line in lines:
            print(line)

        if LOG_FILE:
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n')
    except Exception as e:
        print(f"[-] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
