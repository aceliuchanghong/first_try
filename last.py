import pymysql
import operator
import sys
from time import sleep
db = pymysql.connect("69.171.68.72","吉良吉影","iloveheluo","HW" )
cursor = db.cursor()
keylogin=0;global tmp0;tmp0=0;global tmp1;global tmp;tmp=0

def index_of_str(s1, s2):
    n1=len(s1)
    n2=len(s2)
    for i in range(n1-n2+1):
        if s1[i:i+n2]==s2:
            return i+1
    else:
            return -1

def pi():
    print('欢迎来到这儿,查询生日在pi的第多少位小数请输入1,退出请输入0:')
    b=int(input())
    if b==0:
        print('bye!')
    elif b==1:
        a=''
        fp=open('pi.txt','r+')
        for line in fp.readlines():
            a=a+line
        fp.close()
        b=str(input('你的生日(格式如19980910):'))
        position=index_of_str(a, b)
        if position==-1:
            print('pi的前3550万位居然没有!')
        else:
            print(position)
def signin(name,password):
    k=1;keysign=0
    if len(name)>8 or len(password)>20:
        print('用户名必须小于8位且密码小于20位')
        k=0
    elif k==1:
        try:
            sql = "insert into my_hw\
            (sno,spwd)\
            values ('%s', '%s')" % \
            (name,password)
            cursor.execute(sql)
            db.commit()
            print ("ok,注册成功")
            keysign=1
        except:
            db.rollback()
            print ("Error:注册失败")
    elif k==0:
            print('用户名小于8位且密码小于20位')
            print ("Error:注册失败")
            print('注册请输入0,登录请输入1,退出系统请输入quit:')

def login(name,password):   
    pwd=[];
    sql="select spwd from my_hw where sno= '%s' "%(name)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.commit()
        pwd=results[0]
        if operator.eq(password,pwd[0]):
            print('login successful')
            global keylogin
            keylogin=1
        else:
            print ("密码或用户名不对")
            print('注册请输入0,登录请输入1,退出系统请输入quit:')
            keylogin=0
    except:
       db.rollback()
       print ("Error: login failed")

def insert(name,bkid,author):
    sql = "INSERT INTO my_book(bookname,bookid,auth) VALUES ('%s','%s','%s')"%(name,bkid,author)
    try:
        cursor.execute(sql)
        db.commit()
        print ("ok!")
    except:
        db.rollback()
        print ("oops!失败了qaq")
        

def delete(name,bkid,author):

    if tmp==1:
        sql="DELETE FROM my_book WHERE bookname ='%s'"%(name)
    elif tmp==2:
        sql="DELETE from my_book where bookid='%s'"%(bkid)
    elif tmp==3:
        sql="DELETE from my_book where auth='%s'"%(author)
    try:
        cursor.execute(sql)
        db.commit()
        print ("ok!删除成功")
    except:
        db.rollback()
        print ("oops!qaq,失败了")

def select(name='数学分析',bkid='008',author='靳勇飞'):
    if tmp0==1:
        sql="select * from my_book where bookname= '%s' "%(name)
    elif tmp0==2:
        sql="select * from my_book where bookid= '%s' "%(bkid)
    elif tmp0==3:
        sql="select * from my_book where auth= '%s' "%(author)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for x in results:
            fi=x[0]
            se=x[1]
            th=x[2]
            print("书名:%s\n编号:%s\n作者:%s"%(fi,se,th))
    except:
        db.rollback()
        print ("Error!qaq失败了")

def update(name='数学分析',nname='数学分析',bkid='008',nid='008',author='靳勇飞',nauth='靳勇飞'):
    if tmp1==1:
        sql1="update my_book set bookname='%s' where bookname= '%s' "%(nname,name)
        sql="select * from my_book where bookname= '%s' "%(nname)
    elif tmp1==2:
        sql1="update my_book set bookid='%s' where bookid= '%s' "%(nid,bkid)
        sql="select * from my_book where bookid= '%s' "%(nid)
    elif tmp1==3:
        sql1="update my_book set auth='%s' where auth= '%s' "%(nauth,author)
        sql="select * from my_book where auth= '%s' "%(nauth)
    try:
        cursor.execute(sql1)
        db.commit()
        cursor.execute(sql)
        results = cursor.fetchall()
        for x in results:
            fi=x[0]
            se=x[1]
            th=x[2]
            print("书名:%s\n编号:%s\n作者:%s"%(fi,se,th))
    except:
        db.rollback()
        print ("Error!qaq")


poem = '''
Hello,欢迎来到图书管理系统,我是Akane
管理图书需要登录(注意输入其他会死机!)
注册请输入0,登录请输入1,退出系统请输入quit:\n'''

for char in poem:
    sleep(0.01)
    sys.stdout.write(char)
