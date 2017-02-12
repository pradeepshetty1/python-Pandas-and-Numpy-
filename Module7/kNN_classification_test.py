from numpy import *
from operator import itemgetter
import csv, os

class kNNClassifier(object):
    def __init__(self):
        self.training_labels = None # movie title, genre
        self.training_features = None # movie title, kicks, kisses

        # test-data placeholder
        self.test_features = None # kicks, kisses

        # Build meaningful result
        self.elegantResult = "Most likely, {0} '{1}' is of type/class '{2}'."

    # method with sample data, for testing
    def createSampleTrainingData(self):
        self.training_features = array([[1.0,1.1],[1.0,1.0],[0,0.1],[0.0,0.0]])
        self.training_labels = ['A','A','B','B']
        self.test_features = array([1,1], dtype=float)

    def loadTrainingDataFromFile(self, file_path):
        if file_path is not None and os.path.exists(file_path):

            features = []
            self.training_labels = []

            with open(file_path, 'r') as training_data_file:
                reader = csv.DictReader(training_data_file)
                for row in reader:
                    if row['moviename'] != '?':
                        features.append([float(row['kicks']),float(row['kisses'])])
                        self.training_labels.append(row['movietype'])
                    else:
                        self.test_features = array([float(row['kicks']),float(row['kisses'])])

                if len(features) > 0:
                    self.training_features = array(features)


    def classifyTestData(self, test_data=None, k=0):
        if test_data is not None:
            self.test_features = array(test_data, dtype=float)

        # ensure we have training data, training labels, test data and number of 'k'
        if self.test_features is not None and self.training_features is not None and self.training_labels is not None and k > 0:
            featureVectorSize = self.training_features.shape[0]
            diffMat = tile(self.test_features, (featureVectorSize, 1)) - self.training_features
            sqDiffMat = diffMat ** 2
            sqDistances = sqDiffMat.sum(axis=1)
            distances = sqDistances ** 0.5
            sortedDistanceIndices = distances.argsort()
            print ' diffMat: ',diffMat
            print ' sqDiffMat: ',sqDiffMat
            print ' sqDistances: ',sqDistances
            print ' distances: ',distances
            print ' sortedDistanceIndices: ',sortedDistanceIndices

            classCount = {}
            for i in range(k):
                    voteILabel = self.training_labels[sortedDistanceIndices[i]]
                    classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
                    print ' voteILabel: ',voteILabel
                    print ' classCount[voteILabel]: ',classCount[voteILabel]
                    print '##############################'

            sortedClassCount = sorted(classCount.iteritems(), key=itemgetter(1), reverse=True)
            print ' voteILabel: ',voteILabel
            print ' classCount: ',classCount
            print ' sortedClassCount: ',sortedClassCount



            return sortedClassCount[0][0]
        else:
            return 'Cannot determine result for empty test-data.'


def predictSampleDataClass():
    #test_data =  [1.1, 1.01] # A
    test_data =  [0.1, 0.01] # B
    instance = kNNClassifier()
    instance.createSampleTrainingData()
    classOfTestData = instance.classifyTestData(test_data=test_data, k=3)
    return instance.elegantResult.format('record',str(instance.test_features),classOfTestData)

def predictMovieType():
    #test_data = [5,100]
    test_data = [50,50]

    #test_data = None
    instance = kNNClassifier()
    instance.loadTrainingDataFromFile('movies.csv')
    #classOfTestData = instance.classifyTestData(k=3)
    classOfTestData = instance.classifyTestData(test_data=test_data, k=4)
    return instance.elegantResult.format('movie','user-data',classOfTestData)


if __name__ == "__main__":
    print
    #print predictSampleDataClass()
    print
    print predictMovieType()