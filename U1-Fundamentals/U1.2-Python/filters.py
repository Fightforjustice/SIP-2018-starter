# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(image):
  my_image = PIL.Image.open(image)
  return my_image


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
  Image.show(image)

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image):
  Image.save(image)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
  new_image = PIL.Image.new(RGB, image.size)
  sequence = image.getdata()
  
  for x in range image.width:
    for y in range image.height:
      index = x * image.width + y
      pixel = image.getpixel(xy)
      if math.sumf(pixel) < 182:
        sequence[index] = (0, 51, 76)
      elif math.sumf(pixel) >= 182 and math.sumf(pixel) < 364:
        sequence[index] = (217, 26, 33)
      elif math.sumf(pixel) >= 364 and math.sumf(pixel) < 546:
        sequence[index] = (112, 150, 158)
      else:
        sequence[index] = (252, 227, 166)
        
    new_image = new_image.putdata(sequence)
    return new_image
        
  
  
