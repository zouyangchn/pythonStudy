from pythonStudy import Hello

h = Hello()
h.hello('zouyang')
print(type(Hello))
print(type(h))


def fn(self, name='world'):
    print('Helllo, %s' % name)


Hello1 = type('Hello1', (object,), dict(hello1=fn))
t = Hello1().hello1('jack')
print(type(Hello1))
print(type(t))


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


l1 = MyList()
l1.add(1)
print(l1)

l2 = list()
# l2.add(2)
print(l2)


# ===================================
# ===========简==单==ORM=============#
# ===================================

# 首先定义字段类
# 1，字段基础类
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 2,各种字段类
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 接着编写元类创建类

# 1，编写metaclass类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model :%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 2,编写基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r''' Model' object has no attrbute'%s''' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'inser into %s(%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL :%s' % sql)
        print('ARDS:%s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='jack', email='123@qq.com', password='my-pwd')
u.save()
