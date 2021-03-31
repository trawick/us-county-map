# us-county-map

Python package to create a US county map SVG with fill colors applied, from CSV input

## Todos

* Finish documentation in README
* `Makefile` for dev activities
* research how opacity can be provided for SVG paths; should header have `pct` in the name?
* tox/TravisCI

## Dependencies

* Python 3.6 or higher
* BeautifulSoup
* Click

## How to use

### Installation

```shell
$ pip install git+git://github.com/trawick/us-county-map
```

(no tags/releases of interest yet)

### Using the CLI

```shell
$ us_county_map [-m <MAPPING>]... <INPUT-CSV> <OUTPUT-SVG>
```

A mapping takes the form `<CANONICAL-CSV-COLUMN-NAME>=<YOUR-CSV-COLUMN-NAME>`.

The canonical column names are

* `fips_code`: FIPS code of county or county equivalent
* `fill_color`: valid HTML/CSS color name, RGB, or other form
* `fill_opacity`: percent opacity for the fill color (CSS `fill-opacity`)

If for example the column with the FIPS code is named `Fips`, add the option `-m fips_code=Fips`.

### Using the API from Python

## External resources included

### USA_Counties.svg

Attribution: U.S. Census Bureau, Public domain, via Wikimedia Commons and https://github.com/trawick/USA_Counties

## Support

Please open Github issues for suggestions or suspected problems.  Even if I am
unable to respond in a timely basis, the information may quickly become valuable
to others, and I will eventually find time to respond to the issue.

## LICENSE

The included file `USA_Counties.svg` is public domain.  (See attribution above.)

All other components of this project are covered by the Apache License version 2.0 (ASL2).
See included LICENSE file for more information.
