import source
import pandas as pd

a = source.exec_normal("select title, description, TO_CHAR(creation_date::timestamp, 'DD-MM-YYYY'), contact from public.vaga")

df = pd.DataFrame()
for x in a:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html("vagas.html")