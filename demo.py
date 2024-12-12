# app.py
# Append a string to a text file
file_path = "output.txt"
message = "Hello, World!"

# Open the file in append mode and write the message
with open(file_path, "a") as file:
    file.write(message + "\n")

print(f"Message appended to {file_path}.")
