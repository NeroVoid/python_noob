'''
Mục tiêu:
Luyện viết hàm tách nhỏ bài toán.
Ứng dụng random (mô phỏng dữ liệu) và thao tác list.
Tính conversion rate và so sánh biến thể.

Mô tả:
Một chiến dịch A/B gửi email có hai biến thể A và B. Kết quả mỗi người dùng là 1 (có chuyển đổi) hoặc 0 (không).

Hãy viết chương trình:
(Tuỳ chọn) Sinh dữ liệu giả lập: dùng random.random() với ngưỡng xác suất khác nhau (ví dụ A: 0.12, B: 0.15) để tạo 100 kết quả cho mỗi biến thể.
Viết các hàm:
simulate_group(n, p) → trả về list độ dài n, mỗi phần tử là 1 với xác suất p, ngược lại 0.
conversion_rate(results) → trả về tỉ lệ chuyển đổi = sum(results) / len(results).
compare(a_results, b_results) → in CR của A, B và kết luận biến thể thắng (CR cao hơn).

In bảng tổng hợp:
Variant A: 100 users, 12 conversions → CR = 12.00%
Variant B: 100 users, 15 conversions → CR = 15.00%
Winner: B  (diff = 3.00%)
Variant A: 100 users, 12 conversions → CR = 12.00%
Variant B: 100 users, 15 conversions → CR = 15.00%
Winner: B  (diff = 3.00%)
Gợi ý:
Dùng round(x, 4) khi tính, và format phần trăm khi in.
Nếu đã học statistics, có thể in thêm độ lệch chuẩn (không bắt buộc).
'''