# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Đinh Mạnh Tú - MSSV: 1871020614
- Thành viên 2: - MSSV:

## Assets
- **Plaintext message**: Thông điệp gốc cần được giữ bí mật
- **Encryption key**: DES key 8 byte là chìa khóa để giải mã
- **Initialization vector (IV)**: IV dùng cho DES-CBC mode
- **Communication channel**: Đường truyền TCP giữa Sender và Receiver

## Attacker model
Attacker có khả năng:
1. Lắng nghe (eavesdropping) toàn bộ gói tin trên TCP socket
2. Sửa đổi (modify) nội dung gói tin khi đang truyền
3. Phát tán (replay) gói tin cũ
4. Có quyền truy cập mạng, nhưng không có quyền trực tiếp vào hệ thống của Sender/Receiver

## Threats
1. **Eavesdropping/Plaintext key exposure**: Vì key và IV được gửi dưới dạng plaintext (không mã hóa) trên cùng luồng TCP, attacker có thể lắng nghe và lấy được key, IV rồi dùng chúng để giải mã tất cả các message trong tương lai.
2. **Man-in-the-Middle (MITM)**: Attacker có thể chặn gói tin, sửa đổi ciphertext, rồi gửi tiếp. Nếu padding bị hỏng, Receiver có thể phát hiện, nhưng nếu sửa đổi một cách thông minh (bit flip), plaintext sẽ bị biến dạng mà không bị lỗi.
3. **Replay attack**: Attacker ghi lại một gói tin hợp lệ từ lần gửi trước, rồi gửi lại nó. Receiver sẽ giải mã thành cùng plaintext, dẫn đến thực hiện lại hành động cũ.

## Mitigations
1. **Key derivation và key distribution**: Sử dụng Diffie-Hellman hoặc ECDH để trao đổi key an toàn thay vì gửi key plaintext. Hoặc sử dụng pre-shared keys được phân phối ngoài kênh an toàn (out-of-band).
2. **Authentication và Integrity**: Thêm MAC (Message Authentication Code) hoặc HMAC vào mỗi gói tin để phát hiện sửa đổi và xác thực người gửi. Sử dụng authenticated encryption (AES-GCM) thay vì DES-CBC.
3. **Session management**: Sử dụng TLS/SSL để bảo vệ toàn bộ luồng giao tiếp. Hoặc thêm sequence number vào mỗi gói tin để phát hiện replay attack.
4. **Upgrade algorithm**: DES có key space chỉ 56 bit, đã coi là không an toàn. Nên chuyển sang AES (128/256 bit key).

## Residual risks
- Nếu dùng TLS, vẫn cần xử lý certificate management, key pinning, và version negotiation một cách cẩn thận.
- Nếu dùng pre-shared keys, rủi ro là key sharing, key rotation, và key compromise không được quản lý tốt.
- DES block size chỉ 64 bit, với AES-GCM vẫn cần xử lý large message (>2^32 blocks) một cách đúng đắn.
- Threat từ bên trong (insider threat): Nếu Sender hoặc Receiver bị compromise, tất cả plaintext vẫn bị lộ.
