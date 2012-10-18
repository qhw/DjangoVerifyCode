#encoding:utf-8
from distutils.core import setup  
import DjangoVerifyCode as dvc
setup(name='DjangoVerifyCode',  
      author='TY(pythoner.net)',  
      author_email='tianyu0915@gmail.com',  
      version='0.1.4',  
      description='django验证码',  
      keywords ='django verify code 验证码',
      url='http://github.com/tianyu0915/DjangoVerifyCode',  
      packages=['DjangoVerifyCode'],  
      package_data={'DjangoVerifyCode':['*.*','DjangoVerifyCode/*.*']},

)  
