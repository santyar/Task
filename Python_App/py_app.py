


from flask import Flask,send_file

app=Flask(__name__)

@app.route('/')
def hello():
	return "<H1 style='color:blue'>Hello from Flassk freamwork!</H1>"
@app.route('/image')
def hello_image():
	filename='welcom.jpg'
	return send_file(filename, mimetype='image/gif')

if __name__=='__main__':
	app.debug = True
	app.run()
