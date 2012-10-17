DjangoVerifyCode
=================
在Django中生成验证码
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

依赖
----
+ PIL
+ Django >= 1.3

