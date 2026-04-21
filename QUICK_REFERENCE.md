# LAB 3 - QUICK REFERENCE CARD

## 🔐 DES-CBC Encryption

### Khái niệm
- **DES**: Data Encryption Standard, mã hóa đối xứng
- **Key size**: 56 bit (8 bytes) - YẾU, nên dùng AES-256 (256 bit)
- **Block size**: 8 bytes - CHỈ RỦI RO, nên dùng 16 bytes (AES)
- **CBC mode**: Cipher Block Chaining
  ```
  C_i = Encrypt(P_i ⊕ C_{i-1})
  P_i = Decrypt(C_i) ⊕ C_{i-1}
  C_0 = IV (Initialization Vector)
  ```

### IV (Initialization Vector)
- **Mục đích**: Đảm bảo ciphertext khác nhau dù plaintext giống
- **Size**: 8 bytes cho DES-CBC
- **Bắt buộc**: Phải random, không được tái sử dụng với cùng key
- **Bảo vệ**: Cần gửi kèm (không secret)

## 📦 PKCS#7 Padding

### Định nghĩa
Nếu plaintext không đầy đủ block cuối cùng (multiple of 8 bytes), thêm padding:
```
Padding length = 8 - (plaintext_length % 8)
Padding value = [padding_length, padding_length, ..., padding_length]
```

### Ví dụ
```
Plaintext: "Hello123" (8 bytes)
→ No padding needed? NO! Phải thêm 8 bytes padding (1 full block)
→ Padded: "Hello123" + [0x08 × 8]

Plaintext: "Hello" (5 bytes)
→ Need: 8 - 5 = 3 bytes
→ Padded: "Hello" + [0x03, 0x03, 0x03]
```

### Unpadding
```python
pad_len = data[-1]  # Lấy byte cuối
if pad_len < 1 or pad_len > 8:
    raise ValueError("Invalid padding")
if data[-pad_len:] != bytes([pad_len]) * pad_len:
    raise ValueError("Padding mismatch - data tampered!")
return data[:-pad_len]
```

## 📡 Packet Format

### Cấu trúc
```
[Key (8 bytes)][IV (8 bytes)][Length (4 bytes)][Ciphertext (N bytes)]
└─────────── 20 bytes header ────────────┘└─ Variable size ─┘
```

### Chi tiết
| Field | Size | Type | Purpose |
|-------|------|------|---------|
| Key | 8 bytes | Binary | DES decryption key |
| IV | 8 bytes | Binary | CBC mode IV |
| Length | 4 bytes | Big-endian uint32 | Ciphertext length |
| Ciphertext | N bytes | Binary | Encrypted plaintext |

### Ví dụ
```
Packet hex: 4d3a5f8e2b9c1f7a a1b2c3d4e5f6a7b8 0000002c 7e2f9c4b...

Breakdown:
- Key:        4d3a5f8e2b9c1f7a (8 bytes)
- IV:         a1b2c3d4e5f6a7b8 (8 bytes)
- Length:     0000002c = 44 bytes (ciphertext length)
- Ciphertext: 7e2f9c4b... (44 bytes)
```

## 🔄 Encryption Flow

```
┌─ Plaintext (e.g., "Xin chao FIT4012")
│
├─→ PKCS#7 Padding
│   └─ Padded: 48 bytes (original 16 + 32 padding)
│
├─→ DES-CBC Encryption
│   Input:  Padded plaintext + Key + IV
│   Output: Ciphertext (48 bytes)
│
├─→ Build Packet
│   [Key (8) + IV (8) + Length (4) + Ciphertext (48)]
│
└─→ Send over TCP Socket
```

## 🔓 Decryption Flow

```
┌─ TCP Socket receive packet
│
├─→ Parse Header (20 bytes)
│   Extract: Key, IV, Ciphertext Length
│
├─→ Receive Ciphertext (N bytes)
│
├─→ DES-CBC Decryption
│   Input:  Ciphertext + Key + IV
│   Output: Padded plaintext
│
├─→ Remove PKCS#7 Padding
│   Check last byte == padding value
│   Remove N bytes of padding
│
└─→ Output Plaintext
```

## ⚠️ Security Issues (Threat Model)

### Issue 1: Key Transmitted in Plaintext
```
❌ CURRENT: Sender sends [Key | IV | Length | Ciphertext] all in plaintext
❌ RISK: Attacker sniffs network → gets Key → can decrypt ALL messages
✅ FIX: Use Diffie-Hellman or TLS key exchange
```

### Issue 2: No Authentication
```
❌ CURRENT: No MAC/HMAC verification
❌ RISK: Attacker modifies ciphertext → garbage plaintext (sometimes caught by padding check, sometimes not)
✅ FIX: Use HMAC or authenticated encryption (AES-GCM)
```

### Issue 3: Weak Algorithm
```
❌ CURRENT: DES (56-bit key) is cryptographically broken
❌ RISK: Brute force attack is feasible
✅ FIX: Use AES-256
```

### Issue 4: No Replay Protection
```
❌ CURRENT: No sequence numbers or timestamps
❌ RISK: Attacker replays old message → same plaintext decrypted again
✅ FIX: Add sequence numbers or timestamps
```

## 🧪 Test Coverage

| Test | Purpose | Result |
|------|---------|--------|
| `test_pad_unpad_roundtrip` | Padding/unpadding logic | ✓ |
| `test_build_packet_contains_correct_length` | Packet format | ✓ |
| `test_local_sender_receiver_roundtrip` | End-to-end integration | ✓ |
| `test_protocol_contract_order_is_key_iv_length_ciphertext` | Protocol compliance | ✓ |
| `test_wrong_key_should_not_recover_original_plaintext` | Security (wrong key) | ✓ |
| `test_tampered_ciphertext_should_fail_or_change_plaintext` | Integrity (tamper detection) | ✓ |

## 💡 Key Takeaways

1. **DES-CBC requires IV** - Random IV per message, send with ciphertext
2. **PKCS#7 padding is critical** - Validation catches some tampering
3. **Key distribution is the weak point** - Lab sends key plaintext (intentional flaw for learning)
4. **Authenticated encryption > plain encryption** - Add MAC/HMAC or use AES-GCM
5. **Test everything** - Unit tests + integration tests + negative tests
6. **Threat modeling matters** - Know your security assumptions and violations

## 📚 References

### Commands
```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_padding_and_header.py::test_pad_unpad_roundtrip -v

# Run with coverage
pytest tests/ --cov=. -v

# Start receiver
python receiver.py

# Start sender
MESSAGE="Hello" python sender.py
```

### Environment Variables
```bash
# Sender
SERVER_IP=127.0.0.1
SERVER_PORT=6000
MESSAGE="Your message here"

# Receiver
RECEIVER_HOST=0.0.0.0
RECEIVER_PORT=6000
SOCKET_TIMEOUT=10
```

## 🎯 Demo Checklist

- [ ] Python 3.9+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] All 6 tests pass (`pytest tests/ -v`)
- [ ] Receiver starts and listens
- [ ] Sender connects, sends encrypted message
- [ ] Receiver decrypts correctly
- [ ] Key/IV/Ciphertext logged properly
- [ ] Can explain threat model
- [ ] Can explain why DES is weak
- [ ] Can explain PKCS#7 padding
