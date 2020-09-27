
from core.tracking_object import TrackingObject

def findOldTracking(cnts_0,
        cnts_1,
        tracking_objects,
        config):
    tracking_index_list = list(tracking_objects.keys())
    for tracking_index in tracking_index_list:
        if tracking_index in tracking_objects:
            tracking_object = tracking_objects[tracking_index]
        else:
            continue
        cnt = tracking_object[0]
        for cnt_0 in cnts_0:
            if cnt_0.isNearby(cnt):
                cnt.addChild(cnt_0)
def findNewTracking(cnts_0,
        cnts_1,
        tracking_objects,
        config):
    i_track = 0
    time_str = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(cnts_1[0].time))
    tracking_index_pre = '{}-{}'.format(time_str,
             cnts_1[0].frame_index)
    for cnt in cnts_1:
        if cnt.tracking_index is not None:
            continue
        for cnt_0 in cnts_0:
            if cnt.tracking_index is not None:
                break
            if cnt_0.isNearby(cnt):
                tracking_index = (tracking_index_pre, i_track)
                cnt.tracking_index = tracking_index
                cnt.tracking_object = TrackingObject
                cnt.tracking_object.appendleft(cnt)
                cnt.addChild(cnt_0)
                tracking_objects[tracking_index] = cnt.tracking_object
def tracking(cnts_0,
        cnts_1,
        tracking_objects,
        config):
    findOldTracking(cnts_0,
            cnts_1,
            tracking_objects,
            config)
    findNewTracking(cnts_0,
            cnts_1,
            tracking_objects,
            config)
