l1 = [1, 2, 3]
l2 = [10, 11, 15, 20]

if len(l1) > len(l2):
    bl = l1
    sl = l2
else:
    bl = l2
    sl = l1
for idx, v in enumerate(bl):
    if idx < len(sl):
        sv = sl[idx]
    else:
        sv = 1
    print(v * sv)
