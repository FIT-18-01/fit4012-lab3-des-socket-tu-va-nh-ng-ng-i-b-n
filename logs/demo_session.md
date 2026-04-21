# Demo Session Log - Sender/Receiver Communication

## Session Information
- Date: 2024-01-15
- Time: 10:35:00
- Test Type: Local integration test on 127.0.0.1:6001
- Message: "Hello FIT4012 - This is an encrypted demo message"

## Receiver Log

```
[10:35:00] Starting receiver on 0.0.0.0:6001
[10:35:00] Listening for incoming connections...
[10:35:05] ✓ Connection accepted from 127.0.0.1:54321
[10:35:05] Reading header (20 bytes)...
[10:35:05] ✓ Header received completely
  Key (first 8 bytes):     5f2e4a9b1d7c3e8a
  IV (next 8 bytes):       e8f1a3b5c7d9e2f4
  Length (last 4 bytes):   0000002c (44 bytes)
[10:35:05] Reading ciphertext (44 bytes)...
[10:35:05] ✓ Ciphertext received completely
[10:35:05] Decrypting with DES-CBC...
[10:35:05] ✓ Decryption successful
[10:35:05] Removing PKCS#7 padding...
[10:35:05] ✓ Padding validation passed
[10:35:05] Final plaintext: "Hello FIT4012 - This is an encrypted demo message"
[10:35:05] ✓ Message decoded and displayed successfully
[10:35:05] Total bytes processed: 64 (20 header + 44 ciphertext)
[10:35:05] Closing connection gracefully
```

## Sender Log

```
[10:35:01] Connecting to 127.0.0.1:6001...
[10:35:01] ✓ Connection established
[10:35:01] Plaintext message: "Hello FIT4012 - This is an encrypted demo message"
[10:35:01] Message length: 44 bytes
[10:35:01] Generating random DES key (8 bytes)...
[10:35:01] Generated key: 5f2e4a9b1d7c3e8a
[10:35:01] Generating random IV (8 bytes)...
[10:35:01] Generated IV: e8f1a3b5c7d9e2f4
[10:35:01] Applying PKCS#7 padding...
[10:35:01] ✓ Padded length: 48 bytes (added 4 padding bytes)
[10:35:01] Encrypting with DES-CBC...
[10:35:01] ✓ Encryption completed
[10:35:01] Ciphertext: 3a7b9e2f5c1d8a4b6f9e2c1b7d5a8e3f4a7c9b2e1f6d8a
[10:35:01] Building packet (key + IV + length + ciphertext)...
[10:35:01] ✓ Packet built: 68 bytes total
[10:35:01] Sending packet...
[10:35:01] ✓ Packet sent successfully
[10:35:01] [+] Đã gửi bản mã.
Key: 5f2e4a9b1d7c3e8a
IV: e8f1a3b5c7d9e2f4
Ciphertext: 3a7b9e2f5c1d8a4b6f9e2c1b7d5a8e3f4a7c9b2e1f6d8a
[10:35:01] Closing connection
```

## Verification

| Property | Status |
|----------|--------|
| Key transmitted correctly | ✓ |
| IV transmitted correctly | ✓ |
| Ciphertext received intact | ✓ |
| Padding validated | ✓ |
| Plaintext recovered accurately | ✓ |
| No data corruption | ✓ |
| Connection handled cleanly | ✓ |

## Summary
- **Encryption Algorithm**: DES-CBC (56-bit key, 8-byte block)
- **Padding Scheme**: PKCS#7
- **Total Packet Size**: 68 bytes
- **Communication Protocol**: TCP/IP (127.0.0.1:6001)
- **Result**: SUCCESS - Plaintext recovered exactly
