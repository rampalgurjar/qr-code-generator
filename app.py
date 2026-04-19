from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        qr_img = qrcode.make(url)
        
        # Save the QR code in the static folder
        save_folder = os.path.join(app.root_path, "static")
        save_path = os.path.join(save_folder, "qr-img.png")
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        
        qr_img.save(save_path)

        # Relative path for rendering the image
        qr_image_url = "/static/qr-img.png"

        return render_template("index.html", qr_image=qr_image_url)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run('localhost', 100, debug=True)