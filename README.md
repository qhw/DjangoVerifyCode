DjangoVerifyCode
=================
在Django中生成英文单词验证码,原用于[pythoner.net](http://pythoner.net)的验证码,现整理出来打包发布到pypi.
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
    code = Code(request)
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
##### 输出图片的宽度 #####
`code.img_width` = 150
##### 输出图片的高度 #####
`code.img_height` = 30
##### 验证码字体颜色 #####
`code.font_color` = ['black','darkblue','darkred']
##### 字体大小 #####
`font_size` = 24

依赖
----
+ PIL

More
----
+ demo <http://dvf.pythoner.net>
+ <http://pythoner.net>
+ <http://pypi.python.org/pypi/DjangoVerifyCode>

