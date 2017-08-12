#!/usr/bin/env python
'''Simple ROS Python script to continually publish a message to the
`microphone` topic'''

import time
import rospy
from std_msgs.msg import String

def announcer():
    '''Initialize announcer node and publish to `microphone` topic'''
    rospy.init_node('announcer', anonymous=True)
    mic = rospy.Publisher('microphone', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_time))
        message = "Hi Imad. {0}".format(format_time)
        mic.publish(message)
        rospy.loginfo(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        announcer()
    except rospy.ROSInterruptException:
        pass
