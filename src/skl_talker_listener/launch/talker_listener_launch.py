from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    talker_node = Node(
        package='skl_talker_listener',
        executable='talker',
        name='skl_talker',
        output='screen',
    )

    listener_node = Node(
        package='skl_talker_listener',
        executable='listener',
        name='skl_listener',
        output='screen',
    )

    return LaunchDescription([
        talker_node,
        listener_node,
    ])