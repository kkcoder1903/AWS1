# Image Processing Script

This Python script is designed to perform simple image processing tasks, including resizing an image to a specified width and height and adding a watermark to the image. The script utilizes the Python Imaging Library (PIL) to manipulate images and Docker for containerization.

## Prerequisites

Before running this script, you need to have the following prerequisites in place:

- **Python and Pip**: Make sure you have Python installed on your system. You can install Python and Pip using your package manager or by downloading the official Python distribution from [python.org](https://www.python.org/downloads/).

- **Pillow (PIL Fork)**: Install the Pillow library, which is a maintained fork of the Python Imaging Library (PIL). You can install it using Pip:

  ```bash
  pip install pillow
  ```

- **Docker**: If you plan to use this script in a Docker container, you need to have Docker installed on your system. Refer to the [official Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-directory
   ```

2. **Build the Docker Image** (Optional):

   If you want to run this script inside a Docker container, you can build a Docker image using the provided `Dockerfile`. Navigate to the script directory and run:

   ```bash
   docker build -t image-processor .
   ```

3. **Configure the Script**:

   Edit the script to specify the input image path, output image path, and watermark text:

   ```python
   # Set the input image path
   input_image_path = './input.jpg'
   
   # Set the watermark text
   watermark_text = 'Watermarked'
   
   # Set the output image path
   watermarked_image_path = './watermarked.jpg'
   ```

4. **Run the Script**:

   Run the script using Python:

   ```bash
   python image_processor.py
   ```

   If you've built a Docker image, you can run the script within a Docker container:

   ```bash
   docker run -v /path/to/local/images:/app/images image-processor
   ```

   Replace `/path/to/local/images` with the directory containing your input image.

5. **Output**:

   The script will resize the input image, add the watermark, and save the watermarked image to the specified output path.

## Docker Usage (Optional)

If you choose to run the script in a Docker container, you can build the Docker image as mentioned earlier and use it to process images in a containerized environment. Ensure that you provide the necessary volume binding to access the input image and store the output image outside the container.

## Disclaimer

This script is a simple example for image processing tasks. Depending on your use case, you may need to customize it for more advanced image processing needs. Use this script responsibly and ensure that you have the required permissions to read and write files in the specified directories.
