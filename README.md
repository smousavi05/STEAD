#  STanford EArthquake Dataset (STEAD):A Global Data Set of Seismic Signals for AI          
                       
-----------------------------------------                                                                                                                                                                                   
### You can get the wavefoms from here: 
https://dl.orangedox.com/waveforms-10-29-19.hdf5

### You can get the metadata from here:
https://dl.orangedox.com/metadata-10-29-19.csv

### You can get the paper from here:
https://www.researchgate.net/publication/336598670_STanford_EArthquake_Dataset_STEAD_A_Global_Data_Set_of_Seismic_Signals_for_AI

*Note: all the metadata are aslo available in the hdf5 file (as attributes associated with each waveform).* 

### Last Update:
Oct 29, 2019

-------------------------------------
## How to access earthquake samples

    import h5py
    import matplotlib.pyplot as plt
    hdf_f = "STEAD.hdf5"
    r = h5py.File(hdf_f, 'r')

    for n in r:
        print('class: ', n)
        for nn in r[n]:
            print('category: ', nn)

class:  earthquake  
category:  local   
class:  non_earthquake   
category:  noise   

----------

    inpt =  r['earthquake']['local']
    for evi in inpt:
        print(str(evi))
        x = inpt[evi]

        fig = plt.figure()
        ax = fig.add_subplot(311)         
        plt.plot(x[:,0], 'k')
        plt.rcParams["figure.figsize"] = (8, 5)
        legend_properties = {'weight':'bold'}    
        plt.tight_layout()

        if x.attrs['trace_category'] == 'earthquake_local':    
            ymin, ymax = ax.get_ylim()
            pl = plt.vlines(x.attrs['p_arrival_sample'], ymin, ymax, color='b', linewidth=2, label='P-arrival')
            sl = plt.vlines(x.attrs['s_arrival_sample'], ymin, ymax, color='r', linewidth=2, label='S-arrival')
            cl = plt.vlines(x.attrs['coda_end_sample'], ymin, ymax, color='aqua', linewidth=2, label='Coda End')
            plt.legend(handles=[pl, sl, cl], loc = 'upper right', borderaxespad=0., prop=legend_properties)        
        plt.ylabel('Amplitude counts', fontsize=12) 
        ax.set_xticklabels([])

        ax = fig.add_subplot(312)         
        plt.plot(x[:,1], 'k')
        plt.rcParams["figure.figsize"] = (8, 5)
        legend_properties = {'weight':'bold'}    
        plt.tight_layout()

        if x.attrs['trace_category'] == 'earthquake_local':    
            ymin, ymax = ax.get_ylim()
            pl = plt.vlines(x.attrs['p_arrival_sample'], ymin, ymax, color='b', linewidth=2, label='P-arrival')
            sl = plt.vlines(x.attrs['s_arrival_sample'], ymin, ymax, color='r', linewidth=2, label='S-arrival')
            cl = plt.vlines(x.attrs['coda_end_sample'], ymin, ymax, color='aqua', linewidth=2, label='Coda End')
            plt.legend(handles=[pl, sl, cl], loc = 'upper right', borderaxespad=0., prop=legend_properties)        
        plt.ylabel('Amplitude counts', fontsize=12) 
        ax.set_xticklabels([])

        ax = fig.add_subplot(313)         
        plt.plot(x[:,2], 'k')
        plt.rcParams["figure.figsize"] = (8,5)
        legend_properties = {'weight':'bold'}    
        plt.tight_layout()

        if x.attrs['trace_category'] == 'earthquake_local':    
            ymin, ymax = ax.get_ylim()
            pl = plt.vlines(x.attrs['p_arrival_sample'], ymin, ymax, color='b', linewidth=2, label='P-arrival')
            sl = plt.vlines(x.attrs['s_arrival_sample'], ymin, ymax, color='r', linewidth=2, label='S-arrival')
            cl = plt.vlines(x.attrs['coda_end_sample'], ymin, ymax, color='aqua', linewidth=2, label='Coda End')
            plt.legend(handles=[pl, sl, cl], loc = 'upper right', borderaxespad=0., prop=legend_properties)        
        plt.ylabel('Amplitude counts', fontsize=12) 
        ax.set_xticklabels([])

        plt.show() 

        for at in x.attrs:
            print(at, x.attrs[at])    

![event](eventSample.png)

![event](eventSample2.png)


For noise samples:

    inpt =  r['non_earthquake']['noise'] 
    
------------------------------------------------------

# See the notebook for the dataset's property                                                                                  
------------------------------------------------------
