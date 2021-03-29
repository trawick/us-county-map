import logging

import click

from us_county_map import create_svg

logger = logging.getLogger(__name__)


@click.command()
@click.argument('county_data', type=click.Path(exists=True))
@click.argument('output_svg', type=click.Path(exists=False))
@click.option('--level', type=click.Choice(['DEBUG', 'INFO']), default='INFO')
def cli(county_data, output_svg, level):
    logging.basicConfig(level=logging.getLevelName(level))
    create_svg(county_data, output_svg)
