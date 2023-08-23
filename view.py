from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import image
from typing import Tuple
import random


def pick_random_colour() -> Tuple[int, int, int]:
    r = random.random()
    g = random.random()
    b = random.random()

    return (r, g, b)



def add_yolo_line(line: str, image_height: int, image_width: int, classes: list[str]) -> None:
    if line.strip() == '':
        return
    
    values = line.split(' ')
    class_index = int(values[0])

    all_values = list(values[1:])
    all_values.append(values[1])
    all_values.append(values[2])

    xs = [int(float(x) * image_width) for i, x in enumerate(all_values) if i % 2 == 0]
    ys = [int(float(y) * image_height) for i, y in enumerate(all_values) if i % 2 == 1]
    colour = pick_random_colour()

    # draw box
    plt.plot(xs, ys, linewidth=2, color=colour, marker='o', markersize=3)
    plt.text(xs[0], ys[0], classes[class_index], color=colour, fontsize=12)


def main():
    print('Yolov8 viewer\n')
    labels_file = Path(input('Enter labels file path: '))
    yolo_file = Path(input('Enter yolo file path: '))
    image_file = Path(input('Enter image file path: '))

    assert labels_file.exists(), 'Labels file does not exist'
    assert yolo_file.exists(), 'Yolo file does not exist'
    assert image_file.exists(), 'Image file does not exist'

    classes = labels_file.read_text().split('\n')
    print('\nClasses:')
    print("\n".join(classes))

    yolo = yolo_file.read_text().split('\n')
    print('\nYolo:')
    print(f"Found {len(yolo)} objects")

    img = image.imread(image_file)
    print('\nImage:')

    image_height = img.shape[0]
    image_width = img.shape[1]

    print(f"Image is {image_width}x{image_height}")

    dpi = 96
    plt.figure(figsize=(image_width/dpi, image_height/dpi), dpi=dpi)

    # draw boxes
    for line in yolo:
        add_yolo_line(line, image_height, image_width, classes)

    # show output
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    main()



