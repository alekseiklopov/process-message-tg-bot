from flask import Flask, request
from processing import *

app = Flask(__name__)


@app.route("/api/test")
def test():
    return "Test success\n"

@app.route("/api/containFace")
def contain_face():
    img_file = request.files["image"]
    if img_file:
        np_img = np.fromfile(img_file, np.uint8)
        img = cv2.decode(np_img, cv2.IMREAD_COLOR)
        number_of_faces = count_faces(img)
        if number_of_faces:
            description = "number of faces: {}".format(number_of_faces)
            return get_json_response("success", desription, None)
        return get_json_response("noFace", None, None)
    return get_json_response("notFile", None, None) 


if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0", debug=False)

