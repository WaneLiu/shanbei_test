import logging, time
import os.path
from logging import handlers
from Common.function import project_path


class FrameLog:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', max_byte_each_log=1024, backupCount=3):
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = os.path.join(project_path(), 'Logs/')
        self.log_name = self.log_path + self.log_time + 'log.log'
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations[level])
        formatter = logging.Formatter(
            "[%(asctime)s]  %(filename)s -> %(funcName)s line: %(lineno)d [%(levelname)s] %(message)s")
        # 前台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt=formatter)
        sh.setLevel(self.level_relations['warning'])
        self.logger.addHandler(sh)
        # 输入到文件的日志
        rfh = handlers.RotatingFileHandler(self.log_name, 'a', max_byte_each_log, backupCount, encoding='utf-8')
        rfh.setFormatter(fmt=formatter)
        rfh.setLevel(self.level_relations[level])
        self.logger.addHandler(rfh)

    def log(self):
        return self.logger


if __name__ == "__main__":
    log = FrameLog(__file__, level='debug', max_byte_each_log=1024, backupCount=3)
    log = log.log()
    for i in range(10):
        log.error("error")
        log.debug("debug")
        log.info("info")
        log.critical("critical")
        log.warning("warning")
