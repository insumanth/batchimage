"""
Multiprocessing Module
"""

from multiprocessing import Pool
from resize import _resize

from rich.pretty import pprint

def perform_multiprocessing(config: dict, files_list: list[str]) -> list[bool]:

    args_list = []
    status_list = []

    for files in files_list:
        args = config.copy()
        args["file_list"] = files
        args_list.append(args)

    # pprint(files_list)
    # pprint(args_list)

    process_count = len(args_list)
    call_function = config["function"]

    with Pool(process_count) as p:
        dist_work = p.imap_unordered(call_function, args_list)
        for status in dist_work:
            status_list.append(status)

    return status_list




def invalid_function(*dummy_args) -> bool:
    print("Inside Invalid Function")
    return False

