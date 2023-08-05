import sys
assert(sys.version_info.major>2)
import gridlabd
import time
import pandas
#import pdb; pdb.set_trace()

###USER input
ind = 1
df_settings = pandas.read_csv('settings.csv',index_col=[0]) #,parse_dates=['start_time','end_time'])

##################
#Run GridlabD
#################
print('run Gridlabd')
gridlabd.command('IEEE123_BP_2bus_1min.glm')
gridlabd.command('-D')
gridlabd.command('suppress_repeat_messages=FALSE')
#gridlabd.command('--debug')
#gridlabd.command('--verbose')
gridlabd.command('--warn')
gridlabd.start('wait')
