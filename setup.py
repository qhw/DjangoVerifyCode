#encoding:utf-8
from distutils.core import setup  
setup(name='DjangoVerifyCode',  
      author='TY',  
      author_email='tianyu0915@gmail.com',  
      version='0.1.1',  
      description='django验证码',  
      keywords ='django verify code 验证码',
      #install_requires=["Django>=1.0","PIL>=1.1"],
      url='http://github.com/tianyu0915',  
      packages=['DjangoVerifyCode'],  
      package_data={'DjangoVerifyCode':['*.*','DjangoVerifyCode/*.*']},
)  
