import os
import argparse
import random
from data import Data
import cv2
import time
import sys
from tqdm import tqdm
from bounding_box import bounding_box as bb
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-r","--root_dir", type=str, default="/mnt/069A453E9A452B8D/Ram/surveillance-data/sdd_train")
parser.add_argument("-t","--type", type=str, default="train", help="train|val|trainval|test")
parser.add_argument("--random_seed", type=int, default=100)
parser.add_argument("--save_images", type=bool, default=True)
parser.add_argument("-s","--save_dir", type=str, default="output")
parser.add_argument("-l","--line_thickness", type=int, default=2)
args = parser.parse_args()
random.seed(args.random_seed)

img_dir = os.path.join(args.root_dir, 'JPEGImages')
ann_dir = os.path.join(args.root_dir, 'Annotations')
set_dir = os.path.join(args.root_dir, 'ImageSets', 'Main')

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def get_image_list(dir, filename):
    image_list = open(os.path.join(dir, filename)).readlines()
    return [image_name.strip() for image_name in image_list]


def process_image(image_data):
    image = cv2.imread(image_data.image_path)

    image = cv2.putText(image, image_data.image_name, (5, 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    color_list = ["maroon", "green", "yellow", "purple", "fuchsia", "lime", "red", "silver"]
    for ann in image_data.annotations:
        id_color = random.randint(0, 7)
        box_color = color_list[id_color]

        bb.add(image, ann.xmin, ann.ymin, ann.xmax, ann.ymax, ann.name, box_color)
        #image = cv2.rectangle(image, (ann.xmin, ann.ymin), (ann.xmax, ann.ymax), box_color, args.line_thickness)
        #image = cv2.putText(image, ann.name, (ann.xmin, ann.ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    return image


def main(args):
    image_list = get_image_list(set_dir, args.type + ".txt")
    total_images = len(image_list)

    #for index in progressbar(range(total_images), "Computing: ", 40):
    for index in tqdm(range(total_images)):
        time.sleep(0.1)
        image_data = Data(args.root_dir, image_list[index])
        image = process_image(image_data)
        if args.save_images:
            cv2.imwrite(os.path.join(args.save_dir, image_list[index] + ".jpg"), image)



if __name__ == '__main__':
    main(args)
