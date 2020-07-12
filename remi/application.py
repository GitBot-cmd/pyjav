from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def lead():
    return render_template("lead.html")
@app.route('/more')
def more():
    foodlists = ['Efo riro', 'Fried rice', 'Goat stew']
    return render_template("more.html", foodlists = foodlist)
if __name__=='__main__':
    app.run()
