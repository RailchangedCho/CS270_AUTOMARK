# https://kagus2.tistory.com/28

from keras.models import load_model
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def getanswer():
    model = load_model('mnist_fin.h5')
    answer_array = []
    for i in range(1, 7):
        # img = Image.open("img.png")
        img = cv2.imread('answer/' + str(i) + '_ans.png')
        plt.figure(figsize=(15, 12))
        # print("img")

        img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_blur=cv2.GaussianBlur(img_gray, (5,5), 0)

        ret, img_th = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY_INV)
        contours, hierachy = cv2.findContours(img_th.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        rects = [cv2.boundingRect(each) for each in contours]

        rects = sorted(rects)

        for rect in rects:
            # print(rect)
            cv2.circle(img_blur, (rect[0], rect[1]), 10, (0, 0, 255), -1)
            cv2.circle(img_blur, (rect[0]+rect[2], rect[1]+rect[3]), 10, (0, 0, 255), -1)
            cv2.rectangle(img_blur, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (0, 255, 0), 3)

        #cv2_imshow(img_blur)
        img_for_class = img_blur.copy()

        mnist_imgs = []
        margin_pixel = 15

        for rect in rects:
            #print(rect)
            im = img_for_class[rect[1]-margin_pixel:rect[1]+rect[3]+margin_pixel, rect[0]-margin_pixel:rect[0]+rect[2]+margin_pixel]
            row, col = im.shape[:2]

            bordersize = max(row, col)
            diff = min(row, col)

            bottom = im[row-2:row, 0:col]
            mean = cv2.mean(bottom)[0]

            border = cv2.copyMakeBorder(
                im,
                top=0,
                bottom=0,
                left=int((bordersize-diff)/2),
                right=int((bordersize-diff)/2),
                borderType=cv2.BORDER_CONSTANT,
                value=[mean, mean, mean]
            )

            square = border
            #cv2_imshow(square)

            resized_img=cv2.resize(square, dsize=(28, 28), interpolation=cv2.INTER_AREA)
            mnist_imgs.append(resized_img)
            #cv2_imshow(resized_img)

        result_string = ""
        for i in range(len(mnist_imgs)):

            img = mnist_imgs[i]
            #cv2_imshow(img)

            img=img.reshape(-1, 28, 28, 1)

            input_data = ((np.array(img)/255) - 1) * -1
            input_data

            res = np.argmax(model.predict(input_data), axis=-1)
            result_string += str(res)[1]
            #print(res)

        #print(result_string)
        answer_array.append(str(result_string))

    print("-- your answer --")
    print(answer_array)
    return answer_array