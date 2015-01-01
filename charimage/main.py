#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from converter import make_imagestring
from encoder import encode_charimage, decode_charimage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', dest='row_width', help="result row width", type=int, default=80)
    parser.add_argument('-e', dest='encode', help="encode the result", action='store_true')
    parser.add_argument('-d', dest='decode', help="decode the encoded_string", action='store_true')
    parser.add_argument('-v', dest='verbose', help="verbose output", action='store_true')
    parser.add_argument('image', default="", nargs="?", help="<image_path/encoded_string>")
    args = parser.parse_args()

    if args.decode:
        encoded_image = raw_input("encodedm image:")
        print decode_charimage(encoded_image, args.verbose)
    else:
        from PIL import Image
        i = Image.open(args.image)
        char_img = make_imagestring(i, args.row_width)
        if args.encode:
            print encode_charimage(char_img)
        else:
            print char_img


if __name__ == '__main__':
    main()
