from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/data')
def data():
    # Generate your data here
    data = {
        'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        'datasets': [{
            'label': '# of Votes',
            'data': [12, 19, 3, 5, 2, 3],
            'backgroundColor': [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            'borderColor': [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            'borderWidth': 1
        }]
    }
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)

#/* This is a future template for loading up the Chart.js file.
#fetch('/data')
#    .then(response => response.json())
#
#    .then(data => {
#        var ctx = document.getElementById('myChart').getContext('2d');
#       var myChart = new Chart(ctx, {
#           type: 'bar',
#           data: data,
#           options: {
#               scales: {
#                   y: {
#                       beginAtZero: true
#                   }
#               }
#           }
#       });
#   });
#*/
