# LAB 3 - HƯỚNG DẪN HOÀN THÀNH

Chào bạn! Dưới đây là hướng dẫn hoàn thành Lab 3 một cách đơn giản.

## 1️⃣ CẢI ĐẶT PYTHON VÀ DEPENDENCIES

### Trên Windows:
```bash
# Cài Python 3.9+ từ https://www.python.org/downloads/
# Kiểm tra cài thành công
python --version

# Di chuyển vào thư mục lab
cd c:\Users\Admin\Documents\Lab\fit4012-lab3-des-socket-tu-va-nh-ng-ng-i-b-n

# Tạo virtual environment
python -m venv .venv

# Kích hoạt virtual environment
.venv\Scripts\activate

# Cài dependencies
pip install -r requirements.txt
```

### Trên macOS/Linux:
```bash
python3 --version
cd ~/Documents/Lab/fit4012-lab3-des-socket-tu-va-nh-ng-ng-i-b-n
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2️⃣ CHẠY CÁC TEST

```bash
# Chạy tất cả tests (6 test cases)
pytest tests/ -v

# Chạy một test file cụ thể
pytest tests/test_padding_and_header.py -v

# Chạy tests với output chi tiết
pytest tests/ -v -s
```

**Kết quả mong đợi**: Tất cả 6 tests phải PASS ✓

## 3️⃣ CHẠY SENDER & RECEIVER (LOCAL DEMO)

### Terminal 1 - Khởi động Receiver:
```bash
RECEIVER_PORT=6001 python receiver.py
```

Bạn sẽ thấy:
```
Đang lắng nghe 0.0.0.0:6001...
```

### Terminal 2 - Khởi động Sender:
```bash
SERVER_IP=127.0.0.1 SERVER_PORT=6001 MESSAGE="Xin chao FIT4012" python sender.py
```

Bạn sẽ thấy ở Sender:
```
[+] Đã gửi bản mã.
Key: 4d3a5f8e2b9c1f7a
IV: a1b2c3d4e5f6a7b8
Ciphertext: 7e2f9c4b8d1e6a3f...
```

Bạn sẽ thấy ở Receiver:
```
Kết nối từ ('127.0.0.1', 54321)
[+] Bản tin gốc: Xin chao FIT4012
```

## 4️⃣ LƯỚI KIỂM TRA ĐỂ NỘP BÀI

### Deliverables bắt buộc:
- ✅ `README.md` - Đã điền đầy đủ team info, task division
- ✅ `report-1page.md` - Đã điền mục tiêu, phân công, cách làm, kết quả, kết luận
- ✅ `threat-model-1page.md` - Đã phân tích assets, attacker model, threats, mitigations, residual risks
- ✅ `peer-review-response.md` - Đã ghi nhận góp ý chéo và sửa chữa
- ✅ `tests/` - Có 6 tests (conftest + 5 test files)
- ✅ `logs/` - Có 3 log files minh chứng:
  - `test_run_log.md` - Log chạy 6 test cases
  - `demo_session.md` - Log demo sender/receiver
  - `unittest_execution.md` - Log chi tiết test execution
- ✅ `requirements.txt` - pycryptodome + pytest
- ✅ Code files: `sender.py`, `receiver.py`, `des_socket_utils.py` - Đã hoàn chỉnh

### Toàn bộ structure:
```
fit4012-lab3-des-socket-tu-va-nh-ng-ng-i-b-n/
├── README.md                           ✅ Filled
├── report-1page.md                     ✅ Filled
├── threat-model-1page.md               ✅ Filled
├── peer-review-response.md             ✅ Filled
├── requirements.txt                    ✅ Created
├── sender.py                           ✅ Complete
├── receiver.py                         ✅ Complete
├── des_socket_utils.py                 ✅ Complete
├── tests/
│   ├── conftest.py                    ✅ OK
│   ├── test_padding_and_header.py     ✅ OK
│   ├── test_sender_receiver_local.py  ✅ OK
│   ├── test_sender_receiver_contract.py ✅ OK
│   ├── test_wrong_key_negative.py     ✅ OK
│   └── test_tamper_negative.py        ✅ OK
└── logs/
    ├── .gitkeep
    ├── test_run_log.md                ✅ Created
    ├── demo_session.md                ✅ Created
    └── unittest_execution.md          ✅ Created
