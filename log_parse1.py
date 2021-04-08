import time
while 1:
    infile=r"path_to_your_log_file"
    with open(infile) as line:
        line = line.readline()
    for text in line:
        if not line:
            time.sleep(1)
            file.seek(infile)
        else:
            print(line)
