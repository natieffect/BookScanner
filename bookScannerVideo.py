import cv2
import imutils
from PIL import Image
from imutils.video import VideoStream

class VideoStreamFrame:
    def __init__(self, videosource=0) -> None:
        self.width = None
        self.height= None
        self.source = videosource
        self.videoSource = VideoStream(src=videosource).start()
     
#   imutils video reader initialized   
    def initializeImutilsRead(self):
        try:
            _,frame   = self.readCaptureImage()
            self.width,self.height = frame.shape[:2]
            return True
        except Exception as e:
            print(e)
            return False
    
#   streame  camera read frame     
    def readCaptureImage(self):
        try:
            frame = self.videoSource.read()
            return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),frame
        except Exception as e:
            print(e)
            return None, None
    
#   imutils resize the image frames
    def imutilsMatchSize(self,frame):
        return imutils.resize(frame, width =self.camera_width, height=self.camera_height)
    
#   resize the frame with dimention
    def resizeFrame(self,frame,dimention=(100,100)):
        return cv2.resize(frame, dimention, interpolation=cv2.INTER_AREA)
    
    def __del__(self):
        self.videoSource.stop()
        cv2.destroyAllWindows()
        
#   change frame to png file 
    def imageCapture(self,frame):
        return cv2.imencode(".png",frame)[1].tobytes()
    
# change image to pdf file 
    def changeImageToPdf(self,imageFrame,nameOfPDF):
        imageFrameHolder = []
        for frame in imageFrame:
             frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
             imPil = Image.fromarray(frame)
             imPil = imPil.convert('RGB')
             imageFrameHolder.append(imPil)
        imageFrameHolder[0].save(f"{nameOfPDF}",save_all=True,append_images=imageFrameHolder[1:])
        
#   change the brigtness of the frame
    def fastBrightness(self,inputImage,brightness):
        imageCopy = inputImage.copy()
        return cv2.convertScaleAbs(imageCopy,imageCopy,1,brightness)
    
 #  blur the images   
    def blurImage(self,image,ksize=(-1,-1)):
        return cv2.blur(image,ksize)
        