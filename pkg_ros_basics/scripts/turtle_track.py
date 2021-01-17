#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing the packages and modules for turtlesim simulation
import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from pkg_ros_basics.msg import command

# initialization of global variables

TURTLE_X = 0.0
TURTLE_Y = 0.0
TURTLE_THETA = 0
PREVIOUS_ANGLE = 0
DISTANCE = 0
COMMAND = 5

# defining subscriber callback function

def pose_callback(pose):
    global TURTLE_X, TURTLE_Y, TURTLE_THETA
    TURTLE_X = pose.x
    TURTLE_Y = pose.y
    TURTLE_THETA = pose.theta

def command_callback(msg):
    global COMMAND
    COMMAND = msg.command

# function for the turtle simulation

def move_turtle():
    global TURTLE_X, TURTLE_Y, DISTANCE, TURTLE_THETA, PREVIOUS_ANGLE, COMMAND

    # initializing node
    rospy.init_node('node_turtle_revolve', anonymous=True)

    # initailizing publisher....
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # initializing subscriber....
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    rospy.Subscriber('my_command', command, command_callback)

    rate = rospy.Rate(0.7)  # Rate = 10Hz
    rate1 = rospy.Rate(0.7)
    vel = Twist()  # Assigning publisher
    #count = 0
    flag = 0
    while not rospy.is_shutdown():

        if COMMAND == 0:
            flag = 0

        if COMMAND == 1:
            flag = 1

        while flag == 0:
            if COMMAND == 1:
                break
            rate1.sleep()


        while COMMAND == 3 and flag == 1:
            # linear velocities
            vel.linear.x = 1
            vel.linear.y = 0
            vel.linear.z = 0

            # angular velocities
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = 0


            # calling publisher........
            pub.publish(vel)

            rate1.sleep()

        while COMMAND == 2 and flag == 1:
            # linear velocities
            vel.linear.x = 0
            vel.linear.y = 0
            vel.linear.z = 0

            # angular velocities
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = 0.8


            # calling publisher........
            pub.publish(vel)

            rate1.sleep()

        while COMMAND == 4 and flag == 1:
            # linear velocities
            vel.linear.x = 0
            vel.linear.y = 0
            vel.linear.z = 0

            # angular velocities
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = -0.8


            # calling publisher........
            pub.publish(vel)

            rate1.sleep()

        rospy.loginfo(flag)        


        rate.sleep()    

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass