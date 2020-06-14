#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from tf.transformations import *
from moveit_msgs.msg import RobotState, Constraints, JointConstraint


if __name__ == "__main__":
    # Initialize moveit_commander and node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('d1_get_basic_info', anonymous=False)

    # Get instance from moveit_commander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Get group_commander from MoveGroupCommander
    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)


    # Move using target_pose with constraint
    contraints = Constraints()

    contraints.name = "constraints1"

    jc1 = JointConstraint()
    jc1.joint_name = "joint2"
    jc1.position = 0.0
    jc1.tolerance_above = 0.01
    jc1.tolerance_below = 0.01

    contraints.joint_constraints.append(jc1)
    move_group.set_path_constraints(contraints)


    # Move using target_pose
    x = 0.185
    y = 0
    z = 0.365

    test = [ x, y , z]
    move_group.set_position_target(test)

    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    move_group.set_path_constraints(None)

    quit()