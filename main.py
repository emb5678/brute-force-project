import time 
import argparse

parser = argparse.ArgumentParser(description="Password Finder")

parser.add_argument("minPass", type=int, help="Minimum password value")
parser.add_argument("maxPass", type=int, help="Maximum password value")
parser.add_argument("userPass", type=int, help="Target password to find")
args = parser.parse_args()

minPass = args.minPass
maxPass = args.maxPass
userPass = args.userPass
attempts = 0

if minPass >= maxPass:
    print("Error: minPass should be less than maxPass")
    exit(1)

if not (minPass <= userPass <= maxPass):
    print("Error: target password should be within the specified range")
    exit(1)

start_time = time.perf_counter()

for password in range(minPass, maxPass + 1):

    print(f"Checking password: {password}")
    attempts += 1

    if password == userPass:

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"Password found: {password} in {elapsed_time:.2f} seconds")

        with open("found_password.txt", "w") as f:
            f.write(
                f"Password: {password}\n"
                f"Time taken: {elapsed_time:.2f} seconds\n"
                f"Attempts: {attempts}\n"
            )
        break
