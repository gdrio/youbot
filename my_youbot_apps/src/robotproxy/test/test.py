#!/usr/bin/env python

import robotproxy

if __name__ == "__main__":
    print "Running unit tests"
    print "Joint position definition test +++++++++++++++++"
    robotproxy.test_joint_pose_defs()
    print "Command list test +++++++++++++++++"
    robotproxy.test_commands_list()
    print "Youbot Gazebo load config files +++++++++++++++++"
    robotproxy.test_load_control_plan()
    #print "Youbot Gazebo proxy test load +++++++++++++++++"
    #robotproxy.test_youbot_gazebo_proxy_move()
    print "Youbot Gazebo proxy test exec +++++++++++++++++"
    robotproxy.test_youbot_gazebo_proxy_exec()    
    print "Done +++++++++++++++++"
    robotproxy.moveit_commander.os._exit(0)

