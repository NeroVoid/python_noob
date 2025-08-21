'''
logs_2 = [
    "# system boot",
    "2025-08-21T09:00:00Z,alice,SUCCESS",
    "2025-08-21T09:01:00Z,bob,FAIL",
    "2025-08-21T09:01:10Z,bob,FAIL",
    "2025-08-21T09:01:20Z,bob,FAIL",
     "2025-08-21T09:01:30Z,bob,FAIL",
     "2025-08-21T09:01:30Z,bob,FAIL",
    "",
    "2025-08-21T09:01:30Z,bob,FAIL",
    "2025-08-21T09:01:40Z,carol,SUCCESS",
    "2025-08-21T09:01:50Z,bob,FAIL",
    "END",
    "2025-08-21T09:02:00Z,alice,FAIL",  # không được xử lý vì sau END
] '
'''