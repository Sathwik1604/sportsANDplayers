from peewee import *

db = SqliteDatabase('tournament.db')
db.connect()

class Sport(Model):
    name = CharField()
    category=CharField()
    class Meta:
        database = db 

class Player(Model):
    name = CharField()
    age=CharField()
    sport=ForeignKeyField(Sport, backref='players')
    class Meta:
        database = db 

def setup_database():
    db.drop_tables([Sport,Player],safe=True)
    db.create_tables([Sport,Player])
    
def get_sports(id=None):
    if id == None:
        sind = Sport.select()
    else:
        sind = Sport.select().where(Sport.id == id)
    sind = [
        { 
            "id" : s.id,
            "name" : s.name,
            "category" :s.category
        } 
        for s in sind
    ]
    return sind

def get_players(id=None):
    if id == None:
        pind = Player.select()
    else:
        pind = Player.select().where(Player.id == id)
    pind = [
        { 
            "id" : p.id,
            "name" : p.name,
            "age" :p.age,
            "sport":p.sport.name
        } 
        for p in pind
    ]
    return pind

def get_filtered_sports(query):
    sind = Sport.select().where(Sport.name.contains(query) | Sport.category.contains(query))
    sind = [
        { 
            "id" : s.id,
            "name" : s.name,
            "category" :s.category
        } 
        for s in sind
    ]
    return sind


def add_sport(name,category):
    sind = Sport(name=name,category=category)
    sind.save()

def add_player(Player_name,Player_age,sport):
    pind = Player(name=Player_name,age=Player_age,sport=sport)
    pind.save()


def delete_sport(id):
    sind = Sport.select().where(Sport.id == id).get()
    sind.delete_instance()

def delete_player(id):
    pind = Player.select().where(Player.id == id).get()
    pind.delete_instance()

def update_sport(id, name,category):
    Sport.update({Sport.name: name,Sport.category:category}).where(Sport.id == id).execute()
def update_player(id, name,age,sport):
    Player.update({Player.name: name,Player.age:age,Player.sport:sport}).where(Player.id == id).execute()

