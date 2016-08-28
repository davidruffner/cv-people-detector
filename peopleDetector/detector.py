import cv2

cascPath = '../resources/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


def findFaces(image):
    """
    Finds faces in an image using a cascade classifier.

    Based on blog post by Shantnu Tiwari
    https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

    :param image: openCV image
        Image to be analyzed
    :return faces: list of tuples
        Coordinates of the squares enclosing the detected faces
    """

    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    return faces
