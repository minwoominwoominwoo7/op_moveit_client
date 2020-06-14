#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
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


    # Get information
    planning_frame = move_group.get_planning_frame()
    eef_link = move_group.get_end_effector_link()
    group_names = robot.get_group_names()
    current_state = robot.get_current_state()
    
    # Get end effect pose
    cur_pose = move_group.get_current_pose().pose
    quaternion = (
        cur_pose.orientation.x,
        cur_pose.orientation.y,
        cur_pose.orientation.z,
        cur_pose.orientation.w)
    angles = euler_from_quaternion(quaternion)    
    
    # Get tolerance 
    joint_tolerance = move_group.get_goal_joint_tolerance()
    orientation_tolerance = move_group.get_goal_orientation_tolerance()
    position_tolerance = move_group.get_goal_position_tolerance()
    goal_tolerance = move_group.get_goal_tolerance()

    # Get end joint value
    cur_joint = move_group.get_current_joint_values()

    print "============ Planning frame: %s" % planning_frame
    print "============ End effector link: %s" % eef_link                    
    print "============ Available Planning Groups:", robot.get_group_names()
    print('============ End effector position x {0} y {1} z {2} roll {3} pitch {4} yaw {5}'\
            .format(round(cur_pose.position.x,3), round(cur_pose.position.y,3), round(cur_pose.position.z,3)\
                    ,round(angles[0],3), round(angles[1],3), round(angles[2],3) ))  
    print('============ joint position joint0 {0} join1 {1} joint2 {2} joint3 {3}'\
            .format( round(cur_joint[0],3), round(cur_joint[0],3), round(cur_joint[0],3), round(cur_joint[0],3) ))  
    print "============ Tolerance joint {0} orientation {1} potision {2} goal {3}" \
        .format(joint_tolerance, orientation_tolerance ,  position_tolerance, goal_tolerance )
    print "============ Printing robot state"
    print current_state
    print "="*20

    quit()
