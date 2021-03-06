import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy import signal


def pre_proccess(im_path):
    imcv = cv.imread(im_path)

    tmp_img = np.array(cv.resize(imcv, (512, 536)))

    tmp_img = tmp_img[:, 12:-12, :]
    tmp_img = np.rot90(tmp_img)

    # switch channels to make RGB
    img = np.zeros(tmp_img.shape)
    img[:, :, 0] = tmp_img[:, :, 2]
    img[:, :, 2] = tmp_img[:, :, 0]
    img[:, :, 1] = tmp_img[:, :, 1]

    # make it 0<=>1 insted of 0<=>255: brightest = 1, darkest = 0
    img = img / 255

    return img

def find_sweemerts(img, verbus=False):
    im_hight = img.shape[0]
    im_width = img.shape[1]
    # show image
    if verbus:
        plt.imshow(img)
        plt.suptitle('FirstImg')
        plt.show()

    # ## correlation

    # get red channel
    im_red = img[:,:,0]
    # normelize channel: mean=avarange
    im_red_norm = np.abs(im_red - im_red.mean())
    # correlation
    template = np.ones((im_red_norm.shape[1],1))
    cor_im = signal.correlate2d(im_red_norm, template, boundary='symm', mode='same')
    if verbus:
        plt.imshow(cor_im)
        plt.suptitle('CorImg')
        plt.show()


    # ## find line locations

    # middle hight of the picture
    cor_middle = cor_im[im_hight//2,:]
    #  find maximum peaks: distance between peaks
    line_locs, _ = signal.find_peaks(cor_middle, distance=60) #, threshold=None, prominence=None, width=None, wlen=None, rel_height=0.5, plateau_size=None)
    # show red 'x' in maximums
    if verbus:
        plt.plot(line_locs, cor_middle[line_locs], "rx")


    # ## sweemers width locs

    sweemers_width = []
    for i in range(1,len(line_locs)):
        loc = (line_locs[i]+line_locs[i-1])/2
        sweemers_width.append(int(np.round(loc)))
    print(sweemers_width)


    # ## sweemers hight locs

    # set sweemers hight array
    sweemers_hight = np.zeros(len(sweemers_width),np.integer)
    # loop sweemers each at any 'i'
    for i in range(len(sweemers_width)):
    #     get sweemer line from image
        sweemer_line = im_red_norm[:,sweemers_width[i]]
    #     loop points in the line: where the sweemer start?
        for j in range(len(sweemer_line)):
    #         check minimum value of the sweemer
            if sweemer_line[j] > 0.2:
                sweemers_hight[i] = j
                break
    #   just show graphs
        if verbus:
            plt.plot(sweemer_line)
            plt.plot(sweemers_hight[i], sweemer_line[sweemers_hight[i]], "rx")
            plt.suptitle('PlaceOnGrafh')
            plt.show()

    # ## plot result on picture
    print(sweemers_hight)
    box_size = 6
    im_result = img
    for i in range(len(sweemers_width)):
        im_result[sweemers_hight[i]-box_size//2:sweemers_hight[i]+box_size//2, sweemers_width[i]-box_size//2:sweemers_width[i]+box_size//2,:] = 0

    plt.imshow(im_result)
    plt.suptitle('Result')
    plt.show()

