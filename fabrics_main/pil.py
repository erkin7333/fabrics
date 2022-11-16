from rembg import remove
from PIL import Image
input_path = 'sofdilshop.png'
output_path = 'img/logoshop/png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)