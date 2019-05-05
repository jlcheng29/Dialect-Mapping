#EAST1510 project
# intial project test

#CHANGELOG
# 5/2/2019


import numpy as np
from scipy.stats import zscore


def similarity(X, Y, method):
    '''
    SIMILARITY Computes similarity matrices
    Usage:
        sim = similarity(X, Y, method)
    Input:
    X   N1 x M matrix
    Y   N2 x M matrix
    method   string defining one of the following similarity measure
           'SMC', 'smc'             : Simple Matching Coefficient
           'Jaccard', 'jac'         : Jaccard coefficient
           'ExtendedJaccard', 'ext' : The Extended Jaccard coefficient
           'Cosine', 'cos'          : Cosine Similarity
           'Correlation', 'cor'     : Correlation coefficient
    Output:
    sim Estimated similarity matrix between X and Y
        If input is not binary, SMC and Jaccard will make each
        attribute binary according to x>median(x) '''

    X = np.mat(X)
    Y = np.mat(Y)
    N1, M = np.shape(X)
    N2, M = np.shape(Y)

    method = method[:3].lower()
    if method=='smc': # SMC
        #X,Y = binarize(X,Y);
        sim = ((X*Y.T)+((1-X)*(1-Y).T))/M
    elif method=='jac': # Jaccard
        X,Y = binarize(X,Y);
        sim = (X*Y.T)/(M-(1-X)*(1-Y).T)
    elif method=='ext': # Extended Jaccard
        XYt = X*Y.T
        sim = XYt / (np.log( np.exp(sum(np.power(X.T,2))).T * np.exp(sum(np.power(Y.T,2))) ) - XYt)
    elif method=='cos': # Cosine
        sim = (X*Y.T)/(np.sqrt(sum(np.power(X.T,2))).T * np.sqrt(sum(np.power(Y.T,2))))
    elif method=='cor': # Correlation
        X_ = zscore(X,axis=1,ddof=1)
        Y_ = zscore(Y,axis=1,ddof=1)
        sim = (X_*Y_.T)/(M-1)
    return sim

def binarize(X,Y=None):
    ''' Force binary representation of the matrix, according to X>median(X) '''
    if Y==None:
        X = np.matrix(X)
        Xmedians = np.ones((np.shape(X)[0],1)) * np.median(X,0)
        Xflags = X>Xmedians
        X[Xflags] = 1; X[~Xflags] = 0
        return X
    else:
        X = np.matrix(X); Y = np.matrix(Y);
        XYmedian= np.median(np.bmat('X; Y'),0)
        Xmedians = np.ones((np.shape(X)[0],1)) * XYmedian
        Xflags = X>Xmedians
        X[Xflags] = 1; X[~Xflags] = 0
        Ymedians = np.ones((np.shape(Y)[0],1)) * XYmedian
        Yflags = Y>Ymedians
        Y[Yflags] = 1; Y[~Yflags] = 0
        return [X,Y]
from scipy.spatial import distance
distance.jaccard(bj,sf)
#initialize array of Norman values
bj = [1,1,1,1,1,1,1,1,1,1];#Beijing
xa = [1,1,1,1,1,1,1,1,1,1];#Xian
km = [1,1,1,1,1,1,1,1,1,1];#Kunming
sz = [0,0,1,1,0,1,0,1,1,0.5];#Suzhou
wz = [0,0,1,1,0,1,0,1,1,0];#Wenzhou
cs = [1,0,1,0,0,1,1,1,0,0.5];#Changsha
sf = [1,0,1,0,0,1,0.5,0,0,0.5];#Shuangfeng
nc = [0,0,1,0,0,1,1,1,0,0];#Nanchang
mx = [0,0,0,0,0,0,0,0,0,0];#Meixian
gz = [0,0,0,0,0,0,0,0,0,0];#Guangzhou
fz = [0,0,0,0,0,0,0,0,0,0];#Fuzhou
jo = [0,0,0,0,0,0,0,0,0,0];#Jianou
#similarity(bj,sz, 'SMC')

np.sum(bj)

Norman = [bj,xa,km,sz,wz,cs,sf,nc,mx,gz,fz,jo];


cityNamesNorman = ['bj','xa','km','sz','wz','cs','sf','nc','mx','gz','fz','jo'];
lenNorman = len(Norman);
i = 0;
cityNamesNorman[0]

## Calculation of Norman sums
for city in Norman:
    cityName = cityNamesNorman[i]
    i +=1;
    print(cityName)
    citySum = np.sum(city)
    print(citySum)

## calculation of similarity values (simple matching and Jaccard index, within the cities)
for city in Norman:
    cityName = cityNamesNorman[i];
    i +=1;
    j = 0;
    print(cityName)
    for cityIndex in range(0,lenNorman):
        #calling our predifined jaccard functions
        similarityVal = (similarity(city,Norman[cityIndex],'smc'))
        comparisionCity = cityNamesNorman[j];
        j +=1;
        print(similarityVal[0][0]," is the similarity val for Comparison city ",comparisionCity)


#find dataset with at least 10 words that are pronounced similarly.
