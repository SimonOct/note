from Counter import Counter
c1 = Counter()
print(c1)
print(c1.getValue())
print(str(c1))
c1.increment()
print(c1)
c1.increment(5)
print(c1)
c1.reset()
print(c1)
c2 = Counter()
print(Counter.instance)
print(c1 == c1)
print(c1 == 0)
print(c1 == c2)
c2.increment()
print(c1 == c2)