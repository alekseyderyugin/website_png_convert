import subprocess
from tempfile import NamedTemporaryFile
import requests
import os


class InkscapeSvgToPngConverter:

    def __init__(self, is_debug: bool = False):
        self._is_debug = is_debug

    def convert_from_url(self, svg_url, width=False, height=False):
        """
        Конвертировать, используя url до svg
        @param svg_url:
        @param width:
        @param height:
        @return:
        """
        response = requests.get(svg_url)
        temp = NamedTemporaryFile('wb', suffix='.svg', delete=False)
        temp.write(response.content)
        temp.close()

        png_temp_filename = temp.name.replace('.svg', '.png')

        args = ['inkscape', '-f', temp.name, '-e', png_temp_filename, '-d', '96']

        self._run_subprocess(args)

        png_temp_file = open(png_temp_filename, 'rb')
        content = png_temp_file.read()
        png_temp_file.close()

        os.remove(temp.name)
        os.remove(png_temp_filename)
        return content

    def convert_from_path(self, svg_file_path: str) -> str:
        """
        Конвертировать, используя путь до svg
        @param svg_file_path:
        @return:
        """
        png_path = svg_file_path.replace('.svg', '.png')
        cmd_args = ['inkscape', '-f', svg_file_path, '-e', png_path]
        self._run_subprocess(cmd_args)

        return png_path

    def _run_subprocess(self, cmd_args: list):
        if self._is_debug:
            subprocess.run(cmd_args, shell=True)
        else:
            subprocess.run(cmd_args, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True)