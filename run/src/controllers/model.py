#!/usr/bin/env python3


def create_user(user_name , password):

    with Database() as db:
        create_table()
        user_name_taken = check_user_exist(user_name)
        if user_name_taken==False:
            sql='''INSERT INTO users(user_names,password) 
                            Values(?,?);'''
            db.c.execute(sql, (user_name, password))
            return True
        else:
            return False

def check_user_exist(user_name):
    with Database() as db:
        db.c.execute('''SELECT * FROM users WHERE user_names='{}';'''.format(user_name))
        result=db.c.fetchone()

        if result:
            return True
        else:
            return False

def check_user(user_name, password):
    with Database() as db:
        db.c.execute('''SELECT * FROM users WHERE user_names='{}'
                        AND password='{}';'''.format(user_name, password))
        result=db.c.fetchone()

        if result:
            return True
        else:
            return False