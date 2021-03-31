import logging

import click

from us_county_map import create_svg

logger = logging.getLogger(__name__)


@click.command()
@click.argument('county_data', type=click.Path(exists=True))
@click.argument('output_svg', type=click.Path(exists=False))
@click.option('--level', type=click.Choice(['DEBUG', 'INFO']), default='INFO')
@click.option('--map', '-m', 'mappings', type=str, multiple=True)
def cli(county_data, output_svg, level, mappings):
    logging.basicConfig(level=logging.getLevelName(level))
    csv_header_mapping = {}
    for mapping in mappings:
        canonical, in_csv = mapping.split('=')
        csv_header_mapping[canonical] = in_csv
    create_svg(county_data, output_svg, csv_header_mapping=csv_header_mapping)
