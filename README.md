# `skl_talker_listener` (`skl_ws`) — ROS 2 Jazzy

A ROS 2 Jazzy (`ament_python`) package in workspace `skl_ws` demonstrating a publisher (`talker`), subscriber (`listener`), and a launch file (`talker_listener_launch.py`).

## Nodes & Architecture

- **`talker` (Publisher Node — `skl_talker_listener/talker.py`)**: Creates a publisher on the `/chatter` topic and publishes incrementing string messages once per second using a ROS 2 timer.
- **`listener` (Subscriber Node — `skl_talker_listener/listener.py`)**: Subscribes to the `/chatter` topic and logs every received message to the console.
- **Launch File (`launch/talker_listener_launch.py`)**: Starts both `talker` (as `skl_talker`) and `listener` (as `skl_listener`) together with screen output logging.

## Topic & Message Type

- **Topic Name**: `/chatter`
- **Message Type**: `std_msgs/msg/String`

## Build the Workspace

```bash
source /opt/ros/jazzy/setup.bash
cd ~/skl_ws
colcon build --symlink-install
source install/setup.bash
