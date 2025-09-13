'''
Một công ty có danh sách công việc (tasks), mỗi công việc lưu:
[task_name, days_to_finish]
tasks = [
    ["Submit report", 3],
    ["Prepare slides", 5],
    ["Team meeting", 1]
]

Yêu cầu:
Lấy ngày hiện tại (datetime.datetime.now()).
Với mỗi công việc, tính deadline = now + timedelta(days_to_finish).
In danh sách công việc kèm deadline theo định dạng YYYY-MM-DD.

Output mong đợi (ví dụ chạy ngày 2025-08-28):
Submit report - Deadline: 2025-08-31
Prepare slides - Deadline: 2025-09-02
Team meeting - Deadline: 2025-08-29

'''