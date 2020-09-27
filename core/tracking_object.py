
from collections import deque
import numpy as np

class TrackingObject(deque):
    def __init__(self, 
                 index=None,
                 turning_frame_index=None, ):
        self.index = index
        self.turning_frame_index = turning_frame_index
