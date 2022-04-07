#!/usr/bin/env python2

import rospy
import time

from geometry_msgs.msg import PoseStamped

def callback(msg):
    x_pos = msg.pose.position.x
    y_pos = msg.pose.position.y
    z_pos = msg.pose.position.z

    print("x_pos = {:.2f}".format(x_pos))
    print("y_pos = {:.2f}".format(y_pos))
    print("z_pos = {:.2f}\n".format(z_pos))
    time.sleep(2)


def listener():

    pos_subscriber = rospy.Subscriber("/nav/pose", PoseStamped, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)  
    listener()
