# http://stackoverflow.com/questions/36267874/how-to-re-order-bytes-in-a-python-hex-string-and-convert-to-long/36268144#36268144
s = "20D788028A4B59FB3C07050E2F30"
t = "".join([s[i-2:i] for i in range(8,0,-2)])
print int(t, 16) * 1.0 / pow(2,20)
print int(t, 16) * 1.0 / (1 << 20)
print int(t, 16) >> 20
