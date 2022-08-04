from config import Config
from src.inkscape_svg_to_png_converter import InkscapeSvgToPngConverter
from src.web_content_filter import WebContentFilter
from src.pngs_processor import PngsProcessor


class App:

    def __init__(
        self,
        svg_to_png_converter,
        pngs_processor,
        web_svg_extractor
    ):
        self._svg_to_png_converter = svg_to_png_converter
        self._pngs_processor = pngs_processor
        self._web_svg_extractor = web_svg_extractor

    def run(self, url: str):
        svgs = self._get_web_svg_extractor().get_all_svgs(url)
        for svg in svgs:
            if svg.is_visible:
                converted_item = self._convert_svg_to_png(svg)
                self._process_converted_item(converted_item)

    def _convert_svg_to_png(self, svg):
        source_url = svg.source_url()
        png_width = svg.get_visible_width()
        png_height = svg.get_visible_height()
        converter = self._get_svg_to_png_converter()
        png = converter.convert_from_url(source_url)
        return {
            'source_url': source_url,
            'content': png
        }

    def _get_svg_to_png_converter(self):
        return self._svg_to_png_converter

    def _converted_items_processor(self):
        return self._pngs_processor

    def _get_web_svg_extractor(self):
        return self._web_svg_extractor

    def _process_converted_item(self, item):
        self._converted_items_processor().process(item)


app_config = Config()

web_content_filter = WebContentFilter(app_config)
svg_to_png_converter = InkscapeSvgToPngConverter(app_config.CONVERTER_DEBUG_ENABLED)
pngs_processor = PngsProcessor(app_config.PNG_OUTPUT_DIR)
app = App(
    svg_to_png_converter,
    pngs_processor,
    web_content_filter
)

app.run('https://oborot.ru')
