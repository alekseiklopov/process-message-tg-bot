import requests


def process_photo(img_file):
    print(img_file)
    if test_curl():
        files = {
            "image": ("image.jpg", img_file),
        }
        response = requests.post("http://localhost:4000/api/containFace", files=files)
        print(response)
        return "Connection succeed"
    return "No connection"


def test_curl():
    test_response = requests.get("http://localhost:4000/api/test")
    if test_response == "Test success\n":
        print("Server's answering")
        return True
    print("Server's not answering")
    return False
