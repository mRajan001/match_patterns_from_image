#%% import dependencies 
import cv2, mtm, os
from MTM import matchTemplates, drawBoxesOnRGB
from skimage.data import coins
import matplotlib.pyplot as plt

#%% select a template directory
template_dir = "ellipse_templates/"

image_gray = cv2.imread("imgg2.png", 0) #load image in a graysale

plt.imshow(image_gray, cmap="gray") #plot the image

# %% A function to match the templates with the image

def match_image_template(image, template_dir, thresh):
    """
    A function to match the templates with the image.
    Input: 
    image: Image from which needs to find patterns
    template_dir: A directory containing (cropped) template images
    thresh: Score Threshold Value. 

    Output: matched patterns in pandas dataframe
    BBox, Score, templateName

    """

    list_ = []

    for i in os.listdir(template_dir):
        template = cv2.imread(template_dir+i, 0)
        list_.append((str(i), template))

    match = matchTemplates(list_, image, score_threshold=thresh/100, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
    print("Found {} Ellipses".format( len(match.index) ) )
    return match

matches = match_image_template(image_gray, template_dir, 20)

# %% 
image = cv2.imread("imgg2.png", )

draw_matches = drawBoxesOnRGB(image, matches,boxColor=(0, 255, 0), showLabel=False)
plt.imshow(draw_matches)
