import os

from src.inkscape_svg_to_png_converter import InkscapeSvgToPngConverter


def main():
    svg_to_png_converter = InkscapeSvgToPngConverter()
    tempdir = os.getcwd() + os.path.sep + 'tmp\\'
    files = os.listdir(tempdir)

    for file in files:
        file_path = tempdir + file
        result = svg_to_png_converter.convert_from_path(file_path)
        print(result)


if __name__ == '__main__':
    main()