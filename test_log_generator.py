import random
import time
from datetime import datetime

error_samples = [
    "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
    "SyntaxError: invalid syntax at line 42",
    "ValueError: invalid literal for int() with base 10: 'abc'",
    "AttributeError: 'NoneType' object has no attribute 'get'",
    "NameError: name 'undefined_variable' is not defined",
    "ImportError: No module named 'nonexistent_module'",
    "IndexError: list index out of range",
    "KeyError: 'missing_key'",
    "FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'",
    "ZeroDivisionError: division by zero",
    "RecursionError: maximum recursion depth exceeded",
    "MemoryError: Unable to allocate memory",
    "ConnectionError: Failed to establish connection to database",
    "[ERROR] 404 Not Found - /api/users/123",
    "[ERROR] 500 Internal Server Error - Database query failed",
    "[ERROR] 403 Forbidden - Access denied to resource",
    "RuntimeError: Something went wrong in the application",
    "TimeoutError: Request timed out after 30 seconds",
    "PermissionError: [Errno 13] Permission denied: '/protected/file.txt'",
]


def generate_test_logs(filename='test.log', count=50, interval=2):
    print(f"Generating {count} test log entries to {filename}")
    print(f"Interval: {interval} seconds between logs")
    print("Press Ctrl+C to stop\n")

    with open(filename, 'a') as f:
        try:
            for i in range(count):
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                error = random.choice(error_samples)
                log_entry = f"[{timestamp}] {error}\n"

                f.write(log_entry)
                f.flush()

                print(f"[{i + 1}/{count}] {log_entry.strip()}")

                if i < count - 1:
                    time.sleep(interval)
        except KeyboardInterrupt:
            print("\n\nLog generation stopped by user")


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else 'test.log'
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    interval = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    generate_test_logs(filename, count, interval)