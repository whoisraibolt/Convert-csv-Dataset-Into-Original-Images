#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import cv2
import numpy as np
import os
import sys

def main():
	# Message Error
    if len(sys.argv) < 2:
        print '\nUsage: python convert-csv.py [output_path]\n'

    return -1

    output_path = sys.argv[1]

    if os.path.exists(output_path):
        os.system('rm -rf {}'.format(output_path))

    os.system('mkdir {}'.format(output_path))

    # Labels names 
    label_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # Importing dataset with np.genfromtxt()
    data = np.genfromtxt('FER-2013.csv', delimiter=',', dtype=None)

    labels = data[1:,0].astype(np.int32)

    image_buffer = data[1:,1]

    images = np.array([np.fromstring(image, np.uint8, sep=' ') for image in image_buffer])

    usage = data[1:,2]

    dataset = zip(labels, images, usage)

    for i, d in enumerate(dataset):
        usage_path = os.path.join(output_path, d[-1])
        label_path = os.path.join(usage_path, label_names[d[0]])

        # We know that the size of the images of the FER-2013 are 48x48
        img = d[1].reshape((48, 48))

        image_name = '%08d.jpg' % i

        image_path = os.path.join(label_path, image_name)

        if not os.path.exists(usage_path):
            os.system('mkdir {}'.format(usage_path))

        if not os.path.exists(label_path):
            os.system('mkdir {}'.format(label_path))

        cv2.imwrite(image_path, img)
        print 'Write {}'.format(image_path)

if __name__ == '__main__': main()