##신경망-신호전달 연습
#import numpy as np

#def init_network():
#    db_network = {}
#    db_network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
#    db_network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
#    db_network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
#    db_network['b1'] = np.array([0.1,0.2,0.3])
#    db_network['b2'] = np.array([0.1,0.2])
#    db_network['b3'] = np.array([0.1,0.2])

#    return db_network

#def forward(db_network, x):
#    W1,W2,W3 = db_network['W1'],db_network['W2'],db_network['W3']
#    b1,b2,b3 = db_network['b1'],db_network['b2'],db_network['b3']

#    a1 = np.dot(x, W1) + b1
#    z1 = sigmoid(a1)
#    a2 = np.dot(z1, W2) + b2
#    z2 = sigmoid(a2)
#    a2 = np.dot(z2, W3) + b3
#    y = identity_function(a3)

#    return y

#db_network = init_network()
#x = np.array([1.0,0.5])
#y = forward(db_network, x)
#print(y)


#흑백전환
#import numpy as np
#import matplotlib.pyplot as plt
#import PIL.Image as pimg

#img_main = pimg.open('example_img_v2.jpg')

##이미지 데이터 --Convert--> numpy array
#pix_main = np.array(img_main)
#pix_main = (1/255) * pix_main           #색 관련 보정
#pix_size = np.array(pix_main.shape)
#pix_sub = np.empty(pix_size)

##회색 비율(일부 조정가능, R 0.2126 G 0.7152 B 0.0722)
#for i in range(pix_size[0]):
#    for j in range(pix_size[1]):
#        pix_gray = 0.2126 * pix_main[i][j][0] + 0.7152 * pix_main[i][j][1] + 0.0722 * pix_main[i][j][2]
#        pix_sub[i, j] = (pix_gray, pix_gray, pix_gray)

#plt.subplot(141)       
#plt.imshow(pix_sub)  
#plt.axis('off')         
#plt.title('Convert to gray', fontsize = 7)

#plt.show()


##이미지 합성
#import numpy as np
#import matplotlib.pyplot as plt
#import PIL.Image as pimg

#img_bg = pimg.open('example_bg_v1.jpg')
#img_c1 = pimg.open('example_character_v1.jpg')
#img_c2 = pimg.open('example_character_v2.jpg')

##변경할 크기 계산
#pix_bg = np.array(img_bg)
#resizeX2 = pix_bg.shape[1] / 2
#if(pix_bg.shape[1] % 2 > 0):
#    resizeX1 = pix_bg.shape[1] / 2 + 1
#else:
#    resizeX1 = pix_bg.shape[1] / 2

##사진 나란히 나열시키기 위해 크기 변경
#img_c1 = img_c1.resize((int(resizeX1), int(pix_bg.shape[0])))
#pix_c1 = np.array(img_c1)
#img_c2 = img_c2.resize((int(resizeX2), int(pix_bg.shape[0])))
#pix_c2 = np.array(img_c2)

##사진을 가로 방향으로 나란히 붙이기
#pix_cA = np.concatenate((pix_c1, pix_c2), axis = 1)
#pix_bg = (1 / 255) * pix_bg
#pix_cA = (1 / 255) * pix_cA

##가중치 설정 및 사진 합성
#value_weight = 0.3
#pix_show = pix_bg * value_weight + pix_cA * (1 - value_weight)
#pix_rshow = pix_bg * (1 - value_weight) + pix_cA * value_weight

#plt.subplot(141)        #그래프 표기용 / 상대위치
#plt.imshow(pix_show)    #보여줄 이미지
#plt.axis('off')         
#plt.title('Blended', fontsize = 10)
#plt.subplot(142)       
#plt.imshow(pix_rshow)  
#plt.axis('off')         
#plt.title('Blended Reverse', fontsize = 10)

#plt.show()


'''
#turtle 이용해 이미지 그리기
import turtle as tt
import numpy as np

img_v1 = np.array([[0,0,0,0,0,0,0,0],
                   [0,1,1,1,0,0,0,0],
                   [1,1,1,1,1,0,0,0],
                   [1,1,1,1,1,0,0,0],
                   [0,1,1,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0]])

size_pixel = 10

def putPixel(x,y,pSize,pCol):
    tt.penup()                              #펜 기능 비활성화
    tt.goto(x*pSize,(-1)*y*pSize)           #좌표이동
    tt.pendown()                            #펜 활성화
    tt.begin_fill()                         #다각형 내부 채우기
    tt.fillcolor(pCol)                      #다각형 채움색
    tt.setheading(45)                       #시작각도
    tt.circle(pSize/2, steps=4)             #픽셀 도출
    tt.end_fill()                           #끝내기

for row in range(0,8):
    for col in range(0,8):
        if(img_v1[row][col] > 0):
            putPixel(col, row, size_pixel, 'orange')
        else:
            putPixel(col, row, size_pixel, 'blue') 
'''

##이미지 색 변조
#import numpy as np
#import matplotlib.pyplot as plt
#import PIL.Image as pimg

#file_img = pimg.open('example_img_v1.jpg')
#data_pixel = np.array(file_img)
#size_pixel = np.array(data_pixel.shape)
#print(size_pixel)

##R(0) / G(1) / B(2)
##해당 성분값 이외는 0으로 만듬
##RGB에 해당하는 배열 만들기
#pixel_R = data_pixel.copy()
#pixel_R[:,:,(1,2)] = 0
#pixel_G = data_pixel.copy()
#pixel_G[:,:,(0,2)] = 0
#pixel_B = data_pixel.copy()
#pixel_B[:,:,(0,1)] = 0

##원본
#plt.subplot(141)        #그래프 표기용
#plt.imshow(data_pixel)  #보여줄 이미지
#plt.axis('off')         
#plt.title('RGB')        #제목
##R채널
#plt.subplot(142)
#plt.imshow(pixel_R)
#plt.axis('off')
#plt.title('RED')
##G채널
#plt.subplot(143)
#plt.imshow(pixel_G)
#plt.axis('off')
#plt.title('GREEN')
##B채널
#plt.subplot(144)
#plt.imshow(pixel_B)
#plt.axis('off')
#plt.title('BLUE')

#plt.show()

