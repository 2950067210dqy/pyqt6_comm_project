from loguru import logger

# Author: Qinyou Deng
# Create Time:2025-04-17
# Update Time:2025-04-17
from communication.communication_root import communication_root


def receive_serial_port_data():
    """
    接收串口数据
    :return:无
    """
    communication_root_obj = communication_root()
    logger.info("start serial port communication!")
    communication_root_obj.start()
if __name__ == '__main__':
    # 加载日志配置
    logger.add(
        "COM_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="30 days",
        enqueue=True,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} : {module}:{line} | {message}"
    )
    logger.info(f"{'-' * 30}start{'-' * 30}")
    # 接收串口数据
    receive_serial_port_data()


