class SvgExtractorItem:

    def __init__(self, src, width, height, is_visible):
        self._src = src
        self._width = width
        self._height = height
        self._is_visible = is_visible

    def source_url(self):
        return self._src

    def get_visible_height(self):
        return self._height

    def get_visible_width(self):
        return self._width

    def is_visible(self):
        return self._is_visible