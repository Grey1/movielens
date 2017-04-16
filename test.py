
import numpy as np
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd
def predict(ratings, similarity):
    pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

    return pred


header = ['user_id','item_id','rating','timestamp']
df = pd.read_csv('ratings.csv',sep=',',names=header)
print('done')
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print(n_users)
print(n_items)
train_data, test_data = cv.train_test_split(df, test_size=0.25)
print('done')
train_data_matrix = np.zeros((n_users, n_items))
i =0
movielist=[]
for line in train_data.itertuples():
	if line[2] not in movielist:
		movielist.append(line[2])

for line in train_data.itertuples():
	print(line[3])
	train_data_matrix[int(line[1]) - 1, movielist.index(line[2]) - 1] = float(line[3])
	# test_data_matrix = np.zeros((n_users, n_items))
	# for line in test_data.itertuples():
	#test_data_matrix[line['user'] - 1, line['movie'] - 1] = line['rating']

print('done')
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')
item_prediction = predict(train_data_matrix, item_similarity)

print('done')
for j in range(n_users): 
        for i in item_prediction[j]:
            
            if i>0.9: print(i)

