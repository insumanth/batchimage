
import cv2
from rich.pretty import pprint

# Validate Imports

from validate import is_valid_directory
import glob
import re



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






# validate Resize






def is_valid_interpolation_flag(flag: int) -> bool:
    return flag in [0, 1, 2, 3, 4, 5, 6, 7, 8, 16]


def validate_resize_config(config: dict) -> dict:
    if not is_valid_directory(config['source_directory']):
        config["status"] = "Source Directory is not Proper"
    elif not is_valid_directory(config['destination_directory']):
        config["status"] = "Destination Directory is not Proper"
    else:

        # Source and Destination are valid directory.
        # Checking Input Options.

        if config["scale"]:
            config["use_key"] = "scale"
            config["status"] = "config_ok"
            print(f"Resizing Based on Scale : {config['scale']}")

        elif config["width"] and config["height"]:
            # The isdecimal() checks will be done by typer itself, since we mentioned as int.
            config["use_key"] = "dimensions"
            config["status"] = "config_ok"
            print(f"Resizing Based on width and height : width = {config['width']} and height = {config['height']}")

        elif config["dimensions"]:
            # Replacing all different symbol, used to delimit width and height with 'x'.
            dimensions = re.sub("[*,|]", "x", config["dimensions"].lower().strip())
            if re.match("^\d{1,5}x\d{1,5}$", dimensions):
                width, height = dimensions.split("x")
                # Try Except is not needed as we used Regex to check numbers.
                config["width"] = int(width)
                config["height"] = int(height)
                config["use_key"] = "dimensions"
                config["status"] = "config_ok"
                print(f"Resizing Based on dimensions : {dimensions}")
            else:
                config["status"] = "Dimensions are not in proper format"
                print(f"The Value of Width and/or Height is not proper : {config['dimensions']}")

        else:
            config["status"] = "Improper / Invalid Option / Insufficient Options"
            print(f"Invalid Option")

    if not is_valid_interpolation_flag(config["interpolation"]):
        config["status"] = "Invalid Interpolation Flag given"

    return config











