from processing import *


if __name__ == "__main__":
    image = cv2.imread("../../data/images/image2.jpg")
    print(image.shape)
    print(count_faces(image))
    print(image)
    print(type(image))
