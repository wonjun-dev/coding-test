date = input()
ymd = date.split(".")
d, m, y = int(ymd[-1]), int(ymd[1]), int(ymd[0])
print("{:02d}-{:02d}-{:04d}".format(d, m, y))
