import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8

class calcule(Node):
    def __init__(self):
        super().__init__('calculator')
        self.subscriber1 = self.create_subscription(Int8, 'odd', self.odd_callback, 10)
        self.subscriber2 = self.create_subscription(Int8, 'even', self.even_callback, 10)
        self.odd = 0
        self.result = 0
        self.subscriber1
        self.subscriber2

    def odd_callback(self, odd_msg):
        self.odd = odd_msg.data**2

    def even_callback(self, even_msg):
        self.result = self.odd + (even_msg.data**2)
        self.get_logger().info(f'The sum of squares is: {self.result}')
        self.result = 0

def main(args=None):
    rclpy.init(args=args)
    node = calcule()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
