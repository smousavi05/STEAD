#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:52:58 2020

@author: mostafamousavi
"""

import h5py
import csv
import numpy as np
import glob

 
def main(inp_name): 
    '''
        This function gets a string (name of output files) as input, generates two files:
        "input_name.hdf5" and "input_name.csv" and write the contents of all chunk?.hdf5 
        files in the same directory into them. 
    '''
    output_merge = inp_name+'.hdf5'
    HDF0 = h5py.File(output_merge, 'a')
    HDF0.create_group("data")
     
    csvfile = open(output_merge.split('.')[0]+'.csv', 'w')          
    output_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['network_code','receiver_code','receiver_type','receiver_latitude','receiver_longitude',
                                 'receiver_elevation_m','p_arrival_sample','p_status','p_weight','p_travel_sec', 
                                 's_arrival_sample','s_status','s_weight',
                                 'source_id','source_origin_time','source_origin_uncertainty_sec', 
                                 'source_latitude','source_longitude','source_error_sec',
                                 'source_gap_deg','source_horizontal_uncertainty_km', 'source_depth_km', 'source_depth_uncertainty_km',
                                 'source_magnitude', 'source_magnitude_type', 'source_magnitude_author','source_mechanism_strike_dip_rake',
                                 'source_distance_deg', 'source_distance_km', 'back_azimuth_deg', 'snr_db', 'coda_end_sample', 
                                 'trace_start_time', 'trace_category', 'trace_name'])
    csvfile.flush()
    print('output files have been generated!')
    
    for h5name in glob.glob('chunk*.hdf5'):
        print('working on '+h5name+'...')
        dtfl = h5py.File(h5name, 'r') 
        for evi in dtfl['data']:
            print(evi)
            x = dtfl.get('data/'+str(evi)) 
            data = np.array(x)
                   
            HDFr = h5py.File(output_merge, 'a')
            dsF = HDFr.create_dataset("data/"+evi, data.shape, data=data, dtype=np.float32) 
             
            dsF.attrs['network_code'] = x.attrs['network_code']
            dsF.attrs['receiver_code'] = x.attrs['receiver_code']
            dsF.attrs['receiver_type'] = x.attrs['receiver_type']
            dsF.attrs['receiver_latitude'] = x.attrs['receiver_latitude']
            dsF.attrs['receiver_longitude'] = x.attrs['receiver_longitude']
            dsF.attrs['receiver_elevation_m'] = x.attrs['receiver_elevation_m']
            dsF.attrs['p_arrival_sample'] = x.attrs['p_arrival_sample']
            dsF.attrs['p_status'] = x.attrs['p_status']
            dsF.attrs['p_weight'] = x.attrs['p_weight']
            dsF.attrs['p_travel_sec'] = x.attrs['p_travel_sec']
            dsF.attrs['s_arrival_sample'] = x.attrs['s_arrival_sample']
            dsF.attrs['s_status'] = x.attrs['s_status']
            dsF.attrs['s_weight'] = x.attrs['s_weight']
            dsF.attrs['source_id'] = x.attrs['source_id']
            dsF.attrs['source_origin_time'] = x.attrs['source_origin_time']
            dsF.attrs['source_origin_uncertainty_sec'] = x.attrs['source_origin_uncertainty_sec']
            dsF.attrs['source_latitude'] = x.attrs['source_latitude']
            dsF.attrs['source_longitude'] = x.attrs['source_longitude']
            dsF.attrs['source_error_sec'] = x.attrs['source_error_sec']
            dsF.attrs['source_gap_deg'] = x.attrs['source_gap_deg']
            dsF.attrs['source_horizontal_uncertainty_km'] = x.attrs['source_horizontal_uncertainty_km']
            dsF.attrs['source_depth_km'] = x.attrs['source_depth_km']
            dsF.attrs['source_depth_uncertainty_km'] = x.attrs['source_depth_uncertainty_km']
            dsF.attrs['source_magnitude'] = x.attrs['source_magnitude']
            dsF.attrs['source_magnitude_type'] = x.attrs['source_magnitude_type']
            dsF.attrs['source_magnitude_author'] = x.attrs['source_magnitude_author']
            dsF.attrs['source_mechanism_strike_dip_rake'] = x.attrs['source_mechanism_strike_dip_rake']
            dsF.attrs['source_distance_deg'] = x.attrs['source_distance_deg']
            dsF.attrs['source_distance_km'] = x.attrs['source_distance_km']
            dsF.attrs['back_azimuth_deg'] = x.attrs['back_azimuth_deg']
            dsF.attrs['snr_db'] = x.attrs['snr_db']
            dsF.attrs['coda_end_sample'] = x.attrs['coda_end_sample']
            dsF.attrs['trace_start_time'] = x.attrs['trace_start_time'] 
            dsF.attrs['trace_category'] = x.attrs['trace_category'] 
            dsF.attrs['trace_name'] = x.attrs['trace_name']  
            HDFr.flush() 
           
             
            output_writer.writerow([x.attrs['network_code'], 
                                    x.attrs['receiver_code'], 
                                    x.attrs['receiver_type'],
                                    x.attrs['receiver_latitude'], 
                                    x.attrs['receiver_longitude'], 
                                    x.attrs['receiver_elevation_m'], 
                                    x.attrs['p_arrival_sample'], 
                                    x.attrs['p_status'],
                                    x.attrs['p_weight'], 
                                    x.attrs['p_travel_sec'], 
                                    x.attrs['s_arrival_sample'],
                                    x.attrs['s_status'], 
                                    x.attrs['s_weight'],
                                    x.attrs['source_id'], 
                                    x.attrs['source_origin_time'], 
                                    x.attrs['source_origin_uncertainty_sec'], 
                                    x.attrs['source_latitude'],
                                    x.attrs['source_longitude'],
                                    x.attrs['source_error_sec'], 
                                    x.attrs['source_gap_deg'],
                                    x.attrs['source_horizontal_uncertainty_km'],   
                                    x.attrs['source_depth_km'],
                                    x.attrs['source_depth_uncertainty_km'],
                                    x.attrs['source_magnitude'], 
                                    x.attrs['source_magnitude_type'], 
                                    x.attrs['source_magnitude_author'], 
                                    x.attrs['source_mechanism_strike_dip_rake'],
                                    x.attrs['source_distance_deg'],
                                    x.attrs['source_distance_km'],
                                    x.attrs['back_azimuth_deg'],
                                    x.attrs['snr_db'], 
                                    x.attrs['coda_end_sample'], 
                                    x.attrs['trace_start_time'], 
                                    x.attrs['trace_category'], 
                                    x.attrs['trace_name']]);            
            csvfile.flush()        
            HDFr.close()    
                
        
if __name__ == '__main__':
  #  inp_name=input("Please enter a name for the output files!") 
    inp_name="merged"    
    main(inp_name)    