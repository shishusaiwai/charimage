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


def compute_value(pixels):
    sample_color = pixels[0]
    if isinstance(sample_color, int):
        value = sum(pixels) / len(pixels)
    else:
        value = sum([sum(p) for p in pixels]) / len(pixels)
    return value


def make_imagestring(img, row_width=80):
    char_img = ""
    width = img.size[0]
    step = width / row_width
    if step <= 1:
        step = 1
    thredhold = compute_thredhold(img)

    for h in range(0, img.size[1], step):
        for w in range(0, img.size[0], step):
            pixels = [img.getpixel((w_index, h)) for w_index in range(w, w + step) if w_index < img.size[0]]
            value = compute_value(pixels)
            if value < thredhold:
                char_img += "*"
            else:
                char_img += " "
        char_img += "\n"
    return char_img
