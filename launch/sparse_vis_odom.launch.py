#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        # Launch vid_publisher node
        # Node(
        #     package='bee',
        #     executable='vid_publisher',
        #     name='vid_publisher',
        #     output='screen'
        # ),

        Node(
            package='bee',
            executable='cam1',
            name='cam1',
            output='screen'
        ),

        # Launch cam_filter node
        Node(
            package='bee',
            executable='cam_filter',
            name='cam_filter',
            output='screen'
        ),

        # Launch point cloud generator node
        Node(
            package='bee',
            executable='pcd_generator',
            name='pcd_generator',
            output='screen'
        ),

        # Launch feature accumulator node
        # Node(
        #     package='bee',
        #     executable='accumulator',
        #     name='accumulator',
        #     output='screen'
        # ),

        # Launch odometry node
        # Node(
        #     package='bee',
        #     executable='odometry',
        #     name='odometry',
        #     output='screen'
        # ),

        # Launch feature accumulator node
        # Node(
        #     package='bee',
        #     executable='aligner_3D',
        #     name='aligner_3D',
        #     output='screen'
        # ),

        # Launch RViz2 with a config (optional)
        ExecuteProcess(
            cmd=['rviz2', '-d', '/home/deen/ros2_ws/src/bee/rviz/sparse_odom.rviz'],
            output='screen'
        ),
    ])
