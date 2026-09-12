import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def make_correlation_heatmap(correlation_matrix: pd.DataFrame) -> object:
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(10, 8))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

    sns.heatmap(
        correlation_matrix,
        mask=mask,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        ax=ax,
    )

    return fig
