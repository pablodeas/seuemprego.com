import source

sql = 'src/queries/migration.sql'

if __name__ == "__main__":
    try:
        source.exec_file(sql=sql)
    except Exception as e:
        print(f"> {e}")
