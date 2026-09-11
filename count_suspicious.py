log = "LOGIN FAILED FAILED SUCCESS FAILED LOGIN FAILED SUCCESS"

failed_count = 0
success_count = 0

for word in log.split():
  if word == "FAILED":
    failed_count += 1
  elif word == "SUCESS":
    success_count += 1

print(f"FAILED: {failed_count}")
print(f"SUCCESS: {success_count}")
