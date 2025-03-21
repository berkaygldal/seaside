import requests
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
image_url = "https://avatars.githubusercontent.com/u/143879221"  
response = requests.get(image_url)
response.raise_for_status()
plt.imshow(Image.open(BytesIO(response.content)))
plt.axis("off") 
plt.show()
