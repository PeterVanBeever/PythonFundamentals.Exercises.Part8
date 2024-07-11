import os

def list_current_directory(dirname, file_handler):
    # check each item in directory - os.listdir
    for item in os.listdir(dirname):
        item_path = os.path.join(dirname, item)
        # check if item is directory
        if os.path.isdir(item_path):
            file_handler.write(f"{item_path}/\n")
        else:
            file_handler.write(f"{item_path}\n")

# open outout and print
with open("output.txt", "w") as file_handler:
    list_current_directory(".", file_handler)
