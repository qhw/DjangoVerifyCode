DjangoVerifyCode v0.2.0
=======================
介绍
----
在django中生成英文单词验证码,提供验证码图片生成,检查验证码等功能
原用于[pythoner.net](http://pythoner.net)的验证码,现整理出来打包发布到pypi.

#### 新特性
+ 新增数字验证码模式
+ 字体尺寸根据图片长宽自适应


使用
---
####安装####
```
pip install DjangoVerifyCode
or
easy_install DjangoVerifyCode
```
####显示验证码(views.py)####
```
from DjangoVerifyCode import Code
def code(request):
    code =  Code(request)
    code.worlds = ['hello','world','helloworld']
    #code.type = 'world'
    code.type = 'number'
    return code.display()
```

####检查用户输入的验证码是否正确(views.py)####
```
from DjangoVerifyCode import Code
def index(request):
    _code = request.GET.get('code') or ''
    if not _code:
        return render('index.html',locals())

    code = Code(request)
    if code.check(_code):
        return HttpResponse('验证成功')
    else:
        return HttpResponse('验证失败')
```

自定义
-----
用户可根据自己的需要对DjangoVerifyCode.Code对象的属性进行设置
##### 输出图片的宽度 
`code.img_width` = 150
##### 输出图片的高度 
`code.img_height` = 30
##### 设置验证码类型('number'/'world')
`code.type = 'number'`

依赖
----
+ PIL

More
----
+ demo <http://dvf.pythoner.net>
+ <http://pythoner.net>
+ <http://pypi.python.org/pypi/DjangoVerifyCode>

