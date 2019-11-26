import pickle


d = dict(name='Bob', age=20, score=88)

s=pickle.dumps(d)
print(s)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()