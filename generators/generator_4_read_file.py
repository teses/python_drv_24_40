"""
Datei einlesen

mit with die Datei einlesen und mit yield zeilenweise bearbeiten


"""

def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def datei_verarbeiten(file_path, callback):
    for zeile in read_file_line_by_line(file_path):
        callback(zeile)


############################################################
result = list(filter(lambda x: "google" in x, read_file_line_by_line("../data/access.anonym.log")))
print(len(result))
print("#"*50)
for r in result:
    print(r)

###########################################################






"""
test = read_file_line_by_line("../data/access.anonym.log")
print(next(test))
print(next(test))


#for zeile in read_file_line_by_line("../data/access.anonym.log"):
#    print(zeile)



import sys
normal = sys.getsizeof(read_file("..\\data\\access.anonym.log"))
generator = sys.getsizeof(read_file_line_by_line("..\\data\\access.anonym.log"))

print(normal)
print(generator)
"""

