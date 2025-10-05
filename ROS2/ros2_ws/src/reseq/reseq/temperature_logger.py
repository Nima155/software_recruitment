import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the TemperatureLogger node

class TemperatureLogger(Node):
    def __init__(self, fileName):
    	super().__init__("temperature_subscriber")
    	self.subscription = self.create_subscription(Float32, "/temperature", self.callback, 10)
    	self.fileName = fileName
    def callback(self, temperature):
        if temperature.data > 50.0: 
        	with open(self.fileName, "a+") as file:
            		file.write(f"recording temperature: {temperature}")



def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
