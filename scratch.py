commandlist = ["show run"]
try:
    with open(filename, newline='') as f:
        commandlist = f.read().splitlines()
except:
    errorfunc.commandlist_error(filename)
