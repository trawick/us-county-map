from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from bs4 import BeautifulSoup
from us_county_map import create_svg

here = Path(__file__).parent.resolve()
fixtures = here / 'fixtures'


class Test(TestCase):

    def test(self):
        with TemporaryDirectory() as temp:
            output_svg = Path(temp) / 'wake_is_purple.svg'
            create_svg(
                fixtures / 'test.csv',
                output_svg,
                csv_header_mapping=dict(
                    fill_color='my_fill_color',
                    fips_code='fips',
                    fill_opacity='fill_opacity',
                )
            )
            with open(output_svg, encoding='utf-8') as svg:
                soup = BeautifulSoup(svg, 'html.parser')
                wake = soup.select_one('path#Wake__NC')
                self.assertEqual('fill:purple', wake.attrs['style'])
