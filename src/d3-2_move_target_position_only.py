#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from tf.transformations import *


if __name__ == "__main__":
    # Initialize moveit_commander and node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('d1_get_basic_info', anonymous=False)

    # Get instance from moveit_commander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Get group_commander from MoveGroupCommander
    group_name = "arm"
    #group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)


    # Move using target_pose
    x = 0.194
    y = 0.100 - 0.1
    z = 0.303 + 0.1

    test = [ x, y , z]
    move_group.set_position_target(test)


    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    quit()