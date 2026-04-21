# Peer Review Response

## Thông tin nhóm
- Thành viên 1: Người A - MSSV: 12345678
- Thành viên 2: Người B - MSSV: 87654321

## Thành viên 1 góp ý cho thành viên 2
- Phần Receiver code rất sạch, xử lý socket tốt. Tuy nhiên cần thêm error handling chi tiết hơn khi recv_exact bị timeout hoặc connection drop.
- Hàm parse_header nên validate dữ liệu bytes trước khi unpack, tránh struct.error.
- Suggestion: Thêm logging chi tiết hơn để debug, ví dụ log lại payload size và connection time.

## Thành viên 2 góp ý cho thành viên 1
- Sender module rất ổn định, message input từ ENV hoặc stdin hợp lý.
- Nhưng khi encrypt_des_cbc() được gọi mà không có key/iv argument, nó sẽ tạo random mỗi lần, điều này tốt cho security nhưng khó debug. Suggestion: Khi develop/test, có option để debug mode dùng fixed key.
- Code pad/unpad logic rất chính xác. Có thể thêm test case cho edge case: message dài chính xác bội số của 8 bytes.

## Nhóm đã sửa gì sau góp ý
1. Thêm try-except blocks trong receiver.py để xử lý ConnectionError khi socket bị đóng sớm hoặc timeout.
2. Thêm validation trong parse_header() để kiểm tra header length trước unpack, và xử lý struct.error.
3. Tăng logging: in ra header values (key hex, IV hex, length) khi receive, và connection address.
4. Thêm test case test_pad_even_multiple() để kiểm tra khi plaintext length là bội số chính xác của 8.
5. Cải thiện unpad() logic: check edge case khi data length < 1 hoặc pad_len > 8.
6. Thêm code comment giải thích từng bước encryption/decryption process.
