import database
from bottle import request, redirect, template, post, run, route

database.setup_database()
@route("/")
def get_index():
    redirect("/list1")

@route("/list1")
def get_list1():
    query = request.query.get("query")
    if(query): 
        rows1 = database.get_filtered_sports(query)
    else:
        rows1 = database.get_sports()
        query = ""
    return template("list1.tpl", sports=rows1, query=query)

@route("/list2")
def get_list2():
    players = database.get_players()
    return template("list2.tpl", players=players)


@route("/add1")
def get_add1():
    return template("add_sport.tpl")

@route("/add2")
def get_add2():
    sports = database.get_sports()
    return template("add_player.tpl", sports=sports)


@post("/add1")
def post_add1():
    name = request.forms.get("name")
    category = request.forms.get("category")
    database.add_sport(name, category)
    redirect("/list1")
@post("/add2")
def post_add2():
    name = request.forms.get("name")
    age = request.forms.get("age")
    sport=request.forms.get("sport")
    database.add_player(name, age, sport)
    redirect("/list2")


@route("/delete1/<id>")
def get_deletesp(id):
    database.delete_sport(id)
    redirect("/list1")
@route("/delete2/<id>")
def get_deletepl(id):
    database.delete_player(id)
    redirect("/list2")


@route("/update1/<id>")
def get_update1(id):
    rows1 = database.get_sports(id)
    if len(rows1) != 1:
        redirect("/list1")
    name=rows1[0]['name']
    category=rows1[0]['category']
    return template("update_sport.tpl", id=id, name=name,category=category)
@route("/update2/<id>")
def get_update2(id):
    rows2 = database.get_players(id)
    if len(rows2) != 1:
        redirect("/list2")
    name = rows2[0]['name']
    age = rows2[0]['age']
    sport = rows2[0]['sport']
    sports = database.get_sports()
    return template("update_player.tpl", id=id, name=name, age=age,sport=sport, sports=sports)


@post("/update1")
def post_update1():
    id = request.forms.get("id")
    name = request.forms.get("name")
    category = request.forms.get("category")
    database.update_sport(id, name,category)
    redirect("/list1")

@post("/update2")
def post_update2():
    id = request.forms.get("id")
    name = request.forms.get("name")
    age = request.forms.get("age")
    sport = request.forms.get("sport")
    database.update_player(id, name,age,sport)
    redirect("/list2")


run(host='localhost', port=8081)