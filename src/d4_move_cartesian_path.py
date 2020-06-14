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
from tf.transformations import *

def calcurator_op_orientation(position) :
    orientation = geometry_msgs.msg.Quaternion()

    #yaw = math.atan2(pose_goal.position.y, pose_goal.position.x + 0.092 )
    yaw = math.atan2(pose_goal.position.y, pose_goal.position.x + 0.08 )
    quat = quaternion_from_euler( 0 , 0 , yaw) 

    orientation.x = quat[0]
    orientation.y = quat[1]
    orientation.z = quat[2]
    orientation.w = quat[3]

    return orientation

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

    # Create a `DisplayTrajectory`_ ROS publisher
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                    moveit_msgs.msg.DisplayTrajectory,
                                                    queue_size=20)


    # First move robot to point.
    print "============ Go Target Point"
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = 0.194
    pose_goal.position.y = 0.100
    pose_goal.position.z = 0.303
    pose_goal.orientation = calcurator_op_orientation(pose_goal.position)

    move_group.set_goal_orientation_tolerance(1)
    move_group.set_pose_target(pose_goal)

    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()


    # Move using cartesian path
    waypoints = []
    wpose = pose_goal

    wpose.position.y -= 0.1       
    wpose.orientation = calcurator_op_orientation(wpose.position)
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.z += 0.1
    wpose.orientation = calcurator_op_orientation(wpose.position)
    waypoints.append(copy.deepcopy(wpose))   

    wpose.position.y += 0.1
    wpose.orientation = calcurator_op_orientation(wpose.position)
    waypoints.append(copy.deepcopy(wpose))       

    wpose.position.z -= 0.1
    wpose.orientation = calcurator_op_orientation(wpose.position) 
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)
    print "============ Start Cartersian fraction %f " %fraction

    # For debugging
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    display_trajectory_publisher.publish(display_trajectory)

    # Move!
    move_group.execute(plan, wait=True)

    quit()