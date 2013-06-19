#-*- encoding:utf-8 -*-

from common import models,dictionary

def initializer(obj=None):
    def cmp_(f,s):
        if f[0]>s[0]:
            return 1
        elif f[0]==s[0]:
            return 0
        else:
            return -1
        
    def insert_data(base_name):
        values = None
        try:
            values = getattr(dictionary,base_name[5:])
            model = getattr(models,base_name)
        except Exception,e:
            raise e
        values = list(values)
        values.sort(cmp_)
        count = len(values)
        index = 0
        for code,name in values:
            index += 1
            print "insert %s (%s/%s)" %(base_name.lower(),index,count)
            model.objects.create(code=code,name=name)
    if obj:
        insert_data(obj)
    else:
        model_names = [m for m in dir(models) if  m.startswith("BASE_")]
        for name in model_names:
            insert_data(name)