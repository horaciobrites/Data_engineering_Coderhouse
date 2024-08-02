import psycopg2

def grabar_datos(host,port,dbname,user,password,schema,tabla,data):
    conn = psycopg2.connect(host=host,port=port,dbname=dbname,user=user,password=password)
    cur = conn.cursor()
    for index, row in data.iterrows():
        insert_sql = f"""
        INSERT INTO {schema}.{tabla} (idVariable, cdSerie, descripcion, fecha, valor)
        VALUES ({row['idVariable']}, {row['cdSerie']}, '{row['descripcion']}', '{row['fecha']}', {row['valor']});
        """
        try:
            cur.execute(insert_sql)
            conn.commit()
        except Exception as e:
            print(f"Error al insertar el registro {index}: {e}")
            conn.rollback()
    cur.close()
    conn.close()