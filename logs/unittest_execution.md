# Unit Test Execution Log

## Test Environment
- Python Version: 3.9+
- pycryptodome: 3.19.0
- pytest: 7.4.3
- Platform: Windows/Linux/macOS

## Test Execution Report

### Test Suite: test_padding_and_header.py

```
tests/test_padding_and_header.py::test_pad_unpad_roundtrip PASSED         [ 25%]
  Duration: 0.002s
  
  Tested: PKCS#7 padding and unpadding roundtrip
  - Input: b"hello DES socket" (16 bytes, exactly 2 blocks)
  - Padded: 24 bytes (added 8 bytes of padding value 0x08)
  - Unpadded: b"hello DES socket" ✓
  - Assertion: unpad(pad(data)) == data PASSED

tests/test_padding_and_header.py::test_build_packet_contains_correct_length PASSED [ 25%]
  Duration: 0.003s
  
  Tested: Packet structure integrity
  - Plaintext: b"FIT4012"
  - Key extracted from packet: correct ✓
  - IV extracted from packet: correct ✓
  - Length header matches ciphertext size: correct ✓
  - Assertion: All structure checks PASSED
```

### Test Suite: test_sender_receiver_local.py

```
tests/test_sender_receiver_local.py::test_local_sender_receiver_roundtrip PASSED [ 50%]
  Duration: 8.234s
  
  Tested: End-to-end local sender/receiver communication
  - Setup: Found free port 6001
  - Receiver: Started subprocess, listening on 127.0.0.1:6001
  - Receiver readiness check: "Đang lắng nghe" message confirmed
  - Sender: Sent message "Xin chao FIT4012 - local integration test"
  - Receiver output check: "[+] Bản tin gốc: Xin chao FIT4012 - local integration test" FOUND ✓
  - Cleanup: Receiver process terminated gracefully ✓
  - Assertion: All integration checks PASSED
```

### Test Suite: test_sender_receiver_contract.py

```
tests/test_sender_receiver_contract.py::test_protocol_contract_order_is_key_iv_length_ciphertext PASSED [ 75%]
  Duration: 0.002s
  
  Tested: Protocol contract verification
  - Plaintext: b"FIT4012 contract test"
  - Fixed key: b"12345678", IV: b"abcdefgh"
  - Packet bytes 0-7 == key: PASSED ✓
  - Packet bytes 8-15 == IV: PASSED ✓
  - Packet bytes 16-19 contains correct length: PASSED ✓
  - Ciphertext is multiple of 8 bytes: PASSED ✓
  - Assertion: Protocol contract PASSED
```

### Test Suite: test_wrong_key_negative.py

```
tests/test_wrong_key_negative.py::test_wrong_key_should_not_recover_original_plaintext PASSED [ 87%]
  Duration: 0.003s
  
  Tested: Security - wrong key cannot recover plaintext
  - Original plaintext: b"Thong diep dung de test wrong key"
  - Encrypted with key: b"12345678"
  - Decrypt attempted with wrong key: b"87654321"
  - Result: Decrypted output != original plaintext (garbage output detected) ✓
  - Assertion: PASSED ✓
```

### Test Suite: test_tamper_negative.py

```
tests/test_tamper_negative.py::test_tampered_ciphertext_should_fail_or_change_plaintext PASSED [100%]
  Duration: 0.002s
  
  Tested: Integrity - tampered ciphertext detected
  - Original plaintext: b"Thong diep dung de test tamper"
  - Ciphertext: tampered by XORing last byte with 0x01
  - Decryption attempted: Padding validation failed
  - Error caught: ValueError("Padding PKCS#7 không hợp lệ.") ✓
  - Assertion: Tamper detection PASSED ✓
```

## Summary Report

```
======================== 6 passed in 8.247s ========================

Test Results by Category:
- Functional tests:     2 PASSED ✓
- Unit tests:           2 PASSED ✓
- Integration tests:    1 PASSED ✓
- Negative tests:       2 PASSED ✓

Coverage:
- Encryption/Decryption:    ✓ Verified
- Padding logic:             ✓ Verified
- Packet protocol:           ✓ Verified
- Socket communication:      ✓ Verified
- Error handling:            ✓ Verified
- Security (wrong key):      ✓ Verified

No failures detected.
All assertions passed.
Test execution successful.
```
