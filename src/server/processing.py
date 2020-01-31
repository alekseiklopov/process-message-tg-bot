from mtcnn.mtcnn import MTCNN
import numpy as np
import io
import PIL.Image
import json

FACE_DETECTOR = MTCNN()


# def process_photo(img_bytes):
#     img = get_img_by_byte_stream(img_bytes)
#     print("shape", img.shape)
#     print("type", type(img))
#     print("image:", img)
#     # cv2.imwrite("../data/images/image2.jpg", img)
#     image = cv2.imread("../data/images/image2.jpg")
#     print(image.shape, type(image), image)
#     number_of_faces = count_faces(image)
#     print("number of faces: {}".format(number_of_faces))
#     if number_of_faces > 0:
#         return "Faces found!"
#     return "Faces not found!"


def count_faces(img):
    global FACE_DETECTOR
    faces = FACE_DETECTOR.detect_faces(img)
    return len(faces) if faces else 0


def get_img_by_byte_stream(im_bytes):
    im = np.array(PIL.Image.open(io.BytesIO(im_bytes)))
    return im


def get_json_response(status, description, data):
    return json.dumps({
        "status": status,
        "description": description,
        "data": data
    }) + "\n"
