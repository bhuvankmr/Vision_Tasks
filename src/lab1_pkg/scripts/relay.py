#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def callback(data):
    data.drive.speed = 3 * data.drive.speed
    data.drive.steering_angle = 3 * data.drive.steering_angle
    pub.publish(data)
    rospy.loginfo(data)

def relay():
    rospy.init_node("relay")
    try : 
        rospy.Subscriber("drive", AckermannDriveStamped, callback)
    except rospy.ROSInterruptException:
        pass
    rospy.spin()

if __name__ == '__main__':
    try:
        pub = rospy.Publisher("drive_relay", AckermannDriveStamped, queue_size=10)
        relay()
    except rospy.ROSInterruptException:
        pass