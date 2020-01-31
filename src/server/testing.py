import cv2
import requests
# import os


def send_image_curl(img_file):
    print(type(img_file))
    files = {
        "image": ("image.jpg", img_file),
    }
    if test_curl():
        response = requests.post("http://localhost:4000/api/containFace", files=files)
        print(response)
        return response
    return None
    pass


def test_curl():
    test_response = requests.get("http://localhost:4000/api/test").text
    if test_response == "Test success\n":
        print("Server's answering")
        return True
    print("Server's not answering")
    return False


if __name__ == "__main__":
    # print(os.listdir("./"))
    image = cv2.imread("./data/images/image1.jpg")
    print(image.shape)
    print(type(image))

    print(test_curl())
    send_image_curl(image)
