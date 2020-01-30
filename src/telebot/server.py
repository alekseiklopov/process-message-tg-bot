import requests

def process_photo(img_file):
    print(type(img_file))
    files = {
        "image": ("image.jpg", img_file),
    }
    if test_curl():
        response = requests.post("http://localhost:4000/api/containFace", files=files)
        print(response)
        return responce
    return None


def test_curl():
    test_response = request.get("http://localhost:4000/api/test")
    if test_response == "Test success\n":
        print("Server's answering")
        return True
    print("Server's not answering")
    return False

