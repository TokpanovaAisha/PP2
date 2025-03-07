# Write a Python program to copy the contents of a file to another file

def copy(file, copy_file):
    try:
        with open(file, 'r') as reading:
            with open(copy_file, 'w') as copy_f:
                for line in reading:
                    copy_f.write(line)
        print("File has been copied")
    except Exception as e:
        print("Error", str(e))


file = "C:\\Users\\Aisha\\Desktop\\pp2\\Lab6\\dir-and-files\\for7task.txt"
copy_file = "C:\\Users\\Aisha\\Desktop\\pp2\\Lab6\\dir-and-files\\for7taskcopy.txt"

copy(file, copy_file)