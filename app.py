from flask import Flask
from flask import jsonify, request, render_template

app = Flask (__name__)

		
@app.route('/google-charts/line-chart')
def google_line_chart():
	#print(data)
	return render_template('line-chart.html')
	@app.route()	
if __name__ == "__main__":
    app.run()