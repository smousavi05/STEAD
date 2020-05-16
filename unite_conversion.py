#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:35:07 2020

@author: mostafamousavi
"""
import obspy
import h5py
from obspy import UTCDateTime
import numpy as np
from obspy.clients.fdsn.client import Client
import matplotlib.pyplot as plt

 
def make_stream(dataset):
    '''
    input: hdf5 dataset
    output: obspy stream
    
    '''
    data = np.array(dataset)
              
    tr_E = obspy.Trace(data=data[:, 0])
    tr_E.stats.starttime = UTCDateTime(dataset.attrs['trace_start_time'])
    tr_E.stats.delta = 0.01
    tr_E.stats.channel = dataset.attrs['receiver_type']+'E'
    tr_E.stats.station = dataset.attrs['receiver_code']
    tr_E.stats.network = dataset.attrs['network_code']
    
    tr_N = obspy.Trace(data=data[:, 1])
    tr_N.stats.starttime = UTCDateTime(dataset.attrs['trace_start_time'])
    tr_N.stats.delta = 0.01
    tr_N.stats.channel = dataset.attrs['receiver_type']+'N'
    tr_N.stats.station = dataset.attrs['receiver_code']
    tr_N.stats.network = dataset.attrs['network_code']
    
    tr_Z = obspy.Trace(data=data[:, 2])
    tr_Z.stats.starttime = UTCDateTime(dataset.attrs['trace_start_time'])
    tr_Z.stats.delta = 0.01
    tr_Z.stats.channel = dataset.attrs['receiver_type']+'Z'
    tr_Z.stats.station = dataset.attrs['receiver_code']
    tr_Z.stats.network = dataset.attrs['network_code']

    stream = obspy.Stream([tr_E, tr_N, tr_Z])
    
    return stream

# reading one sample trace from STEAD
file_name = "dataset6/waveforms_12_20_19.hdf5"
dtfl = h5py.File(file_name, 'r')
dataset = dtfl.get('earthquake/local/109C.TA_20061103161223_EV') 

# convering hdf5 dataset into obspy sream
st = make_stream(dataset)
# ploting the verical component of the raw data
tr_Z = st[2]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr_Z.times("matplotlib"), tr_Z.data, "k-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.ylabel('counts')
plt.title('Raw Data')
fig.tight_layout()
plt.show()
fig.savefig('1_raw.png')   

# downloading the instrument response of the station from IRIS
client = Client("IRIS")
inventory = client.get_stations(network=dataset.attrs['network_code'],
                                station=dataset.attrs['receiver_code'],
                                starttime=UTCDateTime(dataset.attrs['trace_start_time']),
                                endtime=UTCDateTime(dataset.attrs['trace_start_time']) + 60,
                                loc="*", 
                                channel="*",
                                level="response")  
# exploring the downloaded response file   
print(inventory)
inventory[0].plot_response(min_freq=1E-4) 


# converting into displacement
st = make_stream(dataset)
st = st.remove_response(inventory=inventory, output="DISP", plot=False)
tr_Z = st[2]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr_Z.times("matplotlib"), tr_Z.data, "k-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.ylabel('meters')
plt.title('Displacement')
fig.tight_layout()
plt.show()
fig.savefig('1_disp.png')   


# converting into velocity
st = make_stream(dataset)
st = st.remove_response(inventory=inventory, output='VEL', plot=False) 
tr_Z = st[2]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr_Z.times("matplotlib"), tr_Z.data, "k-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.ylabel('meters/second')
plt.title('Velocity')
fig.tight_layout()
plt.show()
fig.savefig('1_vel.png')   

# converting into acceleration
st = make_stream(dataset)
st.remove_response(inventory=inventory, output="ACC", plot=False) 
tr_Z = st[2]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr_Z.times("matplotlib"), tr_Z.data, "k-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.ylabel('meters/second**2')
plt.title('Acceleration')
fig.tight_layout()
plt.show()
fig.savefig('1_acc.png')   
