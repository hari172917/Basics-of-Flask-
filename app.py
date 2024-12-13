from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def welcome():
    print("HELLO EVERY ONE")
    return render_template("index.html")
@app.route("/Greet",methods=["POST","GET"])
def greet():   

    name=request.form.get("name")
    if name:
        return f"Q4     Hello {name}"
    else:
        return f"Q4           Hello Guest"
    

@app.route("/calc/<ops>&<n1>&<n2>")
def operations(ops,n1,n2):
    first_num=int(n1)
    second_num=int(n2)
    if (ops == 'add'):
        result = first_num + second_num
        return f"Addition of {first_num} and {second_num} is {result}."
    if (ops == 'subtract'):
        result = first_num - second_num
        return f"Addition of {first_num} and {second_num} is {result}."
    if (ops == 'multiply'):
        result = first_num * second_num
        return f"Addition of {first_num} and {second_num} is {result}."
    if (ops == 'divide'):
        result = first_num / second_num
        return f"Addition of {first_num} and {second_num} is {result}."

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)