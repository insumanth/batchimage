from validate import is_valid_directory
from rich.pretty import pprint
import time
import cv2

def validate_timestamp_config(config: dict) -> dict:
    if not is_valid_directory(config['source_directory']):
        config["status"] = "Source Directory is not Proper"
    elif not is_valid_directory(config['destination_directory']):
        config["status"] = "Destination Directory is not Proper"
    else:

        if config["strftime"]:
            try:
                config["timetext"] = time.strftime(config["strftime"], time.strptime(config["timetext"]))
            except:
                print("Failed to parse the time given as input to specified format. Using the original string")

        config["status"] = "config_ok"

    return config

def _timestamp(config: dict) -> bool:
    pprint(config)
    status = timestamp_image(
        config["file_list"],
        config["destination_directory"],
        config["timetext"],
        config["origin"],
        config["colour"],
        config["fontscale"],
        config["thickness"],
        config["prefix"],
        config["suffix"],
    )
    return status


def timestamp_image(input_files: list, destination_directory: str, text: str, origin: tuple[int, int],
                   colour: tuple[int, int, int], fontscale: float, thickness: float, prefix=None, suffix=None) -> bool:
    pprint([input_files, destination_directory, text, origin, colour, fontscale, thickness, prefix, suffix])

    for file in input_files:
        image_name = file.split('/')[-1]
        base_name, extension = image_name.rsplit(".",1)
        save_file_name = f"{prefix or ''}{base_name}{suffix or ''}.{extension}"
        image = cv2.imread(file)

        if origin == (-1, -1):
            # Printing Text at bottom left
            im_height, im_width, im_colour = image.shape
            origin = (20, im_height - 20)

        processed_image = cv2.putText(
            img=image,
            text=text,
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            org=origin,
            fontScale=fontscale,
            color=colour[::-1], # Since Open CV is BGR but we use RGB
            thickness=thickness
        )
        destination_file_name = f"{destination_directory}/{save_file_name}"
        status = cv2.imwrite(destination_file_name, processed_image)
        print(f"File Saved Status {status} for {save_file_name} | {image.shape} :: {origin}")

    return True


if __name__ == '__main__':
    timestamp_image(
        ["/home/sumanth/Videos/projects/python/images/test/src/Yatin_1660656871029.jpg"],
        "/home/sumanth/Videos/projects/python/images/test/workspace/",
        "Fri Sep  9 20:25:40 2022",
        (-1, -1),
        (255, 255, 255),
        1,
        1,
        "pre1_",
        "__suf",
    )
