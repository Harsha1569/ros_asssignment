#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing the packages and modules for turtlesim simulation
import math
import time
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# initialization of global variables

TURTLE_X = 0.0
TURTLE_Y = 0.0
TURTLE_THETA = 0
PREVIOUS_ANGLE = 0
DISTANCE = 0

# defining subscriber callback function

def pose_callback(pose):
    global TURTLE_X, TURTLE_Y, TURTLE_THETA
    TURTLE_X = pose.x
    TURTLE_Y = pose.y
    TURTLE_THETA = pose.theta


# function for the turtle simulation

def move_turtle():
    global TURTLE_X, TURTLE_Y, DISTANCE, TURTLE_THETA, PREVIOUS_ANGLE

    # initializing node
    rospy.init_node('node_turtle_revolve', anonymous=True)

    # initailizing publisher....
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # initializing subscriber....
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    rate = rospy.Rate(100)  # Rate = 10Hz
    vel = Twist()  # Assigning publisher
    distance = 0
    t=time.time()
    while not rospy.is_shutdown():

        # linear velocities
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0

        # angular velocities
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.8


        # calling publisher........
        pub.publish(vel)

        rate.sleep()
        radius=vel.linear.x/vel.angular.z
        distance = vel.linear.x*(time.time()-t)
        rospy.loginfo("The distance travelled by turtlebot: %.4f",distance)
        rospy.loginfo("The time taken by turtlebot: %.4f",time.time()-t)
        if((2*math.pi*radius)/vel.linear.x<time.time()-t):
        	break

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
