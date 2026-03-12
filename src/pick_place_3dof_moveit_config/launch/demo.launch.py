from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("pick_place_3dof", package_name="pick_place_3dof_moveit_config")
        .to_moveit_configs()
    )

    # Use generate_demo_launch but override rviz with our fixed version
    ld = generate_demo_launch(moveit_config)

    return ld
