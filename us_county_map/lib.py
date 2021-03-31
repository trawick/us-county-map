from collections import namedtuple
import csv
import logging
from pathlib import Path

from bs4 import BeautifulSoup

CountyStyle = namedtuple('CountyStyle', 'fill_color,fill_opacity')
here = Path(__file__).parent.resolve()
images = here / 'images'
logger = logging.getLogger(__name__)


DEFAULT_CSV_HEADER_MAPPING = dict(
    fill_color='fill_color',
    fips_code='fips_code',
    fill_opacity='fill_opacity',
)


def csv_to_dict(county_data, csv_header_mapping):
    fill_color_col = csv_header_mapping['fill_color']
    fill_opacity_col = csv_header_mapping['fill_opacity']
    fips_code_col = csv_header_mapping['fips_code']

    reader = csv.DictReader(county_data)

    by_fips_code = {}
    for row in reader:
        style = CountyStyle(
            fill_color=row.get(fill_color_col),
            fill_opacity=row.get(fill_opacity_col),
        )
        fips_code = row[fips_code_col]
        by_fips_code[fips_code] = style
    return by_fips_code


def create_svg(county_data_path, output_svg_path, csv_header_mapping=None):
    csv_header_mapping = csv_header_mapping or {}
    csv_header_mapping = {**DEFAULT_CSV_HEADER_MAPPING, **csv_header_mapping}

    with open(county_data_path, 'r', encoding='utf-8') as county_data:
        by_fips_code = csv_to_dict(county_data, csv_header_mapping)

    with open(images / 'USA_Counties.svg', encoding='utf-8') as svg:
        soup = BeautifulSoup(svg, 'html.parser')

    for path in soup.select("g#county-group path"):
        # expecting class="cNNNNN" on our known input; grab the numeric portion
        fips_code = path.attrs["class"][0][1:]
        county_name = path.attrs["id"]
        data = by_fips_code.get(fips_code)
        if data is None:
            logger.debug('No style data for fips code %s (%s)', fips_code, county_name)
            continue
        if data.fill_color is not None:
            path['style'] = f'fill:{data.fill_color}'
        if data.fill_opacity is not None:
            path['fill-opacity'] = f"{data.fill_opacity}%"

    with open(output_svg_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
