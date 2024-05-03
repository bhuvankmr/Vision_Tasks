#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    pub = rospy.Publisher('drive', AckermannDriveStamped, queue_size=10)
    rospy.init_node("talker")
    while not rospy.is_shutdown():
        v = rospy.get_param("v")
        d = rospy.get_param("d")
        ack_msg  = AckermannDriveStamped()
        ack_msg.drive.speed = v
        ack_msg.drive.steering_angle = d
        pub.publish(ack_msg)
        rospy.loginfo(ack_msg)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

