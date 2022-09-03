from validate import validate_resize_config
from validate import is_valid_directory

from multiprocess import perform_multiprocessing
from process_files import get_files_list

from resize import _resize

from rich.pretty import pprint

def convert_images():
    return "Images Converted"


# def print_files(path:str , is_recersive:bool = False):
#     files = glob.glob(f"{path}/*")
#     return files


def resize_command(config: dict) -> list[bool]:
    # Checks
    valid_config = validate_resize_config(config)
    status_list = None
    if valid_config["status"] == "config_ok":
        files_list = get_files_list(config["source_directory"], config["process"])
        # pprint(files_list)
        # pprint(valid_config)
        config["function"] = _resize
        status_list = perform_multiprocessing(config, files_list)
    else:
        print(f"{valid_config['status']}")

    return status_list
