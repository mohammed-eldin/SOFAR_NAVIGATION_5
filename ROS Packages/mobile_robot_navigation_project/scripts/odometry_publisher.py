#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


def publish_odom_frame(msg):

    # we can use TF broadcasting to define and establish the relationship between
    # two different coordinate frames,odom and base_link, and build the relationship
    # tree of the coordinate frames in the system.

    # First step, we have to first define the which is “parent” and “child” because
    # TF defines the “forward transform” as transforming from parent to child."""
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    # name of parent frame
    # Odom: World-fixed coordinate frame(The pose is continuous)
    t.header.frame_id = "odom"
    # name of child frame
    # Base_link: Rigidly attached to the mobile robot base.
    t.child_frame_id = "base_link"

    t.transform.translation.x = msg.position.x
    t.transform.translation.y = msg.position.y
    t.transform.translation.z = msg.position.z
    
    t.transform.rotation.x = msg.orientation.x
    t.transform.rotation.y = msg.orientation.y
    t.transform.rotation.z = msg.orientation.z
    t.transform.rotation.w = msg.orientation.w
    # Forward transform between the two frames
    br.sendTransform(t)
    
    
if __name__ == '__main__':
    # Initialization the publisher node
    rospy.init_node('odometry_frame_publisher')
    # Subscribe to the (odometry_frame) topic to acquire (geometry_msgs/Pose) messages
    # which would be used for conversion to (tf/tfMessages) that used in gmapping and navigation stack
    rospy.Subscriber('odometry_frame', geometry_msgs.msg.Pose, publish_odom_frame)
    rospy.spin()


"""odom (nav_msgs/Odometry)
   dometry information that gives the local planner the current speed of the robot.
   The velocity information in this message is assumed to be in the same coordinate 
   frame as the robot_base_frame of the costmap contained within the TrajectoryPlannerROS object.
   See the costmap_2d package for information about the robot_base_frame parameter."""
