#!/usr/bin/env python3

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from geometry_msgs.msg import Twist, Pose, PoseStamped
from sensor_msgs.msg import LaserScan

## the aim of ros tcp endpoint is to coneect ROS with Unity part and accept messages 
def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'Server')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 10000000)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)
    
    tcp_server.start({
        # Subscribe to the (cmd_vel) topic to aquire (geometry_msgs/Twist) messages to control the robot
        'cmd_vel': RosSubscriber('cmd_vel', Twist, tcp_server),
        # Publish to the (laser_scan) topic to provide (sensor_msgs/LaserScan) messages to generate the map on ROS side
        'laser_scan': RosPublisher('laser_scan', LaserScan, queue_size = 100000),
        # Publish to the (odometry_frame) topic to provide (geometry_msgs/Pose) messages to provide the odometry of the robot
        'odometry_frame': RosPublisher('odometry_frame', Pose, queue_size = 100000),
        # Publish to the (move_base_simple/goal) topic to provide (geometry_msgs/PoseStamped) messages to provide the location of the goal
        'move_base_simple/goal': RosPublisher('move_base_simple/goal', PoseStamped, queue_size = 1)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
