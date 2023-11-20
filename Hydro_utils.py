'''
Provides utility functions for the hydrological machine learning study on
soil moisture proxies.

Utility functions include normalisation, feature detection, and standard
plotting functions for visualisation of the results as per the publication.

'''

import numpy as np
import datetime as dt
import matplotlib.dates as mdt
import matplotlib.ticker as mtk
import matplotlib.pyplot as plt


def featurelocator(df, features):
    '''
    Function to return the column numbers for features from a dataframe
    for use with indexing the array form of that dataframe

    Parameters
    ----------
    df : Pandas dataframe
        Pandas dataframe of all input and output information
    features : List
        List of target variables or features.

    Returns
    -------
    List of indices for slicing the converted array.

    '''
    array_indices = [df.columns.get_loc(f) for f in features]
    return array_indices


def normalise(df, feature, norm_dict={}, write_cache=True):
    '''
    Function to normalise the feature columns of a dataframe, with the option
    to retain a cache of the normalisation parameters for use on additional
    datasets.    
    
    Parameters
    ----------
    df : Pandas dataframe
        Dataframe containing columns of variables to be normalised
    feature : String
        Name of feature column to be normalised
    norm_dict : Dictionary
        Dictionary in which normalisation cache parameters are stored
    write_cache : Boolean
        Determines whether or not the cache key values will be overwritten

    Returns
    -------
    The input feature column normalised with a dictionary key value entry made
    containing all normalisation parameters.
    '''
    if write_cache == True:
        favg = np.mean(df[feature])
        fmax = np.max(df[feature])
        fmin = np.min(df[feature])
        cachelist = [favg, fmax, fmin]
        norm_dict[feature] = cachelist
        return(df[feature] - favg)/(fmax-fmin)
    elif write_cache == False:
        cache = norm_dict[feature]
        return(df[feature] - cache[0])/(cache[1]-cache[2])


def year_plot(maxflow, df, y_pred, y_obsv, year, colour1='cadetblue',
              colour2='darkseagreen'):
    '''
    Generates a scatter plot of observations against predictions with an
    indicator line of perfect fit.    

    Parameters
    ----------
    maxflow : Float
        Maximum flow for scaling the y axis
    df : Pandas dataframe
        Pandas dataframe with observations, predictions, and date columns
    y_pred : String
        Name of the predicted flow column
    y_obsv : String
        Name of the observed flow column
    year : Integer
        Target year to be plotted as a time series
    colour1 : String, optional
        Predicted time series colour. The default is 'cadetblue'.
    colour2 : String, optional
        Observed time series colour. The default is 'darkseagreen'.

    Returns
    -------
    Displays the time series plot.

    '''
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(df['Date'], df[y_pred], colour1, lw=3.2)
    ax.plot(df['Date'], df[y_obsv], colour2, lw=3.2, ls='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Flow (m'+r'$^3$'+'s'+r'$^{-1}$'+')')
    ax.set_xlim([dt.date(year, 1, 1), dt.date(year, 12, 31)])
    ax.set_ylim(0,maxflow)
    ax.xaxis.set_major_locator(mdt.MonthLocator())
    ax.xaxis.set_major_formatter(mdt.DateFormatter('%b'))
    ax.yaxis.set_major_locator(mtk.MaxNLocator(5))
    ax.legend(['Prediction', 'Actual'], loc='upper left')
    ax.grid(c='black', ls='dotted', lw=0.5)
    plt.show()


def scatter_plot(maxflow, df, pred, obsv, colour='steelblue', marker='*'):
    '''
    Generates a scatter plot of observations against predictions with an
    indicator line of perfect fit.
    
    Parameters
    ----------
    maxflow : Float
        Maximum flow for scaling the y axis
    df : Pandas dataframe
        Pandas dataframe with observations, predictions, and date columns
    pred : String
        Name of the predicted flow column
    obsv : String
        Name of the observed flow column
    colour : String, optional
        Scatter point colours. The default is 'steelblue'.
    marker : String, optional
            Scatter point colours. The default is 'steelblue'.

    Returns
    -------
    Displays the scatter plot.

    '''
    xyline = np.linspace(0, maxflow, maxflow)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(df[pred], df[obsv], marker=marker, s=4, c=colour)
    ax.plot(xyline, xyline, c='black', lw=1)
    ax.set_xlabel('Predicted Flow (m'+r'$^3$'+'s'+r'$^{-1}$'+')')
    ax.set_ylabel('Observed Flow (m'+r'$^3$'+'s'+r'$^{-1}$'+')')
    ax.set_xlim([0, maxflow])
    ax.set_ylim([0, maxflow])
    ax.xaxis.set_major_locator(mtk.MaxNLocator(5))
    ax.yaxis.set_major_locator(mtk.MaxNLocator(5))
    plt.show()
