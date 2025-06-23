import os

# 📂 What is File Handling?
# File handling allows you to:

# Read data from files

# Write or append data to files

# Work with files using different modes like text or binary




# ✅ 2. File Modes
# Mode	Name	Description
# 'r'	Read	Default mode. Fails if file doesn't exist
# 'w'	Write	Overwrites file. Creates if doesn't exist
# 'a'	Append	Adds to end. Creates if doesn't exist
# 'b'	Binary	Used with 'rb', 'wb' for non-text files
# 'x'	Exclusive Create	Fails if file exists



# with open("test.txt", "w") as file:
#         #   content = file.read()
#         #   line = file.readline()
#         #   lines = file.readlines()
#           file.write("Hello this is a new line!\n")
#           file.write("Hello this is a new line 2!\n")
#         #   print(line)
#         #   print(lines)
#         #   print(content)

# with open("test.txt", "w") as file:
#     file.write("Hello, Mirajul!\n")
#     file.write("This will overwrite existing content.\n")


# with open("test.txt", "a") as file:
#     file.write("This will be added without deleting existing data.\n")
# with open("image.jpg", "rb") as img:
#     data = img.read()

# with open("copy.jpg", "wb") as copy:
#     copy.write(data)


if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")