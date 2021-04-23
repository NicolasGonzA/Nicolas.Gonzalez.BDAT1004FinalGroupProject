from app import app
from flask import jsonify, request, render_template
		
@app.route('/google-charts/line-chart')
def google_line_chart():
	
@app.route ('line-chart.html')
def google_line_chart():
   
[ <!DOCTYPE html>
<html>
    <head>
      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
      <script type="text/javascript">
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
  
        function drawChart() {
          var data = google.visualization.arrayToDataTable([
            data = ['Todays Price', 'Historical Price'], 
                   [1.176 , 1.288],
                   [1.173, 1.318],
                   [1.189, 1.257],
                   [1.19, 1.264],
                   [1.253, 1.282],
                   [1.313,1.277],
          
                   #print(data)
	               return render_template('pie-line.html', data=data)

        ]);
  
            var options = {
            title: 'Stellar (XLM) Performance',
            curveType: 'function',
            legend: { position: 'bottom' }
          };
  
          var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
  
          chart.draw(data, options);
        }
      </script>
    </head>
    <body>
      <div id="curve_chart" style="width: 900px; height: 500px"></div>
    </body>
  </html>]
  		
if __name__ == "__main__":
    app.run()


