import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde
from sklearn.metrics import r2_score
from scipy.stats import pearsonr, spearmanr


def scatter(
    x,
    y,
    ax=None,
    density=False,
    c="b",
    alpha=1,
    s=10,
    xlabel="Observed",
    ylabel="Predicted",
    figsize=(4, 4),
    save=None,
    add_reference_line=True,
    rasterized=False,
):
    # Set up the axes
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    # Drop NA values if any
    x_nas = np.isnan(x)
    y_nas = np.isnan(y)
    x = x[~x_nas & ~y_nas]
    y = y[~x_nas & ~y_nas]

    if density:
        # Get point densities
        xy = np.vstack([x,y])
        z = gaussian_kde(xy)(xy)

        # Sort the points by density, so that the densest points are plotted last
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]
        c=z

    # Plot the points
    ax.scatter(x, y, c=c, s=s, rasterized=rasterized, alpha=alpha)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Add scores
    r2 = r2_score(x, y)
    pearson_r = pearsonr(x, y)
    spearman_r = spearmanr(x, y)
    ax.annotate(f"R2: {r2:.3f}", (0.05, 0.95), xycoords="axes fraction")
    ax.annotate(f"Pearson: {pearson_r[0]:.3f}", (0.05, 0.90), xycoords="axes fraction")
    ax.annotate(f"Spearman: {spearman_r[0]:.3f}", (0.05, 0.85), xycoords="axes fraction")
    
    # Add y=x line for reference but make the mins and maxes extend past the data
    if add_reference_line:
        min_val = min(min(x), min(y))
        max_val = max(max(x), max(y))
        ax.plot([min_val, max_val], [min_val, max_val], c="k", ls="--", lw=1)
    
    # Plt
    plt.tight_layout()

    # Save
    if save:
        plt.savefig(save, dpi=300)
        plt.close()
    else:
        plt.show()
