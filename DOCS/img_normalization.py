import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np
# import tensorflow as tf

def normalize(img_path):
    # 상대경로 수정필요 
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())
    
    image = '../../../datasets/images/' + img_path 
    img2 = mpimg.imread(image)
    means = img2.mean(axis=(0,1,2))
    means.shape

    # -n ~ 0 ~ n : standard normal distribution
    # result = (img2-img2.mean(axis=(0,1,2),keepdims=True))/np.std(img2,axis=(0,1,2),keepdims=True)
    # plt.imshow(result)

    # tensorflow function (standard normal distribution)
    # df = tf.image.per_image_standardization(img2)

    # 0 ~ 1 : normalize
    result = (img2 - np.min(img2)) / (np.max(img2) - np.min(img2))
    print(result)
    
    plt.imshow(result)
    plt.show()
    return result

normalize('36979.jpg')