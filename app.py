from pytube import YouTube
from flask import Flask, request, send_file
from io import BytesIO
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/download')
def download():
    url = request.args.get("url")
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    video = BytesIO()
    stream.stream_to_buffer(buffer=video)
    video.seek(0)
    return send_file(video, mimetype="video/mp4", as_attachment=True, download_name=f"{yt.title}.mp4")

if __name__ == '__main__':
    app.run(debug=True)
