#!/usr/bin/python3

# Import necessary modules
import argparse
from PIL import Image
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
import numpy as np
import io

# Define a function to generate an image from code
def generate_image_from_code(file_path, language, output_path):
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read the content of the file
        code = f.read()

    # Get the lexer for the specified language
    lexer = get_lexer_by_name(language)
    
    # Initialize the formatter for the image
    formatter = ImageFormatter(style='monokai', line_numbers=False)

    # Highlight the code using the lexer and formatter
    result = highlight(code, lexer, formatter)

    # Create an image from the highlighted code
    image = Image.open(io.BytesIO(result))

    # Save the image to the specified output path
    image.save(output_path)

# Define the main function
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Generate image from code.')

    # Add the file argument
    parser.add_argument('-f', '--file', type=str, help='The file to convert', required=True)

    # Add the language argument
    parser.add_argument('-l', '--language', type=str, help='The language of the file', required=True)

    # Add the output file argument
    parser.add_argument('-o', '--output', type=str, help='The output file', required=True)

    # Parse the arguments
    args = parser.parse_args()

    # Generate the image from the code using the arguments
    generate_image_from_code(args.file, args.language, args.output)

# If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
