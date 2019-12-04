import base64

#Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
r=base64.b64encode(b'binary\x00string')
#r=b'YmluYXJ5AHN0cmluZw=='
print(r)
s=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(s)

#标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
t1=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(t1)
t2=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(t2)