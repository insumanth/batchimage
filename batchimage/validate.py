# import glob
# import re
#
# from logger import log
#
#
# def is_valid_directory(path: str) -> bool:
#     # TODO Implement.
#     return True
#
#
# def is_valid_interpolation_flag(flag: int) -> bool:
#     return flag in [0, 1, 2, 3, 4, 5, 6, 7, 8, 16]
#
#
# def validate_resize_config(config: dict) -> dict:
#     if not is_valid_directory(config['source_directory']):
#         config["status"] = "Source Directory is not Proper"
#     elif not is_valid_directory(config['destination_directory']):
#         config["status"] = "Destination Directory is not Proper"
#     else:
#
#         # Source and Destination are valid directory.
#         # Checking Input Options.
#
#         if config["scale"]:
#             config["use_key"] = "scale"
#             config["status"] = "config_ok"
#             print(f"Resizing Based on Scale : {config['scale']}")
#
#         elif config["width"] and config["height"]:
#             # The isdecimal() checks will be done by typer itself, since we mentioned as int.
#             config["use_key"] = "dimensions"
#             config["status"] = "config_ok"
#             print(f"Resizing Based on width and height : width = {config['width']} and height = {config['height']}")
#
#         elif config["dimensions"]:
#             # Replacing all different symbol, used to delimit width and height with 'x'.
#             dimensions = re.sub("[*,|]", "x", config["dimensions"].lower().strip())
#             if re.match("^\d{1,5}x\d{1,5}$", dimensions):
#                 width, height = dimensions.split("x")
#                 # Try Except is not needed as we used Regex to check numbers.
#                 config["width"] = int(width)
#                 config["height"] = int(height)
#                 config["use_key"] = "dimensions"
#                 config["status"] = "config_ok"
#                 print(f"Resizing Based on dimensions : {dimensions}")
#             else:
#                 config["status"] = "Dimensions are not in proper format"
#                 print(f"The Value of Width and/or Height is not proper : {config['dimensions']}")
#
#         else:
#             config["status"] = "Improper / Invalid Option / Insufficient Options"
#             print(f"Invalid Option")
#
#     if not is_valid_interpolation_flag(config["interpolation"]):
#         config["status"] = "Invalid Interpolation Flag given"
#
#     return config
#
#
# if __name__ == '__main__':
#     value = get_all_images_form_directory("/home/sumanth/Videos/projects/python/images")
#     print(value)




def is_valid_directory(path: str) -> bool:
    # TODO Implement.
    return True








