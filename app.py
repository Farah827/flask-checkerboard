from flask import Flask , render_template

app= Flask(__name__)

@app.route('/')
def checkerBoardDefualt():
    return render_template("checkboard.html" , rows=8 ,cols=8 ,color1="red" ,color2="black")

@app.route('/<int:y>')
def checkerBoard_y(y):
    return render_template("checkboard.html" , rows=8 , cols=y , color1="red" ,color2="black")

@app.route('/<int:x>/<int:y>')
def ceckerBoard_x_y(x,y):
    return render_template("checkboard.html" , rows=x ,cols=y ,color1="red" ,color2="black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkBoard(x=8 ,y=8, color1="black" ,color2='red'):
    return render_template("checkboard.html" ,rows =x ,cols=y , color1=color1 , color2=color2)



if __name__ == "__main__":
    app.run(debug=True)