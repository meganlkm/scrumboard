# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from mysite.ncsdd.models import *
from django1.contrib.auth.models import Group
import django
def genuser(uname,group):
    try:
        g=Group.objects.get(name=group)
        u=User()
        u.username=uname
        u.set_password("1")
        u.is_staff=True
        u.save()
        u.groups.add(g)
        u.save()
    except django.db.utils.IntegrityError,e:
        print e
def deluser(uname):
    u=User.objects.get(username=uname)
    u.delete()
def getuser(uname):
    u=User.objects.get(username=uname)
    print dir(u)
    print dir(u.groups)
    print (u.groups.all())
def genall():
    genuser("guofeifei","分析员")
    genuser("quhuayang","分析员")
    genuser("houhongxia","分析员")
    genuser("fengguan","分析员")
    genuser("pengxia","分析员")
    genuser("huyue","分析员")
    genuser("lidongling","分析员")
    genuser("shihuacao","销售")
    genuser("limeiling","管理员")
    genuser("yuxing","管理员")
    #genuser("shenxuejing","管理员")
    #genuser("chenjiwen","管理员")
if __name__ == "__main__":
    #genuser("guofeifei","分析员")
    #deluser("guofeifei")
    #getuser("mahongquan")
    genall()