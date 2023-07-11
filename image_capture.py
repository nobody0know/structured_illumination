from pypylon import pylon
import platform

num_img_to_save = 8
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
def camera_init():
    cam.Open()
    cam.ExposureTime = 8000#设置曝光时间
    cam.Gain = 0#设置增益
    cam.CenterX.SetValue(True)#设置图像中心点为中心
    cam.CenterY.SetValue(True)
    cam.StartGrabbing()
    return

for i in range(num_img_to_save):
    with cam.RetrieveResult(20000) as result:

        # Calling AttachGrabResultBuffer creates another reference to the
        # grab result buffer. This prevents the buffer's reuse for grabbing.
        img.AttachGrabResultBuffer(result)

        # The JPEG format that is used here supports adjusting the image
        # quality (100 -> best quality, 0 -> poor quality).
        ipo = pylon.ImagePersistenceOptions()
        ipo.SetQuality(100)
        filename = "saved_pypylon_img_%d.jpeg"
        img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
        img.Release()

cam.StopGrabbing()
cam.Close()
