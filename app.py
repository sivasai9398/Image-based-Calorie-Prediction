from flask import request
import torch
import os
import json
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from collections import Counter
from PIL import Image

app = Flask(__name__, static_folder=r"D:\calorie prediction\gen_images")
@app.route('/', methods=['GET'])
def intro():
    return render_template('nor.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        # we will get the file from the request
        print("Yess")
        f = request.files['file']
        # convert that to bytes
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'user_data_photos', secure_filename(f.filename))
        f.save(file_path)
        n = f.filename
        path = n
        p = path
        li = p.split(".")
        new_name = li[0] + ".jpg"
        final_str = r"D:\calorie prediction\gen_images" + "/" + path
        im = Image.open(file_path)
        new_im = im.convert("RGB")
        new_im.save(new_name)
        image = Image.open(file_path)
        image.thumbnail((640, 640), Image.ANTIALIAS)
        new_path = r"D:\calorie prediction\user_data_photos" + "/" + li[0] +".jpg"
        image.save(new_path)
        model = torch.hub.load(r'D:\calorie prediction\yolov5', 'custom', path=r'D:\est-less_dosa.pt', force_reload=True, source="local")
        r = model(new_path)
        #r = model(new_name)
        r.print()
        a = r.pandas().xyxy[0].to_json(orient="records")
        b = json.loads(a)
        names = []
        for i in b:
            names.append(i["name"])
        #print(names)
        r.save(save_dir=r"D:\calorie prediction\gen_images")
        c = Counter(names)
        print(path)
        cal_count = {'donut': 452, 'Cookies': 40, 'pizza': 2000, 'burger' : 254, 'samosa': 250, 'popcorn': 106}
        tot = 0
        for i in c.keys():
            tot += cal_count[i]*c[i]
        return render_template('new.html', name=c, path=new_name, tot=tot)
    return render_template('nor.html')
if __name__ == '__main__':
    app.run(debug=True)
