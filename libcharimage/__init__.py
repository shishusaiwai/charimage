from encoder import encode_charimage, decode_charimage


def is_single_band(img):
    first_pixel = img.getpixel((0, 0))
    return isinstance(first_pixel, int)


def compute_thredhold(img):
    thredhold = 350
    if is_single_band(img):
        thredhold = 120
        max_color = 0
        for w in range(0, img.size[0]):
            for h in range(0, img.size[1]):
                color = img.getpixel((w, h))
                if color > max_color:
                    max_color = color
        if max_color <= 127:
            thredhold = 50
    return thredhold


def make_imagestring(img, row_width=80):
    char_img = ""
    width = img.size[0]
    step = width / row_width
    if step <= 1:
        step = 1
    thredhold = compute_thredhold(img)

    for h in range(0, img.size[1], step):
        for w in range(0, img.size[0], step):
            color = img.getpixel((w, h))
            if isinstance(color, int):
                value = color
            else:
                value = sum(color)
            if value < thredhold:
                char_img += "*"
            else:
                char_img += " "
        char_img += "\n"
    return char_img


logo = " 28*1 51n 14*2 1*1 9*2 8*6 37n 14*2 2*1 8*1 1*1 7*1 4*1 37n 14*1 3*1 7*2 1*2 6*6 37n 13*2 4*1 4*3 4*2 47n 12*2 2*1 3*2 1*4 2*1 2*2 1*11 34n 11*2 2*2 4*1 4*1 2*1 8*1 41n 15*1 2*1 6*3 1*2 6*7 36n 14*1 3*1 6*6 12*1 36n 13*2 1*4 4*2 2*2 1*1 10*2 36n 13*4 2*2 2*2 1*3 3*2 7*3 36n 80n 62*2 8*7 1n 2*4 17*2 21*10 3*10 3*1 4*1 2n 2*6 10*2 3*2 23*1 2*2 2*1 3*1 1*6 5*1 4*1 2n 2*2 2*2 1*2 3*2 1*5 1*2 1*2 4*3 4*2 1*2 2*10 3*1 5*2 5*7 1n 2*2 2*2 2*2 2*2 1*5 1*6 2*5 3*5 4*2 1*2 2*1 3*1 2*3 6*8 1n 2*6 2*2 2*1 3*2 3*2 2*2 1*2 3*2 2*2 2*2 2*3 1*5 3*9 3*2 2*1 2*1 1n 2*5 4*1 1*2 3*2 3*2 2*2 1*2 3*2 2*2 2*2 2*4 2*1 5*1 4*1 1*2 3*2 2*1 2*1 1n 2*2 7*4 3*2 3*2 2*2 1*2 3*2 2*2 2*2 1*3 2*5 3*1 4*1 1*1 4*2 2*1 2*1 1n 2*2 7*3 4*3 2*2 2*2 2*5 3*2 2*4 1*1 4*1 5*1 4*1 6*2 1*1 1*3 1n 2*2 8*2 5*2 2*2 2*2 3*3 4*2 2*2 3*1 4*1 4*2 4*1 7*2 3*3n 12*1 35*1 1*7 1*1 4*2 5*3 6*1n 10*3 67n 80"
print decode_charimage(logo)

__all__ = [make_imagestring, encode_charimage, decode_charimage]
