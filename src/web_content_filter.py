from src.web_svg_extractor import WebSvgExtractor
from src.web_svg_extractor import SvgExtractorItem

class WebContentFilter:

    def __init__(self, config):
        self._extractor = WebSvgExtractor(config.CHROME_DRIVER_PATH)

    def get_all_svgs(self, url: str):
        """

        Returns
        -------
        list[SvgExtractorItem]
        """
        return self._extractor.extract(url)
