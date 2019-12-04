

import struct

#struct模块来解决bytes和其他二进制数据类型的转换。
#1.struct的pack函数把任意数据类型变成bytes
#'>I'：  >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
b=struct.pack('>I', 10240099)
print(b)


#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
c=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(c)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

t=struct.unpack('<ccIIIIIIHH', s)
print(t)