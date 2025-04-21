from enum import Enum

from loguru import logger

from communication.communication_com import communication
from communication.communication_com import store_data
from communication.ini_pareser.ini_parser import ini_parser
from communication.util.folder_util import folder_util
class Comm_Methods(Enum):
    COM = "COM"
    UDP = "UDP"
    TCP = "TCP"
class communication_root():
    """
    这是用来串口通讯的入口类
    """
    config_file_path = "./communicate_config.ini"

    def __init__(self,method="COM"):
        """
            类实例化函数
            :param
            :return 无返回值
        """
        # 串口配置
        self.config_parser = ini_parser(self.config_file_path)
        # 串口配置数据{"section":{"key1":value1,"key2":value2,....}，...}
        self.config = self.config_parser.read()
        if (len(self.config) != 0):
            logger.info("communication_root通讯配置文件读取成功。")
        else:
            logger.error("communication_root通讯配置文件读取失败。")
            return


        # 通讯方式有udp tcp com
        self.comm_method = str(self.config['Method']['communication'])
        # 通讯方式为COM串口通讯
        match self.comm_method:
            case Comm_Methods.COM.value:
                # 创建存储文件夹
                folder_path = str(self.config['Storage']['fold_path'])+str(self.config['Serial']['receive_port'])+"/"
                folder_util.create_folder(folder_path)
                self.com_init(save_pre_path=folder_path)
            case Comm_Methods.UDP.value:
                # 创建存储文件夹
                folder_path = str(self.config['Storage']['fold_path']) + str(self.config['UDP']['host']) + "/"
                folder_util.create_folder(folder_path)
                # 通讯方式为UDP通讯
                self.udp_init(save_pre_path=folder_path)
            case Comm_Methods.TCP.value:
                # 创建存储文件夹
                folder_path = str(self.config['Storage']['fold_path']) + str(self.config['TCP']['host']) + "/"
                folder_util.create_folder(folder_path)
                # 通讯方式为TCP串口通讯
                self.tcp_init(save_pre_path=folder_path)
            case _:
                # 通讯方式有误
                logger.error(f"通讯方式配置{self.comm_method}有误！,应为下列一种{[method for method in Comm_Methods]}")
                return
        pass
    def com_init(self,save_pre_path=""):
        """
        串口通讯初始化
        :return:
        """
        self.communication_thread_receive = communication(category="receive", config_file_path=self.config_file_path)
        self.communication_thread_send = communication(category="send", config_file_path=self.config_file_path)
        self.store_data_thread = store_data(config_file_path=self.config_file_path,save_pre_path=save_pre_path)
    def udp_init(self,save_pre_path=""):
        """
        udp通讯初始化
        :return:
        """
    def tcp_init(self,save_pre_path=""):
        """
        tcp通讯初始化
        :return:
        """
    def start(self):
        """
        串口线程通讯开始
        :return:
        """
        match self.comm_method:
            case Comm_Methods.COM.value:
                # 通讯方式为COM串口通讯
                self.com_start()
            case Comm_Methods.UDP.value:
                # 通讯方式为UDP通讯
                self.udp_start()
            case Comm_Methods.TCP.value:
                # 通讯方式为TCP串口通讯
                self.tcp_start()
            case _:
                # 通讯方式有误
                logger.error(f"通讯方式配置{self.comm_method}有误！,应为下列一种{[method  for method in Comm_Methods]}")
                return
        pass

    def com_start(self):
        """
        串口通讯开始
        :return:
        """
        self.communication_thread_receive.start()
        self.communication_thread_send.start()
        self.store_data_thread.start()
    def udp_start(self):
        """
        udp通讯开始
        :return:
        """
        pass
    def tcp_start(self):
        """
        tcp通讯开始
        :return:
        """
        pass
    def test(self):
        """
        tcp通讯开始
        :return:
        """
        pass
    pass
