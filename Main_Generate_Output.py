import datetime
import csv
from itertools import combinations
import numpy
from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import Features_manager
import Database_manager
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

print('###############################')
print('START: ', datetime.datetime.now())

# initializate database_manager
database_manager = Database_manager.make_database_manager()
# initializate feature_manager
feature_manager = Features_manager.make_feature_manager()

tweets_training = numpy.array(database_manager.return_tweets_training())
labels_training = numpy.array(feature_manager.get_label(tweets_training))

feature_types = [
                 "unigrams",
                 # "ngrams",
                 # "chargrams",
                 # "puntuactionmarks",
                 # "capitalizedletters",
                 # "laughter",
                 # "upos",
                 # "deprelneg",
                 # "deprel",
                 # "relationformVERB",
                 # "relationformNOUN",
                 # "relationformADJ",
                 # "Sidorovbigramsform",
                 # "Sidorovbigramsupostag",
                 # "Sidorovbigramsdeprel"
                ]

tweets_test = numpy.array(database_manager.return_tweets_test())
labels_test = numpy.array(feature_manager.get_label(tweets_test))


print("train: ", len(tweets_training))
print("test: ", len(tweets_test))

X, X_test, feature_name, feature_index = feature_manager.create_feature_space(tweets_training, feature_types, tweets_test)


# print(feature_name)
print("feature space dimension X:", X.shape)
print("feature space dimension X_test:", X_test.shape)
print('################################')

# count = 0
# N = len(feature_types)
# for K in range(1, N+1):
#     for subset in combinations(range(0, N), K):

# feature_index_filtered = numpy.array([feature_types)
# feature_index_filtered = numpy.concatenate(feature_type_indexes[feature_index_filtered])
#
# print("features:", feature_types)
# print("features names:", feature_names[list(feature_index_filtered)][:10])
#
# # extracts the columns of the features considered in the current combination (the feature space is reduced)
# X_filter = X[:, feature_index_filtered]
# X_test_filter = X_test[:, feature_index_filtered]

clf = SVC(kernel='linear')
#
# clf = LogisticRegression(C=1.0,
#                          penalty='l2',
#                          dual=False,
#                          tol=0.0001,
#                          fit_intercept=True,
#                          intercept_scaling=1,
#                          class_weight=None,
#                          random_state=None,
#                          solver='lbfgs',
#                          max_iter=500,
#                          verbose=0,
#                          warm_start=False,
#                          n_jobs=None)
#
# clf = RandomForestClassifier()
#
# clf = MLPClassifier(hidden_layer_sizes=(30,), #
#                     learning_rate_init=0.01,
#                     activation='logistic', #
#                     solver='lbfgs', #
#                     verbose=True,
#                     batch_size=5, #
#                     early_stopping=True,
#                     max_iter=15) #
#
# clf = GridSearchCV(MLPClassifier(), param_grid, cv=3, scoring='accuracy')
#
# clf.fit(X_filter, labels_training)
# test_predict = clf.predict(X_test_filter)
clf.fit(X, labels_training)
test_predict = clf.predict(X_test)

# print("Best parameters set found on development set:")
# print(clf.best_params_)

for i in range(0, len(tweets_test)):
    csvfile = open("spanish_unigrams.csv", 'w', newline='')
    spamwriter = csv.writer(csvfile, delimiter='\t')
    spamwriter.writerow(['idtwitter', 'irony'])
    csvfile.close()

for i in range(0, len(tweets_test)):
    csvfile = open("spanish_unigrams.csv", 'a', newline='')
    spamwriter = csv.writer(csvfile, delimiter='\t')
    spamwriter.writerow([tweets_test[i].id, test_predict[i]])
    csvfile.close()

# count = count+1
# print('Iterazione n#:', count, '----->', datetime.datetime.now())


print('END: ', datetime.datetime.now())
print('###############################')
