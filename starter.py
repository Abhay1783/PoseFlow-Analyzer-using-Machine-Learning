from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


#There is 1 csv file in the current version of the dataset:

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))



<iframe src="https://www.kaggle.com/embed/nicolehoelzl/starter-mpii-human-pose-data-6eaf8519-a?cellIds=5&kernelSessionId=50643668" height="300" style="margin: 0 auto; width: 100%; max-width: 950px;" frameborder="0" scrolling="auto" title="Starter: MPII Human Pose Data 6eaf8519-a"></iframe>


data = pd.read_csv(os.path.join(dirname + '/' + filename))


#<class 'pandas.core.frame.DataFrame'>
RangeIndex: 17372 entries, 0 to 17371
Data columns (total 37 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            17372 non-null  int64  
 1   NAME          17372 non-null  object 
 2   r ankle_X     17372 non-null  int64  
 3   r ankle_Y     17372 non-null  int64  
 4   r knee_X      17372 non-null  int64  
 5   r knee_Y      17372 non-null  int64  
 6   r hip_X       17372 non-null  int64  
 7   r hip_Y       17372 non-null  int64  
 8   l hip_X       17372 non-null  int64  
 9   l hip_Y       17372 non-null  int64  
 10  l knee_X      17372 non-null  int64  
 11  l knee_Y      17372 non-null  int64  
 12  l ankle_X     17372 non-null  int64  
 13  l ankle_Y     17372 non-null  int64  
 14  pelvis_X      17372 non-null  int64  
 15  pelvis_Y      17372 non-null  int64  
 16  thorax_X      17372 non-null  int64  
 17  thorax_Y      17372 non-null  int64  
 18  upper neck_X  17372 non-null  float64
 19  upper neck_Y  17372 non-null  float64
 20  head top_X    17372 non-null  float64
 21  head top_Y    17372 non-null  float64
 22  r wrist_X     17372 non-null  int64  
 23  r wrist_Y     17372 non-null  int64  
 24  r elbow_X     17372 non-null  int64  
 25  r elbow_Y     17372 non-null  int64  
 26  r shoulder_X  17372 non-null  int64  
 27  r shoulder_Y  17372 non-null  int64  
 28  l shoulder_X  17372 non-null  int64  
 29  l shoulder_Y  17372 non-null  int64  
 30  l elbow_X     17372 non-null  int64  
 31  l elbow_Y     17372 non-null  int64  
 32  l wrist_X     17372 non-null  int64  
 33  l wrist_Y     17372 non-null  int64  
 34  Scale         17372 non-null  float64
 35  Activity      17372 non-null  object 
 36  Category      17372 non-null  object 
dtypes: float64(5), int64(29), object(3)
memory usage: 4.9+ MB



nRowsRead = 1000 # specify 'None' if want to read whole file
# mpii_human_pose.csv may have more rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv('/kaggle/input/mpii_human_pose.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'mpii_human_pose.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')

df1.head(5)

plotPerColumnDistribution(df1, 10, 5)
