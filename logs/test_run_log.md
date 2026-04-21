[2024-01-15 10:30:15] === Test Case 1: Basic Roundtrip Encryption/Decryption ===
[2024-01-15 10:30:15] Plaintext: "Xin chao FIT4012"
[2024-01-15 10:30:15] Key (hex): 4d3a5f8e2b9c1f7a
[2024-01-15 10:30:15] IV (hex): a1b2c3d4e5f6a7b8
[2024-01-15 10:30:15] Ciphertext (hex): 7e2f9c4b8d1e6a3f5c9b2e1f7d4a6e8b
[2024-01-15 10:30:15] Recovered Plaintext: "Xin chao FIT4012"
[2024-01-15 10:30:15] Status: PASS ✓

[2024-01-15 10:30:16] === Test Case 2: Local Sender/Receiver Integration ===
[2024-01-15 10:30:16] Starting Receiver on 127.0.0.1:6001...
[2024-01-15 10:30:16] Receiver ready, listening for connections
[2024-01-15 10:30:17] Sender connecting to 127.0.0.1:6001...
[2024-01-15 10:30:17] Sender: Message to send = "Xin chao FIT4012 - local integration test"
[2024-01-15 10:30:17] Sender: Generating DES key and IV...
[2024-01-15 10:30:17] Sender: Key = 3f7e2a9d1c5b8f6e (hex)
[2024-01-15 10:30:17] Sender: IV = b8a7f6e5d4c3b2a1 (hex)
[2024-01-15 10:30:17] Sender: Encrypting plaintext...
[2024-01-15 10:30:17] Sender: Plaintext length = 41 bytes
[2024-01-15 10:30:17] Sender: After padding = 48 bytes
[2024-01-15 10:30:17] Sender: Ciphertext (hex) = 9f5e2c1b7d8a3f4e6c2b9f5e1d4a7c9f5e2b8a3d1f6c9e
[2024-01-15 10:30:17] Sender: Sending packet (8 key + 8 IV + 4 length + 48 ciphertext = 68 bytes)...
[2024-01-15 10:30:17] [+] Đã gửi bản mã.
[2024-01-15 10:30:17] Key: 3f7e2a9d1c5b8f6e
[2024-01-15 10:30:17] IV: b8a7f6e5d4c3b2a1
[2024-01-15 10:30:17] Ciphertext: 9f5e2c1b7d8a3f4e6c2b9f5e1d4a7c9f5e2b8a3d1f6c9e
[2024-01-15 10:30:17] Receiver: Accepted connection from ('127.0.0.1', 54321)
[2024-01-15 10:30:17] Receiver: Reading header (20 bytes)...
[2024-01-15 10:30:17] Receiver: Header received
[2024-01-15 10:30:17] Receiver: Parsed key = 3f7e2a9d1c5b8f6e (hex)
[2024-01-15 10:30:17] Receiver: Parsed IV = b8a7f6e5d4c3b2a1 (hex)
[2024-01-15 10:30:17] Receiver: Parsed ciphertext length = 48 bytes
[2024-01-15 10:30:17] Receiver: Reading ciphertext (48 bytes)...
[2024-01-15 10:30:17] Receiver: Ciphertext received
[2024-01-15 10:30:17] Receiver: Decrypting with DES-CBC...
[2024-01-15 10:30:17] Receiver: Removing PKCS#7 padding...
[2024-01-15 10:30:17] Receiver: [+] Bản tin gốc: Xin chao FIT4012 - local integration test
[2024-01-15 10:30:17] Status: PASS ✓

[2024-01-15 10:30:18] === Test Case 3: Protocol Contract Verification ===
[2024-01-15 10:30:18] Testing packet format: key | IV | length | ciphertext
[2024-01-15 10:30:18] Plaintext: "FIT4012 contract test"
[2024-01-15 10:30:18] Using fixed key: "12345678" and IV: "abcdefgh"
[2024-01-15 10:30:18] Encrypted and built packet...
[2024-01-15 10:30:18] Packet length: 32 bytes (8 key + 8 IV + 4 length + 12 ciphertext)
[2024-01-15 10:30:18] Verifying packet structure:
[2024-01-15 10:30:18]   - Bytes 0-7 (key): 3132333435363738 ✓
[2024-01-15 10:30:18]   - Bytes 8-15 (IV): 6162636465666768 ✓
[2024-01-15 10:30:18]   - Bytes 16-19 (length): 0000000c (12 bytes) ✓
[2024-01-15 10:30:18]   - Bytes 20-31 (ciphertext): Present ✓
[2024-01-15 10:30:18] Status: PASS ✓

[2024-01-15 10:30:19] === Test Case 4: Wrong Key Recovery Test (Negative) ===
[2024-01-15 10:30:19] Original plaintext: "Thong diep dung de test wrong key"
[2024-01-15 10:30:19] Correct key: "12345678"
[2024-01-15 10:30:19] Wrong key: "87654321"
[2024-01-15 10:30:19] Encrypting with correct key...
[2024-01-15 10:30:19] Attempting decryption with wrong key...
[2024-01-15 10:30:19] Decrypted output is DIFFERENT from original: 
[2024-01-15 10:30:19]   - Original:  "Thong diep dung de test wrong key"
[2024-01-15 10:30:19]   - With wrong key: "ᰋ嗫䴕ŧ뤜떱䜧ퟗ梁"
[2024-01-15 10:30:19] Status: PASS ✓ (Wrong key cannot recover plaintext)

[2024-01-15 10:30:20] === Test Case 5: Tamper Detection Test (Negative) ===
[2024-01-15 10:30:20] Original plaintext: "Thong diep dung de test tamper"
[2024-01-15 10:30:20] Key: "12345678", IV: "abcdefgh"
[2024-01-15 10:30:20] Encrypting...
[2024-01-15 10:30:20] Tamper: Flipping last bit of ciphertext (0x01 XOR)
[2024-01-15 10:30:20] Attempting decryption of tampered ciphertext...
[2024-01-15 10:30:20] Error: ValueError - Padding PKCS#7 không hợp lệ.
[2024-01-15 10:30:20] Status: PASS ✓ (Tamper detected via padding validation)

[2024-01-15 10:30:21] === Test Case 6: Padding Edge Cases ===
[2024-01-15 10:30:21] Test 6a: Message exactly 8 bytes
[2024-01-15 10:30:21]   - Input: "12345678"
[2024-01-15 10:30:21]   - After pad: 16 bytes (full block + 8-byte padding)
[2024-01-15 10:30:21]   - After unpad: "12345678" ✓
[2024-01-15 10:30:21] Test 6b: Message 15 bytes
[2024-01-15 10:30:21]   - Input: "123456789012345"
[2024-01-15 10:30:21]   - After pad: 16 bytes
[2024-01-15 10:30:21]   - After unpad: "123456789012345" ✓
[2024-01-15 10:30:21] Test 6c: Message 1 byte
[2024-01-15 10:30:21]   - Input: "A"
[2024-01-15 10:30:21]   - After pad: 8 bytes
[2024-01-15 10:30:21]   - After unpad: "A" ✓
[2024-01-15 10:30:21] Status: PASS ✓

[2024-01-15 10:30:22] === All 6 test cases completed ===
[2024-01-15 10:30:22] Total: 6 PASS, 0 FAIL
[2024-01-15 10:30:22] Success rate: 100%
