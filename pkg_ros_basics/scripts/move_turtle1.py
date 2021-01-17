#!/usr/bin/python

import rospy
from rospy.exceptions import ROSInterruptException
from geometry_msgs.msg import Twist

PI = 3.140
def circle_logic():
    linear_velocity = 1.0
    radius= 1.0
    angular_velocity= linear_velocity/radius
    frequency= 100

rospy.init_node("node_circle_publisher")
publisher= rospy.Publisher("/turtle/cmd_vel",Twist,quese_size = 10)

message=Twist()
message.linear.x = linear_velocity
message.angular.z= angular_velocity

rate = rospy.Rate(frequency)
distance_travelled = 0
target_distance = 2*PI*radius

while not rospy.is_shutdown() and distance_travelled < target_distance:-

message.linear.x= 0
message.angular.z=0
publisher.publisher(message)

rospy.loginfo("goal reached..")


if _name="main_":
    try: circle_logic()
    except ROSInterruptException: pass