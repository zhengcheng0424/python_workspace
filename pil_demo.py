from PIL import Image


def resize_image(image_path, output_path, size):
    img = Image.open(image_path)
    img.thumbnail(size)
    img.save(output_path)


if __name__ == '__main__':
    resize_image('input.png', 'output.png', (500, 500))
