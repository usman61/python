# app.py
import time

# Append a string to a text file
file_path = "output.txt"
message = "Hello, World!"

# Open the file in append mode and write the message
with open(file_path, "a") as file:
    file.write(message + "\n")

print(f"Message appended to {file_path}.")
print("Keeping the container alive. Press Ctrl+C to stop.")

# Keep the script running indefinitely
while True:
    time.sleep(60)  # Sleep for 60 seconds in each loop
