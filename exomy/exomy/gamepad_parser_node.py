#!/usr/bin/env python
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from exomy_msgs.msg import Actions
import math



class GamepadParserNode(Node):
    def __init__(self):
        self.node_name = 'gamepad_parser_node'
        super().__init__(self.node_name)

        self.sub = self.create_subscription(
            Joy,
            'joy',
            self.callback,
            10)

        self.pub = self.create_publisher(
            Actions,
            'Actions',
            1)

        self.motors_enabled = True

        self.get_logger().info('\t{} STARTED.'.format(self.node_name.upper()))

    def callback(self, data):

        rover_cmd = Actions()

        # Function map for the Logitech F710 joystick
        # Button on pad | function
        # --------------|----------------------
        # Left Stick    | Control speed and direction
        # START Button  | Enable and disable motors

        # Reading out joystick data
        y = data.axes[4]
        x = data.axes[0]


        # Enable and disable motors
        # START Button
        if (data.buttons[9] == 1):
            if self.motors_enabled is True:
                self.motors_enabled = False
                self.get_logger().info("Motors disabled!")
            elif self.motors_enabled is False:
                self.motors_enabled = True
                self.get_logger().info("Motors enabled!")
            else:
                self.get_logger().error(
                    "Exceptional value for [motors_enabled] \
                    = {}".format(self.motors_enabled))
                self.motors_enabled = False

        # The velocity is decoded as value between -1...1
        rover_cmd.lin_vel = y
        rover_cmd.ang_vel = x
        

        self.pub.publish(rover_cmd)


def main(args=None):
    rclpy.init(args=args)

    try:
        gamepad_parser_node = GamepadParserNode()
        try:
            rclpy.spin(gamepad_parser_node)
        finally:
            gamepad_parser_node.destroy_node()
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
