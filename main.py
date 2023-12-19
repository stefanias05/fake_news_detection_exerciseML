from matplotlib import pyplot as plt
from pandas import read_csv
import seaborn as sns


#region 1. IMPORT DATA

name = ['title','text','subject','date','class']
data = read_csv('C:/Users/soare/Downloads/News.csv', names=name)

# print(data.head(20))




#endregion

#region 2. PREPROCESING DATA

# print(data.describe())
# print(data.shape)
data = data.drop(['title','subject','date'], axis=1)
data.isnull().sum()  #no null values
# print(data)

#drop the index and order data
data = data.sample(frac=1)
data.reset_index(inplace=True)
data.drop(["index"], axis=1, inplace=True)

#plot data, order values by class
sns.countplot(data=data,
              x='class',
              order=data['class'].value_counts().index)
# plt.show()
#endregion

#region 3. Analysis data

#endregion