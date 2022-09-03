
import cv2

from rich.pretty import pprint

def resize(
        source_directory: str,
        destination_directory: str,
        scale_percentage: int = None,
        width: int = None,
        height: int = None,
        prefix: str = None,
        suffix: str = None,
):
    pass


def _resize(config: dict) -> bool:
    status = False
    if config["use_key"] == "scale":
        status = resize_by_scale(
            config["file_list"],
            config["destination_directory"],
            config["scale"],
            config["interpolation"],
            config["prefix"],
            config["suffix"],
        )
    elif config["use_key"] == "dimensions":
        status = resize_by_dimension(
            config["file_list"],
            config["destination_directory"],
            config["height"],
            config["width"],
            config["interpolation"],
            config["prefix"],
            config["suffix"],
        )
    else:
        print("Invalid Option")

    return status


def resize_by_scale(input_files: list, destination_directory: str, scale: int, interpolation: int, prefix=None, suffix=None) -> bool:
    # pprint("inside resize_by_scale")
    # pprint([input_files, destination_directory, scale, interpolation, prefix, suffix])

    for file in input_files:
        image_name = file.split('/')[-1]
        image = cv2.imread(file)
        processed_image = cv2.resize(image, None, fx=scale/100, fy=scale/100, interpolation=interpolation)
        destination_file_name = f"{destination_directory}/{image_name}"
        status = cv2.imwrite(destination_file_name, processed_image)
        print(f"File Saved Status {status} for {image_name}")

    return True


def resize_by_dimension(input_files: list, destination_directory: str, height: int, width: int, interpolation: int,
                        prefix=None,  suffix=None) -> bool:
    # pprint("inside resize_by_dimension")
    # pprint([input_files, destination_directory, height, width, interpolation, prefix, suffix])

    for file in input_files:
        image_name = file.split('/')[-1]
        image = cv2.imread(file)
        processed_image = cv2.resize(image, (width, height), interpolation=interpolation)
        destination_file_name = f"{destination_directory}/{image_name}"
        status = cv2.imwrite(destination_file_name, processed_image)
        print(f"File Saved Status {status} for {image_name}")

    return True
