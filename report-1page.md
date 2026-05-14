# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Đinh Mạnh Tú - MSSV: 1871020614
- Thành viên 2: Hà Minh Quân  - MSSV: 187102470

## Mục tiêu
Bài lab này nhằm xây dựng một hệ thống gửi và nhận dữ liệu mã hoá DES qua TCP socket. Chúng tôi sẽ triển khai Sender tạo key DES 8 byte và IV 8 byte, mã hoá bằng DES-CBC với PKCS#7 padding, rồi gửi qua socket. Receiver sẽ nhận dữ liệu, giải mã và hiển thị bản rõ. Qua đó, chúng tôi hiểu sâu về luồng giao tiếp mã hoá, vai trò của key/IV/padding, và phân tích các mối đe doạ bảo mật.

## Phân công thực hiện
- Thành viên 1 phụ trách: Sender module và logic mã hoá DES-CBC
- Thành viên 2 phụ trách: Receiver module và xử lý socket
- Cả hai cùng làm: DES utils library (pad/unpad, encrypt/decrypt, build_packet/parse_header), viết test cases, phân tích threat model, và lập tài liệu

## Cách làm
Chúng tôi sử dụng thư viện pycryptodome để triển khai DES-CBC encryption. Sender đọc bản tin từ stdin hoặc biến môi trường MESSAGE, tạo ngẫu nhiên 8-byte key và IV, mã hoá bằng DES-CBC mode với PKCS#7 padding, sau đó xây dựng packet theo format: 8-byte key + 8-byte IV + 4-byte length header (big-endian) + ciphertext. Receiver lắng nghe trên TCP socket, nhận đúng thứ tự này, giải mã và in bản rõ. Chúng tôi viết 6 unit tests kiểm tra padding, packet structure, encryption/decryption roundtrip, socket communication, wrong key recovery, và tamper detection.

## Kết quả
Hệ thống hoạt động thành công. Sender có thể mã hoá và gửi bản tin, Receiver nhận đúng thứ tự và giải mã chính xác. Tất cả 6 test cases đều pass. Logs minh chứng được lưu trong thư mục logs/ cho các ca kiểm thử: (1) roundtrip encryption/decryption, (2) local sender-receiver integration test, (3) protocol contract verification, (4) wrong key should not recover plaintext, (5) tampered ciphertext detection.

## Kết luận
Chúng tôi đã hiểu rõ cách triển khai mã hoá DES-CBC và giao tiếp qua socket. Bài học kỹ thuật: PKCS#7 padding rất quan trọng, cần kiểm tra chặt chẽ khi giải mã. Bài học bảo mật: Thiết kế hiện tại gửi key/IV dưới dạng plaintext trên cùng luồng TCP, đây là điểm yếu nghiêm trọng. Hướng cải tiến: dùng Diffie-Hellman để trao đổi key an toàn, hoặc dùng TLS để bảo vệ toàn bộ luồng giao tiếp.
