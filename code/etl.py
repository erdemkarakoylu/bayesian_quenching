# Package ID: edi.1777.1 Cataloging System:https://pasta.edirepository.org.
# Data set title: Non-Photochemical Quenching (NPQ) data for Lake Tahoe and Clear Lake 2016-2022.
# Data set creator:  Samantha Sharp - UC Davis 
# Data set creator:  Alexander Forrest - UC Davis 
# Data set creator:  Derek Roberts - UC Davis 
# Data set creator:  Alicia CortÃ©s - UC Davis 
# Data set creator:  S. Geoffrey Schladow - UC Davis 
# Contact:  Samantha Sharp -  UC Davis  - ssharp@ucdavis.edu
# Stylesheet v1.3 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/f027347be8585882fdc779cdb1e73de6".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(Time_local_datetime=pd.to_datetime(dt1.Time_local,errors='coerce')) 
dt1.Chla_ugL=pd.to_numeric(dt1.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt1.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/37b1a67eb898279ad46e1a89a48c45ad".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt2=dt2.assign(Time_local_datetime=pd.to_datetime(dt2.Time_local,errors='coerce')) 
dt2.Chla_ugL=pd.to_numeric(dt2.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt2.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt2.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile3  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/3df8baf3ff2e65cf2b50389de8d8f906".strip() 
infile3  = infile3.replace("https://","http://")
                 
dt3 =pd.read_csv(infile3 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt3=dt3.assign(Time_local_datetime=pd.to_datetime(dt3.Time_local,errors='coerce')) 
dt3.Chla_ugL=pd.to_numeric(dt3.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt3 and number of lines\n")
print(dt3.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt3\n")
print(dt3.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt3.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt3.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile4  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/dbf358dbce6a498c0c61f11f164186d3".strip() 
infile4  = infile4.replace("https://","http://")
                 
dt4 =pd.read_csv(infile4 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt4=dt4.assign(Time_local_datetime=pd.to_datetime(dt4.Time_local,errors='coerce')) 
dt4.Chla_ugL=pd.to_numeric(dt4.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt4 and number of lines\n")
print(dt4.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt4\n")
print(dt4.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt4.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt4.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile5  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/77752e39bc2f9f25068a1553062bf3aa".strip() 
infile5  = infile5.replace("https://","http://")
                 
dt5 =pd.read_csv(infile5 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt5=dt5.assign(Time_local_datetime=pd.to_datetime(dt5.Time_local,errors='coerce')) 
dt5.Chla_ugL=pd.to_numeric(dt5.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt5 and number of lines\n")
print(dt5.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt5\n")
print(dt5.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt5.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt5.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile6  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/36efb28720b01b1d89f36a2441ea2c14".strip() 
infile6  = infile6.replace("https://","http://")
                 
dt6 =pd.read_csv(infile6 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt6=dt6.assign(Time_local_datetime=pd.to_datetime(dt6.Time_local,errors='coerce')) 
dt6.Chla_ugL=pd.to_numeric(dt6.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt6 and number of lines\n")
print(dt6.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt6\n")
print(dt6.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt6.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt6.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile7  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/bad7330b626acb7d4b57e24d854975af".strip() 
infile7  = infile7.replace("https://","http://")
                 
dt7 =pd.read_csv(infile7 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL",     
                    "Pheo_ugL",     
                    "Notes"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float' , 
#             'Pheo_ugL':'float' ,  
#             'Notes':'str'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt7=dt7.assign(Time_local_datetime=pd.to_datetime(dt7.Time_local,errors='coerce')) 
dt7.Chla_ugL=pd.to_numeric(dt7.Chla_ugL,errors='coerce') 
dt7.Pheo_ugL=pd.to_numeric(dt7.Pheo_ugL,errors='coerce')  
dt7.Notes=dt7.Notes.astype('category') 
      
print("Here is a description of the data frame dt7 and number of lines\n")
print(dt7.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt7\n")
print(dt7.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt7.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt7.Chla_ugL.describe())               
print("--------------------\n\n")
                    
print(dt7.Pheo_ugL.describe())               
print("--------------------\n\n")
                    
print(dt7.Notes.describe())               
print("--------------------\n\n")
                    
                    
                 

infile8  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/2c7eb7cc79cccd00950642382a56e67d".strip() 
infile8  = infile8.replace("https://","http://")
                 
dt8 =pd.read_csv(infile8 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL",     
                    "Pheo_ugL",     
                    "Notes"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float' , 
#             'Pheo_ugL':'float' ,  
#             'Notes':'str'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt8=dt8.assign(Time_local_datetime=pd.to_datetime(dt8.Time_local,errors='coerce')) 
dt8.Chla_ugL=pd.to_numeric(dt8.Chla_ugL,errors='coerce') 
dt8.Pheo_ugL=pd.to_numeric(dt8.Pheo_ugL,errors='coerce')  
dt8.Notes=dt8.Notes.astype('category') 
      
print("Here is a description of the data frame dt8 and number of lines\n")
print(dt8.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt8\n")
print(dt8.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt8.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt8.Chla_ugL.describe())               
print("--------------------\n\n")
                    
print(dt8.Pheo_ugL.describe())               
print("--------------------\n\n")
                    
print(dt8.Notes.describe())               
print("--------------------\n\n")
                    
                    
                 

infile9  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/6d5e36e243523431b8d7cae3b8408d23".strip() 
infile9  = infile9.replace("https://","http://")
                 
dt9 =pd.read_csv(infile9 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL",     
                    "Pheo_ugL",     
                    "Notes"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float' , 
#             'Pheo_ugL':'float' ,  
#             'Notes':'str'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt9=dt9.assign(Time_local_datetime=pd.to_datetime(dt9.Time_local,errors='coerce')) 
dt9.Chla_ugL=pd.to_numeric(dt9.Chla_ugL,errors='coerce') 
dt9.Pheo_ugL=pd.to_numeric(dt9.Pheo_ugL,errors='coerce')  
dt9.Notes=dt9.Notes.astype('category') 
      
print("Here is a description of the data frame dt9 and number of lines\n")
print(dt9.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt9\n")
print(dt9.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt9.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt9.Chla_ugL.describe())               
print("--------------------\n\n")
                    
print(dt9.Pheo_ugL.describe())               
print("--------------------\n\n")
                    
print(dt9.Notes.describe())               
print("--------------------\n\n")
                    
                    
                 

infile10  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/92d85dccba5fbaefca4a2244c8d58d14".strip() 
infile10  = infile10.replace("https://","http://")
                 
dt10 =pd.read_csv(infile10 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL",     
                    "Pheo_ugL",     
                    "Notes"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float' , 
#             'Pheo_ugL':'float' ,  
#             'Notes':'str'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt10=dt10.assign(Time_local_datetime=pd.to_datetime(dt10.Time_local,errors='coerce')) 
dt10.Chla_ugL=pd.to_numeric(dt10.Chla_ugL,errors='coerce') 
dt10.Pheo_ugL=pd.to_numeric(dt10.Pheo_ugL,errors='coerce')  
dt10.Notes=dt10.Notes.astype('category') 
      
print("Here is a description of the data frame dt10 and number of lines\n")
print(dt10.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt10\n")
print(dt10.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt10.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt10.Chla_ugL.describe())               
print("--------------------\n\n")
                    
print(dt10.Pheo_ugL.describe())               
print("--------------------\n\n")
                    
print(dt10.Notes.describe())               
print("--------------------\n\n")
                    
                    
                 

infile11  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/642ca5f871af3af7ab0e5cf13be74a32".strip() 
infile11  = infile11.replace("https://","http://")
                 
dt11 =pd.read_csv(infile11 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL",     
                    "Pheo_ugL",     
                    "Notes"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float' , 
#             'Pheo_ugL':'float' ,  
#             'Notes':'str'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt11=dt11.assign(Time_local_datetime=pd.to_datetime(dt11.Time_local,errors='coerce')) 
dt11.Chla_ugL=pd.to_numeric(dt11.Chla_ugL,errors='coerce') 
dt11.Pheo_ugL=pd.to_numeric(dt11.Pheo_ugL,errors='coerce')  
dt11.Notes=dt11.Notes.astype('category') 
      
print("Here is a description of the data frame dt11 and number of lines\n")
print(dt11.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt11\n")
print(dt11.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt11.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt11.Chla_ugL.describe())               
print("--------------------\n\n")
                    
print(dt11.Pheo_ugL.describe())               
print("--------------------\n\n")
                    
print(dt11.Notes.describe())               
print("--------------------\n\n")
                    
                    
                 

infile12  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/51a47e2a5cb31977845adb10ea4b05ff".strip() 
infile12  = infile12.replace("https://","http://")
                 
dt12 =pd.read_csv(infile12 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt12=dt12.assign(Time_local_datetime=pd.to_datetime(dt12.Time_local,errors='coerce')) 
dt12.Chla_ugL=pd.to_numeric(dt12.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt12 and number of lines\n")
print(dt12.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt12\n")
print(dt12.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt12.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt12.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile13  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/0eb1593a24ed0df07a8b90de0e0b3a34".strip() 
infile13  = infile13.replace("https://","http://")
                 
dt13 =pd.read_csv(infile13 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt13=dt13.assign(Time_local_datetime=pd.to_datetime(dt13.Time_local,errors='coerce')) 
dt13.Chla_ugL=pd.to_numeric(dt13.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt13 and number of lines\n")
print(dt13.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt13\n")
print(dt13.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt13.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt13.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile14  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/28e964463d77f40c1e482019591967fd".strip() 
infile14  = infile14.replace("https://","http://")
                 
dt14 =pd.read_csv(infile14 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt14=dt14.assign(Time_local_datetime=pd.to_datetime(dt14.Time_local,errors='coerce')) 
dt14.Chla_ugL=pd.to_numeric(dt14.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt14 and number of lines\n")
print(dt14.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt14\n")
print(dt14.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt14.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt14.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile15  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/ed27c59c4d838d747f66f00bfa25e3a0".strip() 
infile15  = infile15.replace("https://","http://")
                 
dt15 =pd.read_csv(infile15 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt15=dt15.assign(Time_local_datetime=pd.to_datetime(dt15.Time_local,errors='coerce')) 
dt15.Chla_ugL=pd.to_numeric(dt15.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt15 and number of lines\n")
print(dt15.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt15\n")
print(dt15.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt15.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt15.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile16  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/e634e4cb8b30780ce1a7f94b70cfcc80".strip() 
infile16  = infile16.replace("https://","http://")
                 
dt16 =pd.read_csv(infile16 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt16=dt16.assign(Time_local_datetime=pd.to_datetime(dt16.Time_local,errors='coerce')) 
dt16.Chla_ugL=pd.to_numeric(dt16.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt16 and number of lines\n")
print(dt16.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt16\n")
print(dt16.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt16.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt16.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile17  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/d0475bf54ef83a5fa0904fc8c4af483b".strip() 
infile17  = infile17.replace("https://","http://")
                 
dt17 =pd.read_csv(infile17 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt17=dt17.assign(Time_local_datetime=pd.to_datetime(dt17.Time_local,errors='coerce')) 
dt17.Chla_ugL=pd.to_numeric(dt17.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt17 and number of lines\n")
print(dt17.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt17\n")
print(dt17.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt17.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt17.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile18  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/5e665179a91b929b239a803b76353886".strip() 
infile18  = infile18.replace("https://","http://")
                 
dt18 =pd.read_csv(infile18 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt18=dt18.assign(Time_local_datetime=pd.to_datetime(dt18.Time_local,errors='coerce')) 
dt18.Chla_ugL=pd.to_numeric(dt18.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt18 and number of lines\n")
print(dt18.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt18\n")
print(dt18.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt18.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt18.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                 

infile19  ="https://pasta.lternet.edu/package/data/eml/edi/1777/1/c96271bdef5a7759b24e4ea8c5b15044".strip() 
infile19  = infile19.replace("https://","http://")
                 
dt19 =pd.read_csv(infile19 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Time_local",     
                    "Chla_ugL"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'Time_local':'str' , 
#             'Chla_ugL':'float'  
#        }
          ,parse_dates=[
                        'Time_local',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt19=dt19.assign(Time_local_datetime=pd.to_datetime(dt19.Time_local,errors='coerce')) 
dt19.Chla_ugL=pd.to_numeric(dt19.Chla_ugL,errors='coerce') 
      
print("Here is a description of the data frame dt19 and number of lines\n")
print(dt19.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt19\n")
print(dt19.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt19.Time_local.describe())               
print("--------------------\n\n")
                    
print(dt19.Chla_ugL.describe())               
print("--------------------\n\n")
                    
                    
                





