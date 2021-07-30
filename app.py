from flask import Flask,render_template,request,redirect,url_for
import time,datetime
import re
import pafy
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_youtube',methods=["POST","GET"])
def download():
    if request.method == "POST":
        url = request.form['search']
        if (re.search('watch', url)):
            url = url.split('v=', 1)[1]
            try:
                video = pafy.new(url)
                print (video)
            except:
                url = url[0:11]
                video = pafy.new(url)
            title = video.title
            duration = video.duration
            author = video.author
            thumb = ''
            if video.bigthumb:
                thumb = video.bigthumb
            else:
                thumb = video.thumb
            streams = video.streams
            data = {'arrr':streams,'title':title,'thumb':thumb}
            return render_template('download.html', data = {'arrr':streams,'title':title,'thumb':thumb},duration=duration, author= author ) 
        elif (re.search('playlist',url)):
            #print (url)
            #playlist = pafy.get_playlist(url)
            #bilol = len(playlist['items'])
            #arr = []
            #for i in range(0, bilol):
                #pk = playlist['items'][i]['pafy']
                #arr.append(pk)
            
            return render_template('index.html', videos_playlist=True)
        else:
            url = url.split('be/', 1)[1]
            video = pafy.new(url)
            title = video.title
            thumb = ''
            if video.bigthumb:
                thumb = video.bigthumb
            else:
                thumb = video.thumb
            streams = video.streams
            data = {'arrr':streams,'title':title,'thumb':thumb}
            return render_template('download.html', data = {'arrr':streams,'title':title,'thumb':thumb})
    return render_template('index.html') 


app.run(debug=True)
