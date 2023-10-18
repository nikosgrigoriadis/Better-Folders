import os

# paths = ["C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test1", "C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test3"]
# pathd = ["C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test2", "C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test4"]
#paths = "C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test1"
#pathd = "C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\test2"
# filename = "FOLDERname"
paths = ""
pathd = ""
filename = ""
boollean = True


def Set_pathS(new_path):
    global paths
    paths = new_path


def Set_pathD(new_path):
    global pathd
    pathd = new_path


def Checkbox_value(get_value):
    global boollean
    boollean = get_value


def Set_input(fn):
    global filename
    filename = fn


def backend():
    if boollean:
        os.system('cmd /c "cd {} & mkdir \"{}\"'.format(pathd,
                                                        filename))
    while True:
        print(filename)
        print(paths)
        print(pathd)

        file_names = os.listdir(paths)

        for fn in file_names:
            extension = os.path.splitext(fn)[1]
            FolderName = extension.upper().replace('.', '')
            if boollean:
                os.system('cmd /c "cd "{}\\{}" & mkdir "{}""'.format(pathd, filename, FolderName))
                os.system('cmd /c "cd "{}  '
                          '& move "{}\\{}" '
                          '"{}\\{}\\{}" '.format(paths, paths, fn, pathd, filename, FolderName))
            else:
                os.system('cmd /c "cd "{}" & mkdir {}"'.format(pathd, FolderName))
                os.system('cmd /c "cd "{}  '
                          '& move "{}\\{}" '
                          '"{}\\{}" '.format(paths, paths, fn, pathd, FolderName))


#backend()
