# one-hot encode the breast cancer dataset
from pandas import read_csv
from sklearn.preprocessing import OneHotEncoder

# define the location of the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv"

# load the dataset
dataset = read_csv(url, header=None)

# retrieve the array of data
data = dataset.values

# separate into input and output columns
X = data[:, :-1].astype(str)
y = data[:, -1].astype(str)

# summarize the raw data
print(X[:3, :])

# define the one hot encoding transform
encoder = OneHotEncoder(sparse=False)

# fit and apply the transform to the input data
X_oe = encoder.fit_transform(X)

# summarize the transformed data
print(X_oe[:3, :])
