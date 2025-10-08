# read   r w a r+ w+
# write
FILE_PATH = r"E:\Python-B14\Files\file_handling\test.txt"
f = open(FILE_PATH, "r")
# f.writelines(["acdc\n", "grtgrtg\n", "fergege"])


# data = f.read()
# print(f.closed)
# f.close()
# print(f.closed)



class FileOperation:
    def __init__(self, file_path, mode):
        print("in init")
        self.file = file_path
        self.mode = mode

    def __enter__(self):
        print("in enter")
        self.opened_file = open(self.file, self.mode)
        return self.opened_file

    def __exit__(self, exc_type, exc_value, traceback):
        print("in exit")
        self.opened_file.close()
        
with FileOperation(FILE_PATH, "r") as f:
    print("in with")
    print(f.read())
    print(f.closed)


# print(f.closed)

# with open(FILE_PATH, "r") as f:
#     # print(f.read())
#     print(f.closed)


# print(f.closed)



# {1: 6, 2: 3, 5:1}
# def get_total_word_count(wd, is_case_sensitive=True):
#     if is_case_sensitive:
#         words = data.split()
#     else:
#         words = data.lower().split()
#         wd = wd.lower()
#     words.count(wd)


# get_total_word_count("The", False)


# def get_total_chars():
    # print(len(data))


# get_total_chars()

# {"after": 5, "also": 4}

# def get_initial_of_words():
#     words = data.split()
#     print(set(map(lambda x: x[0], words)))

# get_initial_of_words()
# def get_word_len_mapping():
#     print({wd: len(wd) for wd in data.split()})

# get_word_len_mapping()

# dictionary -- key word: value len(word) 


# def get_word_by_initial(letter):
#     print([wd for wd in data.lower().split() if wd.startswith(letter.lower())])

# def get_word_by_initial(letter):
#     words = data.lower().split()
#     print(list(filter(lambda x: x.startswith(letter.lower()), words)))


# get_word_by_initial("A")

# def get_no_of_words():
#     print(len(data.split()))

# get_no_of_words()



# data = f.readlines()
# print(len(data))
# data = f.read(5)
# print(data)
# data = f.read()
# print(data)


# d1 = f.readline(2)
# d2 = f.readline(3)
# print(d1)
# print(d2)
# content = f.read()

# print(dir(f))
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'