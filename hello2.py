hello = []

hello.append(2**5 * 2 + 8)
hello.append(101)
hello.append(108)
hello.append(int((1e10 + 1e2 + 0x08) % 1e10))
hello.append(111)

for element in hello:
    print(chr(element))
