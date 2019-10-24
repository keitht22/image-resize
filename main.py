import os
import cv2


def main():

    # creates directory for formatted images to be sent to
    # this option is more favorable than overwriting the images
    try:
        if not os.path.isfile('/Users/tylerkeith/Documents/Research/Destination for Formatted'):
            makeDestDir()
            imageResize()
    except FileExistsError:
        imageResize()


def makeDestDir():

    directory = "Destination for Formatted"
    path = "/Users/tylerkeith/Documents/Research"
    fullpath = os.path.join(path, directory)
    os.mkdir(fullpath)


def imageResize():

    # changes the working directory to the copied version
    # of our gathered data sets
    dirlist = os.listdir('Data Sets for Testing copy 2')

    # iterates over each .png or .jpg image file in the directory
    for c, file in enumerate(dirlist):
        if ('.png' in str(file)) or ('.jpg' in str(file)):
            # we split original file names at the understore in order to isolate
            # the observed number of clusters for comparison with our machine's prediction
            tokens = file.split('_')
            clustnum = int(tokens[1].split(".")[0])
            filect = str(c) + '_' + str(clustnum)
            print(clustnum)
            pic = 'Data Sets for Testing copy' + os.path.sep + file
            imgread = cv2.imread(pic)

            # the creation of our resized images
            # and the movement of said images to our destination directory
            img = cv2.resize(imgread, (500, 500))
            cv2.imwrite('/Users/tylerkeith/Documents/Research/Destination for Formatted/' + filect + '.jpg', img)


if __name__ == '__main__':
    main()
