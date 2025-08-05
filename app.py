from flask import Flask , render_template

app= Flask(__name__)

@app.route('/')
@app.route('/<int:y>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkBoard(x=8 ,y=8, color1="black" ,color2='red'):
    return render_template("checkboard.html" ,row =x ,col=y , c1=color1 , c2=color2)



if __name__ == "__main__":
    app.run(debug=True)