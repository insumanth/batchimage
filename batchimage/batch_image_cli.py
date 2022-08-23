# Package Imports
import typer

# Module Imports
from batch_image_module import convert_images
from batch_image_module import print_files


# Typer App
app = typer.Typer()


@app.callback(
    invoke_without_command=True,
)
def main(
        default: str  = typer.Option(
            "",
            "--dict",
            "-d",
            help="Python Dictionary / Ruby Hash name",
        ),
    ):

    """
        Process large batches of images in parallel.

        You can,

                🔹 Compress Images - 🗜️

                🔹 Convert Images  - 🔄

                🔹 Crop Images  - 🔲

                🔹 Apply Filters  - 💅

                🔹 Convert Images  - 🔄


        \n

        batchimage on Pypi           :  https://pypi.org/project/batchimage

        batchimage on Github         :  https://github.com/insumanth/batchimage

        Please report any issues     :  https://github.com/insumanth/batchimage/issues
    """

    print(f"Main {default}")




@app.command()
def display(
        directory_path: str,
    ):
    print(directory_path)
    print(print_files(directory_path))


@app.command()
def compress(

        source: str = typer.Argument(
            ...,
            help="Source Directory containing Image files",
            metavar="source",
            # rich_help_panel="compress",
        ),

        destination: str = typer.Argument(
            ...,
            help="Destination Directory where processed images are stored",
            metavar="destination",
            # rich_help_panel="compress",
        ),


    ):
    print(f"{source} \n {destination}")


@app.command()
def convert(

    ):
    print(f"{item} ")





def start() -> None:
    app()


if __name__ == "__main__":
    app()



