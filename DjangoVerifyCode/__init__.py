#encoding:utf-8
from django.http import HttpResponse
import Image,ImageDraw,ImageFont,random,StringIO
import os

##########################
# author:tianyu0915
# site:pythoner.net
# date:2011-7-10
##########################
__version__ = '0.1'
__author__  = 'TY'

class Code(object):

    def __init__(self,request):
        self.django_request = request
        self.session_key = 'django-verify-code'
        self.worlds = [
            'about',
            'bronze',
            'blouse',
            'china',
            'complex',
            'document',
            'django',
            'facebook',
            'finally',
            'freezer',
            'github',
            'google',
            'instance',
            'linux',
            'lambda',
            'mysql',
            'object',
            'python',
            'syntax',
            'twitter',
        ]
        # 验证码图片尺寸
        self.img_width = 150
        self.img_height = 30
        # 验证码字体颜色
        self.font_color = ['black','darkblue','darkred']
        # 随即背景颜色
        self.background = (random.randrange(230,255),random.randrange(230,255),random.randrange(230,255))
        # 字体大小 
        font_size = 24
        current_path = os.path.normpath(os.path.dirname(__file__))
        # 字体
        self.font = ImageFont.truetype(os.path.join(current_path,'timesbi.ttf').replace('\\','/'),font_size)

    def display(self):
        """ django 单词验证码生成 """

        # the worlds list maxlength = 8
        self.django_request.session[self.session_key] = '' 
        # creat a image
        im = Image.new('RGB',(self.img_width,self.img_height),self.background)
        #code = random.sample(string['litter'],4)
        code = self.worlds[random.randrange(0,len(self.worlds))]
        # creat a pen
        draw = ImageDraw.Draw(im)

        # 画随机干扰线
        for i in range(random.randrange(3,5)):
            line_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            xy = (random.randrange(0,self.img_width/4),random.randrange(0,self.img_height),
                  random.randrange(3*self.img_width/4,self.img_width),random.randrange(0,self.img_height))
            draw.line(xy,fill=line_color,width=1)

        # 写验证码
        x = random.randrange(10,20)
        for i in code:
            y = random.randrange(0,5)
            draw.text((x,y), i, font=self.font, fill=random.choice(self.font_color))
            x += 16
            self.django_request.session[self.session_key] += i
        del x
        del draw
        buf = StringIO.StringIO()
        im.save(buf,'gif')
        buf.closed
        return HttpResponse(buf.getvalue(),'image/gif')

    def check(self,code):
        """ 检查用户输入的验证码是否正确 """
        _code = self.django_request.session.get(self.session_key) or ''
        code = str(code).lower()
        return _code.lower() == code


