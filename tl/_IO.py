import functools
import gzip
from typing import Tuple, Union
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
from importlib import resources

from .. import _data


def _output(
    filename: str = "",
    _format: str = "",
    *,
    od: str = ".",
    prefix: str = "",
    suffix: str = "",
) -> str:
    return f"{od}/{prefix}{filename}{suffix}.{_format}"


def _export(
    filename: str,
    formats: Union[str, Tuple[str, ...]],
    *,
    od: str = ".",
    prefix: str = "",
    suffix: str = "",
    dpi: int = 300,
    figsize=(7, 7),
) -> None:
    if isinstance(formats, str):
        formats = (formats,)

    plt.rcParams["figure.figsize"] = figsize
    for i in formats:
        plt.savefig(
            _output(filename, i, od=od, prefix=prefix, suffix=suffix),
            dpi=dpi,
            bbox_inches="tight",
        )
    plt.close()


def export(
    formats: Union[str, Tuple[str, ...]],
    *,
    od: str = ".",
    prefix: str = "",
    suffix: str = "",
    dpi: int = 300,
    figsize=(7, 7),
):
    return functools.partial(
        _export, formats=formats, od=od, prefix=prefix, suffix=suffix, dpi=dpi
    )


def mkdir(od: str):
    pass


def read_csv_gz(
    data_file_name: str,
    index_col=None,
    usecols=None,
    sep=",",
    *,
    encoding="utf-8",
    **kwargs,
):
    """Loads gzip-compressed with `importlib.resources`.

    1) Open resource file with `importlib.resources.open_binary`
    2) Decompress file obj with `gzip.open`
    3) Load decompressed data with `pd.read_csv`

    Parameters
    ----------
    data_file_name : str
            Name of gzip-compressed csv file  (`'*.csv.gz'`) to be loaded from
            `_data/data_file_name`. For example `'humanGene.csv.gz'`.
    """

    with resources.open_binary(_data, data_file_name) as _:
        _ = gzip.open(_, mode="rt", encoding=encoding)
        _df = pd.read_csv(_, usecols=usecols, index_col=index_col, sep=sep)
    return _df

def gmt_to_dict(pth: str) -> dict:
    """
    Parse a gmt file to a dict.
    """
    from itertools import chain, repeat

    pathways = {}

    with pathlib.Path(pth).open("r") as f:
        for line in f:
            name, _, *genes = line.strip().split("\t")
            pathways[name] = genes
    return pathways