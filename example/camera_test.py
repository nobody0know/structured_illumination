from pypylon import pylon
import cv2 as cv
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

# demonstrate some feature access
camera.Width.SetValue(800)
camera.Hight.SetValue(600)
numberOfImagesToGrab = 100
camera.StartGrabbingMax(numberOfImagesToGrab)

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data.
        print("SizeX: ", grabResult.Width)
        print("SizeY: ", grabResult.Height)
        img = grabResult.Array
        cv.imshow('image',img)
        cv.waitKey(10)
        print("Gray value of first pixel: ", img[0, 0])

    grabResult.Release()
camera.Close()