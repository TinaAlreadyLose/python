# # -*- coding: utf-8 -*-
#
# from django.http import HttpResponse
#
# from Blog.models import Test
#
# # 数据库操作
#
#
# def testdb(request):
#     #insert data (is tables is empty create data type )
#     test1 = Test(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</数据添加成功p>")
#
#     # select data
#     '''
#     response0=""
#     response1=""
#     list=Test.objects.all() #等价于select *from
#     response2=Test.objects.filter(id=1) # 相当于where语句
#     response3=Test.objects.get(id=1) # 获取单个对象
#     Test.objects.order_by('name')[0:2]  #显示返回的数据相当于sql中的OFFSET LIMIT
#     Test.objects.order_by("id")
#     Test.objects.filter(name="runoob").order_by('id') #数据排序
#     #输出所有数据
#     for i in list:
#         response1+=i.name+" "
#     response0=response1
#     return HttpResponse("<p>"+response0+"</p>")
#     '''
#     # update data
#     '''
#     #method1
#     test=Test.objects.get(id=1)
#     test.name='Google'
#     test.save()
#     #method2
#     Test.objects.filter(id=2).update(name='baidu')
#     #Test.objects.all().update(name="twitter")
#
#     return HttpResponse("<p>数据修改成功</p>")
#     '''
#     # delete data
#     '''
#     #method1
#     test=Test.objects.get(id=2)
#     test.delete()
#     #method2
#     Test.objects.filter(id=2).delete()
#     #delete all
#     Test.objects.all().delete()
#     return HttpResponse("<p> sccuess delete</p>")
#     '''
