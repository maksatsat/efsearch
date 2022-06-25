import numpy as np
from stingray import Lightcurve
from stingray.events import EventList
import matplotlib.pyplot as plt

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

def _sinusoid(times, frequency, baseline, amplitude, phase):
        return baseline + amplitude * np.sin(2 * np.pi * (frequency * times + phase))

def periodic_generator(period=50, obs_length = 1000, mean_countrate = 1, pulsed_fraction = 1.0, ):
    """
    Periodic events generator

    Generates poisson sin-like data

    Args:
        period (float): period of the signal.
        obs_length (float): duration of observation.
        mean_countrate (float): average counts per sec.
        pulsed_fraction (float): from 0 to 1 - sin pulse fraction

    Returns:
        array: generated periodic arrival times

    """
    bin_time = 0.01
    obs_length = 200
    t = np.arange(0, obs_length+bin_time, bin_time)

    # The continuous light curve
    counts = _sinusoid(t, 1 / period, mean_countrate,
                    0.5 * mean_countrate * pulsed_fraction, 0) * bin_time


    lc = Lightcurve(t, counts, gti=[[-bin_time / 2, obs_length + bin_time / 2]],
                    dt=bin_time)
    
    events = EventList()
    events.simulate_times(lc)    
    return events.time




