# turtlebot3_manipulation] Moveit API Applicaiotn Python      

https://cafe.naver.com/openrt/23657   

# System   
Ubuntu 18.04 , melodic 

## Install   

1. turtlebot3 install and change melodic version      
https://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/#install-dependent-ros-1-packages    

2. open manipulator install and change melodic version       
https://emanual.robotis.com/docs/en/platform/openmanipulator_x/ros_setup/#install-ros-packages    

3. turtlebot3 manipulator install and change melodic version       
https://emanual.robotis.com/docs/en/platform/turtlebot3/manipulation/#software-setup    

4. sudo apt-get install ros-melodic-trac-ik-kinematics-plugin     

5. git download and build       
git clone https://github.com/minwoominwoominwoo7/op_moveit_client   
cd ~/catkin_ws && catkin_make    

## run [Gazebo]   
roscore   
roslaunch turtlebot3_manipulation_gazebo turtlebot3_manipulation_gazebo.launch  
roslaunch turtlebot3_manipulation_moveit_config move_group.launch  
roslaunch turtlebot3_manipulation_moveit_config moveit_rviz.launch  
roslaunch turtlebot3_manipulation_gui turtlebot3_manipulation_gui.launch   

## demo
1. get information demo  
rosrun op_moveit_client d1_get_basic_info.py

2. joint control motion planning   
rosrun op_moveit_client d2_move_joint_space.py

3. end effect target pose motion planning   
rosrun op_moveit_client d3-1_move_target_position_only.py
rosrun op_moveit_client d3-2_move_target_pose.py

4. cartesian demo 
rosrun op_moveit_client d4_move_cartesian_path.py   

[![Video Label](http://img.youtube.com/vi/jIu7RaQzyOc/0.jpg)](https://youtu.be/jIu7RaQzyOc?t=0s)   

5. add box and scene demo   
rosrun op_moveit_client d5-1_add_box.py

[![Video Label](http://img.youtube.com/vi/OQXUlKhSl-g/0.jpg)](https://youtu.be/OQXUlKhSl-g?t=0s)   

6. constraint demo  
rosrun op_moveit_client d6_move_target_pose_w_constraint.py
