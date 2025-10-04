import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nima155/software_recruitment/ROS2/ros2_ws/src/reseq/install/reseq'
