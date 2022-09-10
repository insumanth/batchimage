from multiprocess import perform_multiprocessing
from process_files import get_files_list

from rich.pretty import pprint

from resize import _resize, validate_resize_config
from annotate import _annotate, validate_annotate_config
from timestamp import _timestamp, validate_timestamp_config

process_dict = {
    "annotate": _annotate,
    "resize": _resize,
    "timestamp": _timestamp,
}

validate_dict = {
    "annotate": validate_annotate_config,
    "resize": validate_resize_config,
    "timestamp": validate_timestamp_config,
}


def process_image(config: dict, process_name: str) -> list[bool]:
    # Checks
    valid_config = validate_dict[process_name](config)
    status_list = None
    if valid_config["status"] == "config_ok":
        files_list = get_files_list(config["source_directory"], config["process"])
        config["function"] = process_dict[process_name]
        # pprint(files_list)
        # pprint(valid_config)
        status_list = perform_multiprocessing(config, files_list)
    else:
        print(f"{valid_config['status']}")

    return status_list


# def resize_command(config: dict) -> list[bool]:
#     # Checks
#     valid_config = validate_resize_config(config)
#     status_list = None
#     if valid_config["status"] == "config_ok":
#         files_list = get_files_list(config["source_directory"], config["process"])
#         # pprint(files_list)
#         # pprint(valid_config)
#         config["function"] = _resize
#         status_list = perform_multiprocessing(config, files_list)
#     else:
#         print(f"{valid_config['status']}")
#
#     return status_list


def convert_images():
    return "Images Converted"

# def print_files(path:str , is_recersive:bool = False):
#     files = glob.glob(f"{path}/*")
#     return files
