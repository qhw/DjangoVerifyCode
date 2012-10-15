#encoding:utf-8
from django.http import HttpResponse
import Image,ImageDraw,ImageFont,random,StringIO
import os

##########################
# author:tianyu0915
# site:pythoner.net
# date:2011-7-10
##########################

def display(request):
    """ django 单词验证码生成 """

    # the worlds list maxlength = 8
    worlds = [
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
    # 随即背景颜色
    background = (random.randrange(230,255),random.randrange(230,255),random.randrange(230,255))
    # 验证码图片尺寸
    img_width = 150
    img_height = 30
    # 验证码字体颜色
    font_color = ['black','darkblue','darkred']
    # 字体大小 
    font_size = 24
    current_path = os.path.normpath(os.path.dirname(__file__))
    # 字体
    font = ImageFont.truetype(os.path.join(current_path,'timesbi.ttf').replace('\\','/'),font_size)
    request.session['verify'] = ''

    # creat a image
    im = Image.new('RGB',(img_width,img_height),background)
    #code = random.sample(string['litter'],4)
    code = worlds[random.randrange(0,len(worlds))]
    # creat a pen
    draw = ImageDraw.Draw(im)

    # draw lines
    # 画随机干扰线
    for i in range(random.randrange(3,5)):
        line_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        xy = (random.randrange(0,img_width/4),random.randrange(0,img_height),
              random.randrange(3*img_width/4,img_width),random.randrange(0,img_height))
        draw.line(xy,fill=line_color,width=1)

    # draw the litter
    # 写验证码
    x = random.randrange(10,20)
    for i in code:
        y = random.randrange(0,5)
        draw.text((x,y), i, font=font, fill=random.choice(font_color))
        x += 16
        request.session['verify'] += i
    del x

    del draw
    buf = StringIO.StringIO()
    im.save(buf,'gif')
    buf.closed
    return HttpResponse(buf.getvalue(),'image/gif')

