from os.path import abspath, dirname, join
from matplotlib import style
from matplotlib.axes import Axes

from typing import List

style.use(join(dirname(abspath(__file__)), "markplotlib.mplstyle"))

__all__ = ["ylabel_top", "restore_spines"]


def ylabel_top(ax: Axes, label: str) -> None:
    """Adds a y axis label to the top of the axis, instead of the side

    :param ax: the Axes object to label
    :param label: text for the label

    :returns: the ``Text`` object returned by ``ax.set_ylabel``"""

    ax.set_ylabel(label, ha="right", va="bottom", rotation=0)
    ax.yaxis.set_label_coords(-0.01, 1.02)
    return None


def restore_spines(ax: Axes, spines: List[str] = ["left", "top"]) -> None:
    for spine in spines:
        ax.spines[spine].set_visible(True)
    return None
