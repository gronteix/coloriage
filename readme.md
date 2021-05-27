# Introducing coloriage

Coloriage is a quick tool to manually select regions from graphs. The tool is based on the Bokeh interractive plotting tool.

## Installation

Download the package and then from the package location run `pip install .` in the command prompt.

## Workflow

The package is composed of one unique function `make_interactive_plot`, it takes as an entry a networkX graph object G that **at least** has `x`, `y` and `label` as attributes. The two former need to be integers or floats.

From a Jupyter notebook then call:

```
from coloriage import coloriage

coloriage.make_interactive_plot(G)

```