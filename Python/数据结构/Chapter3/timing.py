import time

problemSize = 10_000_000
print("%12s%16s" % ("problemSize", "Seconds"))
for count in range(5):
    start = time.time()

    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
