# app.py
from flask import Flask, render_template, request, send_file, send_from_directory
import subprocess
import cv2
import os

app = Flask(__name__)


@app.route('/static/video/<path:filename>')
def download_file(filename):
    return send_from_directory('static/video', filename)


@app.route('/')
def index():
    return render_template('index.html')


# ... (other imports)


@app.route('/generate_video', methods=['POST', 'GET'])
def generate_video():
    print("I made it here")
    velocity = request.form.get('velocity')
    angle = request.form.get('angle')

    # Call your existing Python script with velocity and angle as arguments
    # Modify the command based on your script and file paths
    command = f"python ball_moving.py {velocity} {angle}"
    subprocess.run(command, shell=True)

    # Call a function to convert the images to video
    convert_images_to_video()

    # Provide a link to download the generated video
    # the bellow works but the bellow bellow does not
    # return f'<h2>Video Generated!</h2><p><a href="/download_video">Download Video</a></p>'
    return create_embedded_image()


def create_embedded_image():
    # place button in here
    html = """
    <html>
    <body style="text-align: center">
        <h1 style="color: green">Video Created!</h1>
        <video width="500px" height="500px" controls>
            <source src="static/video/simulation.mp4" type="video/mp4"/>
       </video>
       
        <a href="/" style="color: blue;">Back to Home</a>

    </body>
</html>
    """

    return html


@app.route('/download_video')
def download_video():
    # Provide the path to the generated video file
    video_path = 'static/video/simulation.mp4'
    return send_file(video_path, as_attachment=True)


def convert_images_to_video():
    # Your code to convert images to video (use a library like OpenCV)

    image_folder = 'static/images'
    video_name = 'static/video/simulation.mp4'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
    print("******DEUBGUGGIN", len(images))
    images.sort()  # Ensure the images are in the correct order

    """
    bug here
    """
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Use 'avc1' as the fourcc code for H.264 encoding
    video = cv2.VideoWriter(
        video_name, cv2.VideoWriter_fourcc(*'avc1'), 2, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

    for image in images:
        image_path = os.path.join(image_folder, image)
        os.remove(image_path)


"""
if shit goes tits up delete this 1/2
"""


if __name__ == '__main__':
    app.run(debug=True)
