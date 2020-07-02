#%% import dependencies 
import cv2, mtm, os
from MTM import matchTemplates, drawBoxesOnRGB
from skimage.data import coins
import matplotlib.pyplot as plt

#%% 

template_dir = "ellipse_templates/"
image_gray = cv2.imread("imgg2.png", 0)

plt.imshow(image_gray, cmap="gray")

#%%
# list_ = []

# for i in os.listdir(template_dir):
#     template = cv2.imread(template_dir+i, 0)
#     list_.append((str(i), template))

# match = matchTemplates(list_, image_gray, score_threshold=0.60, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
# print("Found {} Ellipses".format( len(match.index) ) )
# match

# image = cv2.imread("imgg5.png")
# Overlay = drawBoxesOnRGB(image, match, showLabel=False)
# plt.imshow(Overlay)
# %%

def match_image_template(image, template_dir, thresh):
    list_ = []

    for i in os.listdir(template_dir):
        template = cv2.imread(template_dir+i, 0)
        list_.append((str(i), template))

    match = matchTemplates(list_, image, score_threshold=thresh/100, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
    print("Found {} Ellipses".format( len(match.index) ) )
    return match

match_image_template(image_gray, template_dir, 20)

# %%

