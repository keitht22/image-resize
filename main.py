import os
import cv2


def main():

    # creates directory for formatted images to be sent to
    # this option is more favorable than overwriting the images
    try:
        if not os.path.isfile('/path/for/new/directory/name-of-directory-to-create'):
            makeDestDir()
            imageResize()
    except FileExistsError:
        imageResize()


def makeDestDir():

    directory = "name-of-directory-to-create"
    path = "/path/for/new/directory"
    fullpath = os.path.join(path, directory)
    os.mkdir(fullpath)


def imageResize():

    # changes the working directory to the copied version
    # of our gathered data sets
    dirlist = os.listdir('directory-with-images-to-resize')

    # iterates over each .png or .jpg image file in the directory
    for c, file in enumerate(dirlist):
        if ('.png' in file) or ('.jpg' in file):
            img = 'directory-with-images-to-resize' + os.path.sep + file
            imgread = cv2.imread(img)
            height, width = imgread.shape[0], imgread.shape[1]

            # the creation of our resized images
            # and the movement of said images to our destination directory
            new_img = cv2.resize(imgread, (500, 500))
            cv2.imwrite('/path/for/new/directory/name-of-directory-to-create' + str(c) + '.png', new_img)


if __name__ == '__main__':
    main()
