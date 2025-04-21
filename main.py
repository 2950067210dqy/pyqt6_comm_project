from loguru import logger

# Author: Qinyou Deng
# Create Time:2025-04-17
# Update Time:2025-04-17
from communication.communication_root import communication_root
from enu.enviroment import enviroment


def receive_serial_port_data():
    """
    接收串口数据
    :return:无
    """

    communication_root_obj = communication_root()
    logger.info("start serial port communication!")
    communication_root_obj.start()
def set_envir():
    """
    设置环境变量'HOST_COMPUTER_DATA_STORAGE_LOC' 上位机通讯数据存储文件地址
    :return:
    """
    envir = enviroment()
    envir.set_envir()
if __name__ == '__main__':
    # 加载日志配置
    logger.add(
        "./log/COM_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="30 days",
        enqueue=True,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} : {module}:{line} | {message}"
    )
    logger.info(f"{'-' * 30}start{'-' * 30}")

    # 设置环境变量
    set_envir()
    # 接收串口数据
    receive_serial_port_data()




