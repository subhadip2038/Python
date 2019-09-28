
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[19]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# Load Data

# In[20]:

clstMetaCol=['ID', 'NAME']

work_hash= 'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89'
cstr_MetaFileName='data/C2A2_data/BinSize_d{}.csv'.format(400)
cstrWorkFile='data/C2A2_data/BinnedCsvs_d{}/{}.csv'.format(400, work_hash)    
dfMeta=make_dfMeta(work_hash)
dfData = pd.read_csv(cstrWorkFile, parse_dates=[0])
    
dfRet=pd.merge(dfMeta[clstMetaCol], dfData, how='left', on='ID', sort=False)
dfRet['Data_Value']=dfRet['Data_Value'].apply(lambda x: x/10)
dfRet.head()


# Data for plotting

# In[26]:

def make_plotting():
    
    def group_stations(df_Work, strFuncName):
        df=df_Work.groupby(['Date'], as_index=False).agg({'Data_Value':strFuncName})
        temp = pd.DatetimeIndex(df['Date'])
        df['Year'], df['Month'], df['Day']=temp.year, temp.month, temp.day
        tmp=df[(df['Month']==2) & (df['Day']==29)] 
        return df.drop(tmp.index).drop('Date', axis=1)

    def group_years_months(df_Work, strFunc):
        return df_Work.groupby(['Month', 'Day'], as_index=False).agg({'Data_Value':strFunc})

    def make_ret_df(dfLeft, dfRight, strLabelMax, strLabelMin):
        dfRet=pd.merge(dfLeft, dfRight, how='inner', on=['Month', 'Day'])
        dfRet.rename(index=str, columns={'Data_Value_x':strLabelMax, 'Data_Value_y':strLabelMin}, inplace=True)
        dfRet.set_index(['Month', 'Day'], inplace=True)
        return dfRet
        
    dfx=make_WorkData()
    
    dfMax=dfx[dfx['Element']=='TMAX'] #make 2 dataframes for 2 lines
    dfMin=dfx[dfx['Element']=='TMIN']

    dfMax=group_stations(dfMax, 'max') # find min-max value for each day by all stations
    dfMin=group_stations(dfMin, 'min')

    df2015Max=dfMax[dfMax['Year']==2015].drop('Year', axis=1) # select 2015 year
    df2015Min=dfMin[dfMin['Year']==2015].drop('Year', axis=1)

    dfMax=dfMax.drop(df2015Max.index) # drop 2015 years data from lines
    dfMin=dfMin.drop(df2015Min.index)

    dfMax=group_years_months(dfMax, 'max') # calc min-max values for each day, year to year
    dfMin=group_years_months(dfMin, 'min')
    
    # make lines dataframe
    dfLinesRet=make_ret_df(dfMax, dfMin, 'Max temp, C', 'Min temp, C')
    dfScatRet=make_ret_df(df2015Max, df2015Min, 'Max temp 2015, C', 'Min temp 2015, C')
    
    return (dfLinesRet, dfScatRet)

dfL, dfS=make_plotting()

print (dfS.head(20))


# In[27]:

get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt
import numpy as np
from calendar import month_abbr
from datetime import date, timedelta


# In[28]:

def listdata(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

diap_date=[result.strftime('%b %d') for result in listdata(date(2015, 1, 1), date(2016, 1, 1), timedelta(days=1))]
dfLines, dfScat=make_plotting_DF()

def plot2lines(dtf):
    #ax1=dfLines.xs(1).plot.line(figsize=(9, 5), use_index=False) # for one month

    dfx=dtf.reset_index()
    x_val=dfx.index.values
    x_ticks=dfx[dfx['Day']==1].index.tolist()

    ax1=dtf.plot.line(x_val, figsize=(9, 4), xticks=x_ticks) # plot 2 lines
    ax1.fill_between(x_val, dtf['Max temp, C'], dtf['Min temp, C'], facecolor='gainsboro') # fill betwee 2 lines
    return ax1

def format_plot_area(ax1):
    # format plot area
    ax1.spines['bottom'].set_color('black')
    ax1.spines['left'].set_color('black')

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.set_axis_bgcolor('white')

    h, l = ax1.get_legend_handles_labels()
    lines=(h[0], h[1]) #ax1.get_lines()
    h[0].set_color('indianred')
    h[1].set_color('cornflowerblue')
    ax1.legend(h, ('Max 2005-2014', 'Min 2005-2014', 
                   '2015 above Max', '2015 below Min'), loc=0, frameon=False)
    plt.setp(lines, linewidth=0.3)
    ax1.set_xticklabels([s for s in month_abbr if s!='']) 
    
    ax1.set_xlabel('')
    ax1.set_title('Assignment 2: The interval of minimum and maximum temperatures for 2005-2014 \n and temperatures of 2015, dropping out of the interval')
    ax1.set_ylabel('Temperature, C')

    
def plot_scatter(ax1):
    df=pd.merge(dfLines.reset_index(), dfScat.reset_index(), how='inner')
    df['ind']=df.index
    dfMx=df[df['Max temp 2015, C']>df['Max temp, C']]
    dfMn=df[df['Min temp 2015, C']<df['Min temp, C']]

    dfMx.plot.scatter(x='ind', y='Max temp 2015, C', label='a', ax=ax1, 
                      color='darkred', s=7)
    dfMn.plot.scatter(x='ind', y='Min temp 2015, C', label='b', ax=ax1, 
                      color='darkblue', s=7)
    return ax1

ax1=plot2lines(dfLines)
plot_scatter(ax1)
format_plot_area(ax1)


# In[25]:

def listdata(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

diap_date=[result.strftime('%b %d') for result in listdata(date(2015, 1, 1), date(2016, 1, 1), timedelta(days=1))]
#print(diap_date)


# In[ ]:



