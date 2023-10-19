import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

def resize_image(image, width, height):
  #Resizes an image to the specified width and height.

  resized_image = image.resize((width, height))
  return resized_image

def watermark_image(image, watermark_text):
  #Watermarks an image with the specified text."""

  draw = ImageDraw.Draw(image)
  draw.text((10, 10), watermark_text, fill=(255, 255, 255))
  return image

def main():
  #Resizes and watermarks an image.

  # Get the input image.
  input_image_path = './input.jpg'
  input_image = Image.open(input_image_path)

  # Resize the image.
  resized_image = resize_image(input_image, 300, 300)

  # Watermark the image.
  watermarked_image = watermark_image(resized_image, 'Watermarked')

  # Save the watermarked image.
  watermarked_image_path = './watermarked.jpg'
  watermarked_image.save(watermarked_image_path)

if _name_ == '__main__':
  main()
