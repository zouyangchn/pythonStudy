import pickle

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)