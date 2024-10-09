import source

login = input(f"> New Login: \n> ")
a = source.new_pass()

sql = f"""
        CREATE USER {login} WITH PASSWORD '{a}';
        GRANT USAGE ON SCHEMA public TO {login};
        """
        #GRANT SELECT ON ALL TABLES IN SCHEMA public TO {login};

if __name__ == "__main__":
    try:
        if source.exec_normal(sql=sql):
            print(f"> Your password: {a}")
    except Exception as e:
        print(f"> {e}")