while True:
    l_or_s=input()
    if l_or_s=='quit':
        print('舍不得你啊......')
        break
    elif int(l_or_s)==1:
        print ("输入名字:")
        name=input()
        print ("输入密码:")
        password=input()
        login(name,password)
        if keylogin==1:
            poem1 = '''恭喜登录成功,现在开始对图书进行管理吧!
你现在可以对图书经行查询,修改,删除,添加了(注意输入其他会死机!)
查询请输入0,修改请输入1,删除请输入2,添加请输入3,退出系统请输入quit:\n'''
            for char in poem1:
                sleep(0.01)
                sys.stdout.write(char)
            while True:
                tmpkey=input()
                if tmpkey=='quit':
                    print('注册请输入0,登录请输入1,退出系统请输入quit:')
                    break
                elif int(tmpkey)==0:
                    print('请输入查询的对象\n查询书名请输入0,查询书的编号请输入1,查询书的作者请输入2,退出系统请输入quit:')
                    while True:
                        bkid='008';name='数学分析';author='靳勇飞'
                        myselect=input()
                        if myselect=='quit':
                            print('查询请输入0,修改请输入1,删除请输入2,添加请输入3,退出系统请输入quit')
                            break
                        elif int(myselect)==0:
                            print('书名:')
                            name=input()
                            tmp0=int(myselect)+1
                        elif int(myselect)==1:
                            print('书的编号:')
                            bkid=input()
                            tmp0=int(myselect)+1
                        elif int(myselect)==2:
                            print('书的作者:')
                            author=input()
                            tmp0=int(myselect)+1
                        else:
                            print('别皮!')
                        select(name,bkid,author)
                        print('请输入查询的对象\n查询书名请输入0,查询书的编号请输入1,查询书的作者请输入2,退出系统请输入quit:')
                elif int(tmpkey)==1:
                    print('请输入修改的对象以及要修改成什么样子\n修改书名请输入0,修改书的编号请输入1,修改书的作者请输入2退出系统请输入quit:')
                    while True:
                        name='数学分析';nname='数学分析';bkid='008';nid='008';author='靳勇飞';nauth='靳勇飞'
                        myupdate=input()
                        if myupdate=='quit':
                            print('查询请输入0,修改请输入1,删除请输入2,添加请输入3,退出系统请输入quit')
                            break
                        elif int(myupdate)==0:
                            print('原来的书名:')
                            name=input()
                            print('要改成的书名:')
                            nname=input()
                            tmp1=int(myupdate)+1
                        elif int(myupdate)==1:
                            print('原来的书编号:')
                            bkid=input()
                            print('要改成的书编号:')
                            nid=input()
                            tmp1=int(myupdate)+1
                        elif int(myupdate)==2:
                            print('原来的书作者:')
                            author=input()
                            print('要改成的书作者:')
                            nauth=input()
                            tmp1=int(myupdate)+1
                        else:
                            print('别皮!')
                        update(name,nname,bkid,nid,author,nauth)
                        print('请输入修改的对象以及要修改成什么样子\n修改书名请输入0,修改书的编号请输入1,修改书的作者请输入2退出系统请输入quit')
                elif int(tmpkey)==2:
                    print('请输入删除的对象\n通过书名删除请输入0,通过书的编号删除请输入1,通过书的作者删除请输入2退出系统请输入quit:')
                    while True:
                        bkid='test';name='test';author='test'
                        mydelete=input()
                        if mydelete=='quit':
                            print('查询请输入0,修改请输入1,删除请输入2,添加请输入3,退出系统请输入quit')
                            break
                        elif int(mydelete)==0:
                            print('书名:')
                            name=input()
                            tmp=tmp+1
                        elif int(mydelete)==1:
                            print('书的编号:')
                            bkid=input()
                            tmp=tmp+1
                        elif int(mydelete)==2:
                            print('书的作者:')
                            author=input()
                            tmp=tmp+1
                        else:
                            print('别皮!')
                        delete(name,bkid,author)
                        print('请输入删除的对象\n通过书名删除请输入0,通过书的编号删除请输入1,通过书的作者删除请输入2退出系统请输入quit')
                elif int(tmpkey)==3:
                    print('要添加对象请输入1,退出系统请输入quit:')
                    while True:
                        myinsert=input()
                        if myinsert=='quit':
                            print('查询请输入0,修改请输入1,删除请输入2,添加请输入3,退出系统请输入quit')
                            break
                        print('书名:')
                        name=input()
                        print('书的编号:')
                        bkid=input()
                        print('书的作者:')
                        author=input()
                        insert(name,bkid,author)
                        print('要添加对象请输入1,退出系统请输入quit:')
                else:
                    print('别皮!')
    elif int(l_or_s)==0:
        print ("输入名字:")
        name=input()
        print ("输入密码:")
        password=input()
        signin(name,password)
        print('登录请输入1,退出系统请输入quit')
    elif int(l_or_s)==520:
        poem2= '''欢迎来到隐藏关卡!\n'''
        for char in poem2:
            sleep(0.01)
            sys.stdout.write(char)
        pi()
        print('注册请输入0,登录请输入1,退出系统请输入quit')
    else:
        print('别皮!')
        print('注册请输入0,登录请输入1,退出系统请输入quit')
db.close()
