from config import app

@app.task
def run(ip):
	print ip
