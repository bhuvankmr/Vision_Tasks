#!/usr/bin/env python3

import rospy
import subprocess

if __name__ == '__main__':
    rospy.init_node('lab1_launch', anonymous=True)

    package_name = 'lab1_pkg'
    talker_node = 'talker.py'
    relay_node = 'relay.py'

    rospy.set_param('v', 5)
    rospy.set_param('d', 3)
    
    talker_process = subprocess.Popen(['rosrun', package_name, talker_node])

    relay_process = subprocess.Popen(['rosrun', package_name, relay_node])

    rospy.loginfo("Nodes launched.")

    talker_process.wait()
    relay_process.wait()