```

## 5️⃣ CHUẨN BỊ CHO DEMO (QUY TRÌNH TRÌNH BÀY)

### Bước 1: Giới thiệu hệ thống (1 phút)
```
- Hệ thống Sender/Receiver qua TCP socket
- Mã hóa DES-CBC, key 8 byte, IV 8 byte
- PKCS#7 padding
- Packet format: key | IV | length | ciphertext
```

### Bước 2: Chạy demo (3 phút)
```bash
# Terminal 1
RECEIVER_PORT=6001 python receiver.py

# Terminal 2
SERVER_IP=127.0.0.1 SERVER_PORT=6001 MESSAGE="Demo message" python sender.py
```

### Bước 3: Chạy tests (2 phút)
```bash
pytest tests/ -v
```

### Bước 4: Trả lời câu hỏi
Giảng viên sẽ hỏi:

1. **DES-CBC là gì?**
   - DES: 56-bit key, 8-byte block size
   - CBC mode: Cipher Block Chaining, phụ thuộc vào block trước
   - IV: Initialization Vector, đảm bảo ciphertext khác nhau dù plaintext giống

2. **PKCS#7 padding như thế nào?**
   - Nếu cần thêm N byte padding, mỗi byte = N
   - Ví dụ: 6 bytes cần thêm, padding = 0x06 0x06 0x06 0x06 0x06 0x06
   - Unpad: Lấy byte cuối cùng làm pad length, kiểm tra tất cả padding bytes

3. **Threat model là gì?**
   - Key/IV gửi plaintext -> MITM lắng nghe được -> Critical flaw
   - Cần dùng Diffie-Hellman hoặc TLS để trao đổi key an toàn
   - DES đã yếu (56-bit), nên upgrade lên AES-256

4. **Làm thế nào để phát hiện tamper?**
   - Nếu tamper ciphertext, decryption sẽ cho padding sai
   - Unpad sẽ throw ValueError "Padding PKCS#7 không hợp lệ"
   - Nên dùng HMAC hoặc authenticated encryption (AES-GCM) tốt hơn

5. **Lý do phân chia công việc?**
   - Thành viên 1: Sender + encryption logic
   - Thành viên 2: Receiver + socket
   - Cả hai: Utils + testing + threat model (nhóm phải hiểu toàn bộ)

## 6️⃣ CÁC LỖI THƯỜNG GẶP & CÁCH FIX

### Lỗi: `No module named 'Crypto'`
```bash
# FIX: Cài pycryptodome
pip install pycryptodome
```

### Lỗi: `Address already in use`
```bash
# FIX: Thay đổi PORT
RECEIVER_PORT=6002 python receiver.py
SERVER_PORT=6002 python sender.py
```

### Lỗi: Receiver không kết nối được
```bash
# Kiểm tra IP/Port đúng không
# Windows: ipconfig
# macOS/Linux: ifconfig
# Thử localhost 127.0.0.1 trước
```

### Lỗi: Padding không hợp lệ khi decrypt
```bash
# Kiểm tra key/IV đúng không
# Key/IV phải đúng 8 bytes
# Nếu socket lỗi, ciphertext có thể bị cut
```

## 7️⃣ GỌI VỚI GIẢNG VIÊN

Khi sẵn sàng, liên hệ GV để:
1. ✅ Kiểm tra code
2. ✅ Chạy demo trực tiếp
3. ✅ Nghe giải thích về threat model
4. ✅ Trả lời các câu hỏi về DES/CBC/padding/security

## 📌 CHÚC BẠN THÀNH CÔNG!

Nếu có vấn đề, kiểm tra:
- Python version 3.9+?
- pycryptodome cài đúng?
- Port không bị chiếm?
- Code không có syntax error?

Happy coding! 🎉
