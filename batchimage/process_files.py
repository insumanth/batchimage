from numpy import array_split
from glob import iglob
import re


def get_all_images_form_directory(path: str) -> list[str]:
    all_files = iglob(f"{path}/*")
    image_files = []
    extract_extension = re.compile("\.\w{2,4}?$")
    opencv_support = ['.bmp', '.dib', '.jpeg', '.jpg', '.jpe', '.jp2', '.png', '.webp', '.pbm', '.pgm', '.ppm', '.pxm',
                      '.pnm', '.pfm', '.sr', '.ras', '.tiff', '.tif', '.exr', '.hdr', '.pic', ]
    for file in all_files:
        extension = extract_extension.search(file)
        if extension:
            if extension.group(0) in opencv_support:
                image_files.append(file)
    return image_files


def split_files(file_names: list[str], parts: int) -> list[list[str]]:
    # Converting into list of numpy Arrays

    split_file_list = [list(chunk) for chunk in array_split(file_names, parts)]
    return split_file_list


def get_files_list(path: str, parts: int):

    all_files = get_all_images_form_directory(path)
    file_list = split_files(all_files, parts)
    return file_list



if __name__ == '__main__':
    a = get_all_images_form_directory("/home/sumanth/Videos/projects/python/images/all")
    for i in split_files(a,4):
        print(i)
