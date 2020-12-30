import sys, os
sys.path.append(os.pardir)
from mnist import load_mnist
import numpy as np
import pickle
import matplotlib.pyplot as plt

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)


##사전에 제공된 가중치로 머신러닝 정확도 구하기
#import sys, os
#sys.path.append(os.pardir)
#from mnist import load_mnist
#import numpy as np
#import pickle
#import matplotlib.pyplot as plt

#def get_data():
#    #normalize: 이미지의 픽셀 값을 0.0~1.0 사이의 값으로 정규화할지?
#    #one_hot_label : 레이블을 원-핫(one-hot) 배열로 반환할지?
#    #flatten : 입력 이미지를 1차원 배열로 만들지?
#    (x_train, t_train), (x_test, t_test) = \
#        load_mnist(normalize=True, flatten=True, one_hot_label=False)
    
#    return x_test, t_test

#def init_network():
#    with open("sample_weight.pkl", 'rb') as f:          #사전 정의 가중치
#        network = pickle.load(f)                    

#    return network

#def predict(network, x):
#    W1, W2, W3 = network['W1'], network['W2'], network['W3']
#    b1, b2, b3 = network['b1'], network['b2'], network['b3']

#    a1 = np.dot(x, W1) + b1
#    z1 = sigmoid(a1)
#    a2 = np.dot(z1, W2) + b2
#    z2 = sigmoid(a2)
#    a3 = np.dot(z2, W3) + b3
#    y = softmax(a3)

#    return y


##계산 함수 - 시그모이드, 소프트맥스
#def sigmoid(x):
#    return 1 / (1 +np.exp(-x))
#def softmax(x):
#    val_c = np.max(x)
#    val_exp = np.exp(x - val_c)
#    sum_exp = np.sum(val_exp)
#    y = val_exp / sum_exp

#    return y

#x, t = get_data()
#network = init_network() 
#batch_size = 100                                   #배치 사이즈   
#accuracy_cnt = 0

#for i in range(0, len(x), batch_size):
#    x_batch = x[i:i+batch_size]
#    y_batch = predict(network, x_batch)           #레이블 확률 계산
#    p = np.argmax(y_batch, axis=1)                #배치의 각 리스트에서 가장 높은 값의 원소 인덱스 저장
#    accuracy_cnt += np.sum(p==t[i:i+batch_size])  #정답 카운트

#print("Accuracy: " + str(float(accuracy_cnt) / len(x)))