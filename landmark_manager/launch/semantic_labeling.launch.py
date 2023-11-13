from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package = "tf2_ros", 
            executable = "static_transform_publisher",
            arguments = ["--x", "0.35", "--y", "-0.27", "--z", "0", "--yaw", "0.2618", "--pitch", "0.3142", "--roll", "0", "--frame-id", "base_camera", "--child-frame-id", "camera_link"]
        ),

        Node(
            package='landmark_manager',
            executable='semantic_labeling',
            name='semantic_labeling'
        )
    ])