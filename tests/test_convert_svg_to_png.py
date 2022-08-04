from src.inkscape_svg_to_png_converter import InkscapeSvgToPngConverter

converter = InkscapeSvgToPngConverter()

output_file = 'D:/tmp/python/oborot_png_convert/test/logo.png'
svg_url = 'https://oborot.ru/wp-content/themes/oborot_theme-child/img/logo.svg'

image_content = converter.convert_from_url(svg_url, width=800, height=800)

fstream = open(output_file, 'wb')
fstream.write(image_content)
fstream.close()
