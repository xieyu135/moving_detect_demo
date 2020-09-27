#!/usr/bin/env python3

import os
import sys
import json
import cv2
import numpy as np
from collections import deque
#import argparse
import time
import datetime
import imutils
from core.run_seq_one_frame import runSeqOneFrame


class Detect():
    '''
    detect-object main class
    '''
    def __init__(self, config):
        self.config = config
    def prepare(self, camera):
        self.config['fps'] = camera.get(cv2.CAP_PROP_FPS)
        self.config['log_file'] = open(self.config['log_file_path'])
    def release(self):
        self.config['log_file'].close()
        self.camera.release()
    def getFrame(self):
        ret, frame_color = self.camera.read()
        if not ret:
            return None
        if ('flag_resize' in self.config 
        and self.config['flag_resize']
        and 'frame_width_resize' in self.config
        ):
            frame_color = imutils.resize(frame_color, 
                    width=self.config['frame_width_resize'])
        return frame_color
    def runSeqOneFrame(self,
            i_current_frame,
            frame,
            bg_gray_frame,
            cnts,
            tracking_objects):
        runSeqOneFrame(i_current_frame,
                frame,
                bg_gray_frame,
                cnts,
                tracking_objects, 
                self.config)
        return tracking_objects
    def rmDisappear(self, tracking_objects):
        pass
        return tracking_objects, disappeared_tracking_objects
    def saveAndSendAlarm(tracking_objects):
        pass
    def runSeqFrames(self, getFrame):
        bg_color_frame = getFrame()
        frame_height, frame_width = bg_color_frame.shape[:2]
        gray_frame = cv2.cvtColor(bg_color_frame, cv2.COLOR_BGR2GRAY)
        bg_gray_frame = gray_frame
        cnts = []
        tracking_objects = {}
        i_current_frame = 0
        while True:
            i_current_frame += 1
            frame = getFrame()
            if frame is None:
                break
            tracking_objects = self.runSeqOneFrame(i_current_frame,
                    frame,
                    bg_gray_frame,
                    cnts,
                    tracking_objects)
            tracking_objects, disappeared_tracking_objects = \
                    self.rmDisappear(tracking_objects)
            bg_color_frame = self.updateBgFrame(bg_color_frame, frame)
            self.gcCollect()
        if len(self.tracking_objects['down'])>0:
            self.saveAndSendAlarm(tracking_objects)
    def run(self):
        self.camera = cv2.VideoCapture(self.config['camera_name'])
        self.prepare(self.camera)
        self.runSeqFrames(self.getFrame)
        self.release()
def run():
    t0 = time.time()
    config = json.load(open('config.json', 'r'))
    td = ThrowDetect(config)
    td.run()
    t1 = time.time()
    print('Time consumed:', t1-t0)
if __name__ == '__main__':
    run()
