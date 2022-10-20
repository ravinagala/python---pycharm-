l1 = [1, 2, 3]
l2 = [10, 20, 15, 5]
for r1, r2 in zip(l1, l2, strict=False):
    print(r1 * r2)
