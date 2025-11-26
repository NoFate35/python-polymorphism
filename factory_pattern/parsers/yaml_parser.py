import yaml


class YAMLParser:
    # BEGIN (write your solution here)
    def get_data(raw_data):
        return yaml.safe_load(raw_data)
# END
