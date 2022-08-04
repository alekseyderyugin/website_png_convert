from src.web_svg_extractor import WebSvgExtractor
from config import Config

extractor = WebSvgExtractor(Config.CHROME_DRIVER_PATH)

svgs = extractor.extract('https://oborot.ru')