from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/day/<number>')
def get_day(number):
    template_name = f"day-{number}.html"
    return render_template(template_name)


@app.route('/day/<number>/solution')
def get_solutions(number):
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
