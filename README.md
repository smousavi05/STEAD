#  STanford EArthquake Dataset (STEAD):A Global Data Set of Seismic Signals for AI                                                                                                                                                                                                      
![map](map2.png)

![map](stations2.png)

-----------------------------------------                                                                                                                                                                                   
### You can get the wavefoms from here: 
https://rebrand.ly/waveforms-11-13-19  (this is a single hdf5 file, 83 GB)

### You can get the metadata from here :
https://rebrand.ly/metadata-11-13-19   (this is a single csv file, 350 MB)

* Note: all the metadata are aslo available in the hdf5 file (as attributes associated with each waveform).

### You can get the paper from here:
https://ieeexplore.ieee.org/abstract/document/8871127

### You can send your questions or suggestions to: 
mmousavi@stanford.edu

### Last Update:
Nov 15, 2019


-------------------------------------
## Reference:

`Mousavi, S. M., Sheng, Y., Zhu, W., Beroza G.C., (2019). 
STanford EArthquake Dataset (STEAD): A Global Data Set of Seismic Signals for AI, 
IEEE Access, doi:10.1109/ACCESS.2019.2947848` 


BibTeX:

    @article{mousavi2019stanford,
      title={STanford EArthquake Dataset (STEAD): A Global Data Set of Seismic Signals for AI},
      author={Mousavi, S Mostafa and Sheng, Yixiao and Zhu, Weiqiang and Beroza, Gregory C},
      journal={IEEE Access},
      year={2019},
      publisher={IEEE}
    }

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
