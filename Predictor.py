import numpy as np
import geocoder
import cv2
import glob
import time
from keras.models import Sequential
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def start():
	cred = credentials.Certificate("apikey.json")
	firebase_admin.initialize_app(cred)
	db=firestore.client()


	global size
	size = 100
	model = Sequential()
	model = load_model('sample.h5')
	nonPotholeTestImages = glob.glob("Dataset/test/Plain/*.jpg")
	test2 = [cv2.imread(img,0) for img in nonPotholeTestImages]
# train2[train2 != np.array(None)]
	for i in range(0,len(test2)):
		test2[i] = cv2.resize(test2[i],(size,size))
	temp4 = np.asarray(test2)


## load Testing data : potholes
	potholeTestImages = glob.glob("Dataset/test/Pothole/*.jpg")
	test1 = [cv2.imread(img,0) for img in potholeTestImages]
# train2[train2 != np.array(None)]
	for i in range(0,len(test1)):
		test1[i] = cv2.resize(test1[i],(size,size))
	temp3 = np.asarray(test1)



	X_test = []
	X_test.extend(temp3)
	X_test.extend(temp4)
	X_test = np.asarray(X_test)

	X_test = X_test.reshape(X_test.shape[0], size, size, 1)
	y_test1 = np.ones([temp3.shape[0]],dtype = int)
	y_test2 = np.zeros([temp4.shape[0]],dtype = int)
	y_test = []
	y_test.extend(y_test1)
	y_test.extend(y_test2)
	y_test = np.asarray(y_test)


	correct=0;
	tests = model.predict_classes(X_test)
	for i in range(0,50):
		docname=str(i)
		if tests[i]==1:
			g = geocoder.ip('me')
			answer=g.latlng
			doc_ref = db.collection(u'Potholes').document(docname)
			doc_ref.set({
				u'Lat,Lang': answer
			})
		time.sleep(15)






if __name__ == "__main__":
    start()













