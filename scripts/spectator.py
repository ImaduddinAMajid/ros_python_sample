#!/usr/bin/env python
'''Simple ROS Python script to continually subscribe a message to the
`microphone` topic'''

import rospy
from std_msgs.msg import String

def spectator():
    '''Initialize spectator node and the subscriber'''
    rospy.init_node('spectator', anonymous=True)
    rospy.Subscriber('microphone', String, confirmation)
    rospy.spin()

def confirmation(message):
    '''Show the received message'''
    rospy.loginfo("This message is received from %s:\n%s" \
    , rospy.get_caller_id(), message.data)

if __name__ == '__main__':
    spectator()
