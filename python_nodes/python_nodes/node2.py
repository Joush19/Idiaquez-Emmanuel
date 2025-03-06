import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8

class node2(Node):
    def __init__(self):
        super().__init__('node2')
        self.subscription = self.create_subscription(Int8, 'numbers', self.listener_callback, 10)
        self.sum = 0
        self.subscription

    def listener_callback(self,msg):
        self.sum = self.sum + msg.data
        self.get_logger().info(f'Sum: {self.sum}')

def main(args=None):
    rclpy.init(args=args)
    node = node2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
