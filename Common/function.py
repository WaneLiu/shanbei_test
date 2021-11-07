import os
import yaml


def project_path():
    """
    返回项目的系统路径
    :return:
    """
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]


def config_url():
    """
    返回public_config.yml里面配置的所有url
    :return:
    """
    with open(os.path.join(project_path(), 'public_config.yml')) as f:
        return yaml.safe_load(f)['urls']


if __name__ == "__main__":
    print(f"项目的系统路径为{project_path()}")
    print(f"项目配置了的urls: {config_url()}")
    print(os.path.join(project_path(), 'Logs/'))
