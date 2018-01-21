from sklearn.cross_validation import KFold


	#https://rasbt.github.io/mlxtend/user_guide/classifier/StackingClassifier/
'''
Implementing Stacking with No GridSearchCV
lg = LogisticRegression(random_state= 42)
svm = SVC(random_state= 42)
rf = RandomForestClassifier( random_state= 42, n_jobs=-1)
knn = KNeighborsClassifier()
base_learner = [['SVM', svm], ['Random Forest', rf], ['KNN',knn]]
'''

''' X_tr = np.array(X_tr)
        y_tr = np.array(y_tr)
        X_te = np.array(X_te)
        y_te = np.array(y_te)'''

	'''def setRandomState(self):
					for i in range(len(base_learners)):
						base_learners[i][2]['random_state'] = self.seed
					meta_learner[2]['random_state'] = self.seed'''
class Stacking(object):
	
    def __init__(self, seed, n_fold, base_learners, meta_learner):
        self.seed = seed
        self.n_fold = n_fold
        self.base_learners = base_learners
        self.meta_learner = meta_learner
        self.T = len(base_learners) # num of base learners

    def generateBaseLearner(self, X_tr, y_tr, X_te, y_te):
    
        n1 = X_tr.shape[0]
        n2 = X_te.shape[0]

        kf = KFold(n1, n_folds= self.n_fold, random_state= self.seed)

        #constructing data for meta learner
        meta_train = np.zeros((n1, self.T))
        meta_test = np.zeros((n2, self.T))

        for i, clf in enumerate(self.base_learners):
            meta_test_i = np.zeros((n2, self.n_fold))
            for j, (train_index, test_index) in enumerate(kf):
                X_train = X_tr[train_index]
                y_train = y_tr[train_index]
                X_holdout = X_tr[test_index]
                y_holdout = y_tr[test_index]
           
                clf[1].fit(X_train, y_train)
                y_pred = clf[1].predict(X_holdout)[:]
                
                print 'Base Learner:%s accuracy = %s' % (clf[0], metrics.accuracy_score(y_holdout, y_pred))
                # filling predicted X_holdout into meta training set
                meta_train[test_index, i] = y_pred
                meta_test_i[:, j] = clf[1].predict(X_te)[:]
            
            meta_test[:, i] = meta_test_i.mean(1)
        
        self.meta_learner.fit(meta_train, y_tr)
        y_result_pred = self.meta_learner.predict(meta_test)
       
        print 'Final accuracy = %s' % (metrics.accuracy_score(y_te, y_result_pred))
        return y_result_pred
    
  
