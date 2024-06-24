import mscfunc


def writetofile(filename, inputdata=[]):
    if inputdata:
        print(f"{filename} - writing")
        with open(f'{filename}', 'a', encoding="utf-8") as f:
            for output in inputdata:
                f.write(f"{output}\n")
            print(f"{filename} - complete")


xdata = "asdfasdfasfdasdfsafdsafd"
# mscfunc.writestringtofile("test.txt", [xdata])
writetofile("test.txt", [xdata])
xdata = "asdfasdfasfdasdfsafdsafd2"
writetofile("test.txt", [xdata])
