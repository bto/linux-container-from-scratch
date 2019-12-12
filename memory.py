with open("/dev/urandom", "rb") as f:
    data = b'';
    i = 0;
    while True:
        data += f.read(1048576)
        i += 1
        print("%dmb" % (i * 1, ))
