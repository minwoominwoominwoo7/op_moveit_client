#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


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


    # Move using joint space
    joint_goal = move_group.get_current_joint_values()
    print joint_goal

    '''joint_goal[0] = 0
    joint_goal[1] = -pi/2
    joint_goal[2] = pi/2
    joint_goal[3] = 0
    joint_goal[4] = pi/2
    joint_goal[5] = 0'''
    joint_goal[0] = 0
    joint_goal[1] = -1.000
    joint_goal[2] = 0.300
    joint_goal[3] = 0.700


    move_group.go(joint_goal, wait=True)
    move_group.stop()

    current_joints = move_group.get_current_joint_values()
    print current_joints

    quit()