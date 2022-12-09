import mysql
import schedule
import time

bd = mysql.connector.connect(host='localhost', user='root', password='', database='python_test')


def search_in_autho(lp):
    c = False
    cursor = bd.cursor()
    licence_plates = list()
    cursor.execute("select licence_plate from users;")
    licence_plates = cursor.fetchall()
    for i in licence_plates:
        if i == lp:
            c = True
            return c

    return c


def search_in_visitor(lp):
    c = False
    cursor = bd.cursor()
    licence_plates = list()
    cursor.execute("select licence_plate from users;")
    licence_plates = cursor.fetchall()
    for i in licence_plates:
        if i == lp:
            c = True
            return c

    return c


def add_visitor(lp):
    cursor = bd.cursor()
    cursor.execute(f"insert into users values('{lp}');")

    return True


def remove_visitor(lp):
    cursor = bd.cursor()
    cursor.execute(f"delete from users where licenece_plate='{lp}';")
    return True


def add_in_control_entrance(lp, type):
    cursor = bd.cursor()
    cursor.execute(f"insert into controle_entrance values('{lp}','{type}');")


def add_autho(lp):
    cursor = bd.cursor()
    cursor.execute(f"insert into known_plates values('{lp}');")
    return True


def remove_autho(lp):
    cursor = bd.cursor()
    cursor.execute(f"delete from known_plate where licenece_plate='{lp}';")
    return True

def show_autho():
    cursor = bd.cursor()
    cursor.execute("SELECT* FROM known_plate;")
    autho = cursor.fetchall()


def main(lp):

    A = search_in_autho(lp)
    if not A:
        exist = search_in_visitor(lp)
        if not exist:
            cursor = bd.cursor()
            cursor.execute(f"insert into visitor values('{lp}');")
            add_in_control_entrance(lp, "V")
        if exist:
            cursor = bd.cursor()
            cursor.execute(f"delete from visitors where licence_plate='{lp};")

    if A:
        cursor = bd.cursor()
        add_in_control_entrance(lp, "A")



