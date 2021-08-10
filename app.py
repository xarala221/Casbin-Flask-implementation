from flask import Flask, render_template, request, redirect

import casbin

e = casbin.Enforcer("./configs/model.conf", "./configs/policy.csv")


app = Flask(__name__)

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

@app.route("/")
def index():
    result = None
    if e.enforce(sub, obj, act):
        # permit alice to read data1
        result = True
    else:
        # deny the request, show an error
        result = False
    return render_template("index.html", result=result)




if __name__ == '__main__':
    app.run(debug=True)