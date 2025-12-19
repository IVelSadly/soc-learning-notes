# analyzer.py

failed_logins = 0

with open("sample.log", "r") as log:
    for line in log:
        if "FAILED_LOGIN" in line:
            failed_logins += 1

print("Log analysis result:")
print(f"Failed login attempts detected: {failed_logins}")

if failed_logins > 5:
    print("Warning: Possible brute force activity detected.")
else:
    print("No suspicious activity detected.")
