import random
import re
from datetime import datetime
from flask import Flask,render_template, request, redirect
from zhuyin_type import ZhuyinType
from zhuyin_practicer import load_zhuyin_json_list

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET","POST"])
def home():
    # return "Hello, Flask!"
    return render_template("index.html")


@app.route("/hello/<name>", methods=["GET", "POST"])
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/practice/<selected_type>", methods=["GET","POST"])
def practice(selected_type):



    zhuyin_practice_list = load_zhuyin_json_list(selected_type)
    # [i for i in zhuyin_practice_list]

    random.shuffle(zhuyin_practice_list)
    print(zhuyin_practice_list)
    # content = "The type: " + type
    # return content
    return render_template("practice.html",
                           type_to_practice = selected_type.capitalize(),
                           zhuyin_practice_list = zhuyin_practice_list)



# @app.route("/practice/<selected_type>", methods=["GET", "POST"])
# def practice(selected_type):
#     zhuyin_practice_list = load_zhuyin_json_list(selected_type)

#     if request.method == "POST":
#         # Process answers
#         results = []
#         for i, zhuyin in enumerate(zhuyin_practice_list, start=1):
#             user_answer = request.form.get(f"answer_{i}")
#             correct = user_answer == zhuyin["answer"]
#             results.append({
#                 "question": zhuyin["question"],
#                 "user_answer": user_answer,
#                 "correct_answer": zhuyin["answer"],
#                 "correct": correct
#             })

#         # Render results page
#         return render_template("results.html", results=results, type_to_practice=selected_type.capitalize())

#     # Initial GET request to load the practice questions
#     return render_template("practice.html",
#                            type_to_practice=selected_type.capitalize(),
#                            zhuyin_practice_list=zhuyin_practice_list)
