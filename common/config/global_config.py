import configparser, os


class GlobalConfig:
    def __init__(self, file_name):
        self.file_name = file_name

    def find_file(self):
        """
        현재 디렉토리 및 부모 디렉토리에서 ini 파일 찾기.
        """
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)

        while current_dir != parent_dir:
            file_path = os.path.join(current_dir, self.file_name)
            if os.path.exists(file_path):
                return file_path
            current_dir = parent_dir
            parent_dir = os.path.dirname(current_dir)

        # 파일을 찾지 못한 경우 None 반환
        return None

    def read_config(self):
        """
        ini 파일을 읽어서 딕셔너리로 반환.
        """
        file_path = self.find_file()
        if file_path:
            config = configparser.ConfigParser()
            config.read(file_path)
            config_dict = {section: dict(config.items(section)) for section in config.sections()}
            return config_dict
        else:
            raise FileNotFoundError(f"Config file '{self.file_name}' not found.")