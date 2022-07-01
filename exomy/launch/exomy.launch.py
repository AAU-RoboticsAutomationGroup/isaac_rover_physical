import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression

namespace_ = 'exomy'

def generate_launch_description():
    use_joy = DeclareLaunchArgument(
        'use_joy_control',
        default_value='False'
    )
    
    camera = Node(
        package='exomy',
        executable='Camera_node',
        name='Camera_node',
        namespace=namespace_,
        output='screen'
    )

    joy = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        namespace=namespace_,
        output='screen'
    )
    gamepad = Node(
        package='exomy',
        executable='gamepad_parser_node',
        name='gamepad_parser_node',
        namespace=namespace_,
        output='screen'
    )
    kinematics = Node(
        package='exomy',
        executable='Kinematics_node',
        name='Kinematics_node',
        namespace=namespace_,
        output='screen'
    )
    motors = Node(
        package='exomy',
        executable='motor_node',
        name='motor_node',
        namespace=namespace_,
        output='screen'
    )
    model = Node(
        package='exomy',
        executable='RLModel_node',
        name='RLModel_node',
        namespace=namespace_,
        output='screen'
    )
    
    return LaunchDescription([
        camera,
        #joy,
        #gamepad,  
        kinematics,
        motors,
        model
    ])
