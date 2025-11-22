from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=10):
    try:
        image = Image.open(image_path)
        image = image.resize((150, 150))  # Resize to speed up
        image = image.convert('RGB')
        
        pixels = list(image.getdata())
        counter = Counter(pixels)
        most_common = counter.most_common(num_colors)
        
        hex_colors = []
        for color, count in most_common:
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            hex_colors.append(hex_color)
            
        return hex_colors
    except Exception as e:
        return str(e)

image_path = r"c:\Users\PC GOAT\Documents\ingles-2025-2026\paginas web\salon hm\295634114_944816933078172_5147936675844224673_n (2).jpg"
colors = get_dominant_colors(image_path)
print(colors)
