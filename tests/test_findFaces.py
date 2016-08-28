__author__ = 'davidruffner'

import cv2
import peopleDetector.detector as detector
from unittest import TestCase

class TestFindFace(TestCase):
    """
    Tests of the findFace function.
    """
    def test_webcam(self):
        """
        Tests ability of findFace on a webcam video feed. This test displays the video
        with boxes around any faces that are found.

        Based on the blog post by Shantnu Tiwari.
        https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/

        :return:
        """
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            print "frameShape", frame.shape

            frameSmall = frame[::2, ::-2]

            gray = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2GRAY)

            # Find faces
            faces = detector.findFaces(gray)

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                print
                print x, y, w, h
                print frameSmall.shape
                print gray.shape
                print
                topCorner = (min(360, x+w), min(640, y+h))
                cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

