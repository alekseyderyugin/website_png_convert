from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from src.Item.svg_extractor_item import SvgExtractorItem


class WebSvgExtractor:

    def __init__(self, chrome_driver_path):
        self._browser = Chrome(chrome_driver_path)

    def extract(self, url) -> List[SvgExtractorItem]:
        """

        @param url: str
        @return: list[SvgExtractorItem]
        """
        browser = self._get_browser
        browser.get(url)

        imgs = self._extract_html_imgs()

        return imgs

    def _extract_html_imgs(self):
        browser = self._get_browser
        imgs = browser.find_elements_by_tag_name('img')

        result = []
        for img in imgs:
            src = img.get_attribute('src')

            if '.svg' not in src:
                continue

            matches = [x for x in result if x.source_url() == src]
            if matches:
                continue

            result.append(self._get_new_svg_extractor_item(img))

        return result

    def extract_css_imgs(self):
        browser = self._get_browser


    @property
    def _get_browser(self):
        return self._browser

    def _get_new_svg_extractor_item(self, img: WebElement) -> SvgExtractorItem:
        is_visible = img.value_of_css_property('visibility') == 'visible' and img.value_of_css_property(
            'display') is not 'none'
        visible_width = img.get_attribute('clientWidth')
        visible_height = img.get_attribute('clientHeight')
        item = SvgExtractorItem(
            img.get_attribute('src'),
            visible_width,
            visible_height,
            is_visible
        )

        return item
