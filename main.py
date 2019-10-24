import os
import cv2


def main():

    # creates directory for formatted images to be sent to
    # this option is more favorable than overwriting the images
    try:
        if not os.path.isfile('path/to/directory/folder-to-save-in'):
            makeDestDir()
            imageResize()
    except FileExistsError:
        imageResize()


def makeDestDir():

    directory = "folder-to-save-in"
    path = "/path/to/directory"
    fullpath = os.path.join(path, directory)
    os.mkdir(fullpath)


def imageResize():

    # changes the working directory to the copied version
    # of our gathered data sets
    dirlist = os.listdir('folder with images')

    # iterates over each .png or .jpg image file in the directory
    for c, file in enumerate(dirlist):
        if ('.png' in str(file)) or ('.jpg' in str(file)):
            # we split original file names at the understore in order to isolate
            # the observed number of clusters for comparison with our machine's prediction
            tokens = file.split('_')
            clustnum = int(tokens[1].split(".")[0])
            filect = str(c) + '_' + str(clustnum)
            pic = 'folder with images' + os.path.sep + file
            imgread = cv2.imread(pic)

            # the creation of our resized images
            # and the movement of said images to our destination directory
            img = cv2.resize(imgread, (500, 500))
            cv2.imwrite('/path/to/directory/folder-to-save-in' + filect + '.jpg', img)


if __name__ == '__main__':
    main()
    return True
