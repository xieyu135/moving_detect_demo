
import cv2

def calcCntCenter(cnt_val):
    M = cv2.moments(cnt_val)   
    center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
    return center
class Contour(object):
    def __init__(self,
            values=None, 
            frame_index=None, 
            frame=None, 
            time=None, 
            config={}):
        self.values = values
        self.frame_index = frame_index
        self.time = time
        self.config = config
        self.prepare()
    def prepare(self):
        self.tracking_index = None
        self.tracking_object = None
        if self.values is not None:
            self.center = calcCntCenter(self.values)
            self.box = cv2.boundingRect(self.values)
            self.area = cv2.contourArea(self.values)
        else:
            self.center = None
            self.box = None
            self.area = None
    @property
    def center_x(self):
        if self.center is None:
            return None
        else:
            return self.center[0]
    @property
    def center_y(self):
        if self.center is None:
            return None
        else:
            return self.center[1]
    def __sub__(self, other):
        if not isinstance(other, Contour):
            print('{} is not a Contour'.format(other.__name__))
        if self.center is None:
            print('{}.center is None'.format(self.__name__)
        if other.center is None:
            print('{}.center is None'.format(other.__name__)
        dist = ((self.center_x-other.center_x)**2
                + (self.center_y-other.center_y)**2)**0.5
        return dist
    def isNearby(self, other):
        if abs(self-other)<self.config['dist_thre']:
            return True
        else:
            return False
    def rmChild(self, tracking_objects):
        tracking_objects.popleft()
        self.child_node.parent_node = None
        self.child_node.tracking_index = None
        self.child_node = None
    def rmParent(self, tracking_objects):
        tracking_objects.popleft()
        if len(tracking_objects)==1:
            del tracking_objects
            self.parent_node.tracking_index = None
        self.parent_node.child_node = None
        self.tracking_index = None
        self.parent_node = None
    def addChild(self, other):
        self.tracking_object.appendleft(other)
        self.justAddChild(other)
    def justAddChild(self, other):
        other.tracking_index = self.tracking_index
        self.child_node = other
        other.parent_node = self
