h, b, c, s = input().split(" ")
h = int(h)
b = int(b)
c = int(c)
s = int(s)

bit = h * b * c * s
mb = bit / 8 / 1024 / 1024

print("{:.1f} MB".format(mb))