import os
from urllib.parse import urlparse


class PngsProcessor:

    def __init__(self, png_dir):
        self._png_dir = png_dir

    def process(self, converted_item):
        filename = self.get_file_name_from_url(converted_item['source_url'])
        filename = filename.replace('.svg', '.png')

        fstream = open(self._png_dir + '\\' + filename, 'wb')
        fstream.write(converted_item['content'])
        fstream.close()

    def get_file_name_from_url(self, source_url):
        parse = urlparse(source_url)
        return os.path.basename(parse.path)
