
import os
import time
import cv2
from core.contour import Contour
from core.tracking import tracking

def saveFrame(i_current_frame, frame, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    fig_path = os.path.join(save_dir, str(i_current_frame)+'.jpg')
    cv2.imwrite(fig_path, frame)
def refineCnts(cnts):
    pass
    return cnts
def runSeqOneFrame(i_current_frame, 
        frame, 
        bg_gray_frame, 
        cnts, 
        tracking_objects, 
        config):
    current_time = time.time()
    cnts_1 = cnts
    cnts_0 = []
    cnts_vals, diff_frame = bgObjectDetect(frame, bg_gray_frame, config)
    if config['flag_debug']>=2:
        saveFrame(i_current_frame, 
                diff_frame, 
                os.path.join(config['save_log_dir'], 'diff_pics'))
        saveFrame(i_current_frame, 
                frame, 
                os.path.join(config['save_log_dir'], 'origin_pics'))
    for cnt_val in cnts_vals:
        cnt = Contour(values=cnt_val, 
                frame_index=i_current_frame, 
                frame=frame, 
                time=current_time, 
                config)
        cnts_0_raw.append(cnt)
    cnts_0 = refineCnts(cnts_0_raw)
    tracking_objects = tracking(cnts_0,
            cnts_1,
            tracking_objects,
            config)