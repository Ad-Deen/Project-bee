from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Define paths
    urdf_path = PathJoinSubstitution([
        FindPackageShare('bee'), 'urdf', 'bee.urdf'
    ])
    rviz_config = PathJoinSubstitution([
        FindPackageShare('bee'), 'rviz', 'urdf.rviz'
    ])

    # Declare arguments
    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_gui',
            default_value='true',
            description='Use joint_state_publisher_gui'),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            condition=LaunchConfiguration('use_gui')
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': PathJoinSubstitution([
                FindPackageShare('bee'), 'urdf', 'bee.urdf'
            ])}]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        ),
    ])
