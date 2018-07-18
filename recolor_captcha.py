from collections import Counter
from PIL import Image, ImageDraw


def recolor_captcha(filename):

    image = Image.open(filename)
    obj = image.load()
    draw = ImageDraw.Draw(image)

    width = image.size[0] #ширина изображения
    height = image.size[1] #высота изображения

    color = [] #массив цветов
    #заполняем пустой массив цветами каждого пикселя на изображении
    for x in range(width):
        for y in range(height):
            color.append(image.getpixel((x,y)))
    #сортируем по количеству пикселей одного цвета
    all_color_on_img = Counter(color)

    background_color = all_color_on_img.most_common()[0][0] #задний фон
    r_bc,g_bc,b_bc = background_color[0], background_color[1], background_color[2] #раскладываем на RGB
    S_bc = r_bc + g_bc + b_bc

    color_flag = None #флаг для обозначающий светлый/темный цвет
    color_coeff = None #коэффициент разброса цветов
    if S_bc >= 382: #светлый цвет
        color_coeff = -300
        color_flag = True
    else: #темный цвет
        color_coeff = 300
        color_flag = False

    text_color = None #цвет текста
    for i in all_color_on_img.most_common():
        r,g,b = i[0][0], i[0][1], i[0][2]
        S = r + g + b
        if (color_flag):
            if S <= S_bc + color_coeff and text_color == None:
                text_color = i[0]
        else:
            if S >= S_bc + color_coeff and text_color == None:
                text_color = i[0]

    r_tc, g_tc, b_tc = text_color[0], text_color[1], text_color[2]
    S_tc = r_tc + g_tc + b_tc

    for x in range(width):
        for y in range(height):
            r = image.getpixel((x,y))[0]
            g = image.getpixel((x,y))[1]
            b = image.getpixel((x,y))[2]
            S = r + g + b
            if (color_flag):
                if S <= S_tc+40:
                    image.putpixel((x,y), text_color)
                else:
                    image.putpixel((x,y), background_color)
            else:
                if S >= S_tc-120:
                    image.putpixel((x,y), text_color)
                else:
                    image.putpixel((x,y), background_color)

    # point_start = None
    # point_end = None
    #
    # for y in range(height):
    #     for x in range(width):
    #         r = image.getpixel((x,y))[0]
    #         g = image.getpixel((x,y))[1]
    #         b = image.getpixel((x,y))[2]
    #         S = r + g + b
    #
    #         if S == S_tc and point_start is None:
    #             point_start = (x,y)
    #
    # for x in range(width-1, 0, -1):
    #     for y in range(height-1, 0, -1):
    #         r = image.getpixel((x,y))[0]
    #         g = image.getpixel((x,y))[1]
    #         b = image.getpixel((x,y))[2]
    #         S = r + g + b
    #
    #         if S == S_tc and point_end is None:
    #             point_end = (x,y)
    #
    # draw.line((point_start, point_end), fill=background_color, width=5)

    image.save('done/recolor_%s' %(filename))


if __name__ == '__main__':
    for i in range(1,11):
        name = str(i) + '.png'
        recolor_captcha(name)
