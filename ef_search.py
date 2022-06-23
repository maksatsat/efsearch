import numpy as np

def search(times, period_min, period_max, nbins=20, nperiods=1000):
    """
    Epoch folding

    Calculate chi2 statistics for time-event data

    Args:
        times (array): time-event data (photon arrival times).
        period_min (float): starting period for search.
        period_max (float): ending period for search.

    Returns:
        array: array of calculated chi2 statistics

    """
    periods = np.linspace(period_min, period_max, nperiods)
    stats = np.zeros(nperiods)
    for i, period in enumerate(periods):
        folded = np.histogram(times%period/period, bins=nbins, range=(0,1))[0]
        expected = len(times)/nbins
        chi2 = np.sum((folded-expected)**2/expected**2)
        stats[i] = chi2
    return periods, stats


def periodic_generator(num):
    counts = np.random.poisson(100, size=len(times))
