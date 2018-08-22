from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("form.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
    for key, value in request.form.items():
        print(key, ":", value)

    key_list = list(request.form.keys())
    name = request.form["firstname"] + " " + request.form["lastname"]
    #personal info is a dictionary containing all the personal info of the person
    personal_info = {}
    for i in range(2, 10):
        putInDict(personal_info, request.form, key_list[i])
    print(personal_info)

    #edu_info is a list containing dictionaries, where each dictionary contains one education block
    edu_1 = {}
    for i in range(10, 16):
        putInDict(edu_1, request.form, key_list[i])

    edu_2 = {}
    for i in range(16, 22):
        putInDict(edu_2, request.form, key_list[i])

    edu_info = [edu_1, edu_2]
    print(edu_info)

    #job_info is a list containing dictionaries, where each dictionary contains one job block
    job_1 = {}
    for i in range(22, 28):
        putInDict(job_1, request.form, key_list[i])

    job_2 = {}
    for i in range(28, 34):
        putInDict(job_2, request.form, key_list[i])

    job_info = [job_1, job_2]
    print(job_info)

    #act_info is a list containing dictoinaries, where each dictionary contains one activity block
    act_1 = {}
    for i in range(34, 41):
        putInDict(act_1, request.form, key_list[i])

    act_info = [act_1]
    print(act_info)

    return render_template("result.html", name=name, personal_info=personal_info, edu_info=edu_info, job_info=job_info, act_info=act_info)

def putInDict(newDict, oldDict, key):
    newDict[key] = oldDict[key]

if __name__ == '__main__':
   app.run(debug = True)
