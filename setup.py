#encoding:utf-8
from distutils.core import setup  
setup(name='DjangoVerifyCode',  
      author='TY(pythoner.net)',  
      author_email='tianyu0915@gmail.com',  
      version='0.2.2',  
      description='在django中生成英文/数字公式验证码',  
      keywords ='django verify code 验证码',
      url='http://github.com/tianyu0915/DjangoVerifyCode',  
      packages=['DjangoVerifyCode'],  
      package_data={'DjangoVerifyCode':['*.*','DjangoVerifyCode/*.*']},

)  
