from flask import Flask,render_template
app = Flask(__name__)

import analysis
import location_analysis

@app.route('/')
def home():
   return render_template('dashboard.html')

@app.route('/fields/<field>.html')
def f1(field):
   field_path='fields/'+field+'.html'
   return render_template(field_path)

@app.route('/charts/<field>_<chart>.html')
def f2(field,chart):
   chart_path='/charts/'+field+'_'+chart+'.html'
   return render_template(chart_path)

@app.route('/dashboard.html')
def f3():
   field_path='dashboard.html'
   return render_template(field_path)

if __name__ == '__main__':
   analysis.operate_the_functions()
   location_analysis.operate_the_functions_location()
   app.config['TEMPLATES_AUTO_RELOAD'] = True # for autoreloading html templates and update changes
   app.run()