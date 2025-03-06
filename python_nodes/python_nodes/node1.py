import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8
from random import randint

class node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher = self.create_publisher(Int8, 'numbers', 10)
        time_period = 2
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.i = randint(0,9)

    def timer_callback(self):
        msg = Int8()
        msg.data = self.i
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.i = randint(0,9)

def main(args=None):
    rclpy.init(args=args)
    node = node1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()