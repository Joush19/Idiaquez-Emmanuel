import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8

class odd(Node):
    def __init__(self):
        super().__init__('odd_node')
        self.publisher = self.create_publisher(Int8, 'odd', 10)
        time_period = 2
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        msg = Int8()
        msg.data = self.i
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing odd number: {msg.data}')
        self.i = self.i+2

def main(args=None):
    rclpy.init(args=args)
    node = odd()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()