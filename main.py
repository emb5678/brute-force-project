import time 

minPass = 999080000
maxPass = 999089999

userPass = int(input("Enter the password to find: "))
start_time = time.perf_counter()
for password in range(minPass, maxPass + 1):
    print(f"Checking password: {password}")
    if password == userPass:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Password found: {password} in {elapsed_time:.2f} seconds")
        with open("found_password.txt", "w") as f:
            f.write(
                f"Password: {password}\n"
                f"Time taken: {elapsed_time:.2f} seconds\n"
            )
        break