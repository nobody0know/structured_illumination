from pypylon import pylon
import image_undistort as iu
img = pylon.PylonImage()
tlf = pylon.TlFactory.GetInstance()
cam = pylon.InstantCamera(tlf.CreateFirstDevice())
def camera_init():
    r"""打开相机并初始化参数"""
    cam.Open()
    cam.ExposureTime = 8000#设置曝光时间
    cam.Gain = 0#设置增益
    cam.CenterX.SetValue(True)#设置图像中心点为中心
    cam.CenterY.SetValue(True)
    cam.StartGrabbing()
    return
def camera_capture(num_img):
    r"""#num_img为要拍摄图片的序号"""
    result = cam.RetrieveResult(2000)
    iu.undistort_image(result,num_img)
    img.AttachGrabResultBuffer(result)
    ipo = pylon.ImagePersistenceOptions()
    ipo.SetQuality(100)
    filename = 'saved_pypylon_img_' + num_img + '.jpeg'
    img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
    img.Release()
    return True

def camera_off():
    r"""关闭相机"""
    cam.StopGrabbing()
    cam.Close()
    return
