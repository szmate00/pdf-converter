import os
from typing import Callable
from pdf2image import convert_from_path


def convert_pdf_to_image(file_path: str, output_format: str, output_folder: str, progress_callback: Callable) -> list:
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extract file name and extension
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))

    # Create a directory with the same name as the input file
    output_dir = os.path.join(output_folder, file_name)
    os.makedirs(output_dir, exist_ok=True)

    # Convert PDF to image using pdf2image library
    images = convert_from_path(file_path)

    # Save each image to the output folder
    output_files = []
    for i, image in enumerate(images):
        output_file_path = os.path.join(output_dir, f"page_{i+1:03d}.{output_format}")
        image.save(output_file_path, output_format)
        output_files.append(output_file_path)
        progress_callback((i+1) / len(images) * 100)

    return output_files
