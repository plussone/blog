import pymysql


def get_connect_mysql():
    """
    建立数据库连接
    :return: 连接, 游标
    """
    connect = pymysql.connect(host="localhost",
                              user="root",
                              password="gjy135136",
                              db="db_studydata",
                              charset="utf8")
    cursor = connect.cursor()
    return connect, cursor


def close_connect_mysql(connect: object, cursor: object) -> object:
    """
    关闭数据库连接
    :param connect: 连接
    :param cursor: 游标
    :return: None
    """
    cursor.close()
    connect.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql: sql语句
    :param args: 占位符参数
    :return: 返回查询到的结果, ((), ())的形式
    """
    connect, cursor = get_connect_mysql()
    cursor.execute(sql, args)
    connect.commit()
    res = cursor.fetchall()
    close_connect_mysql(connect, cursor)
    # print(res)
    return res


def insert(sql, *args):
    """
    封装通用插入
    :param sql: sql语句
    :param args: 占位符参数
    :return: none
    """
    connect, cursor = get_connect_mysql()
    cursor.execute(sql, args)
    connect.commit()
    close_connect_mysql(connect, cursor)


def checking_login(name, password):
    sql = "select password, uid " \
          "from username" \
          " where username={};"
    sql = sql.format("'" + name + "'")
    res = query(sql)
    if len(res) == 0:
        return 3, -1
    elif res[0][0] == password:
        return 1, res[0][1]
    else:
        return 2, -1


def add_data(date, a, b, c, d, e, f, g, h):
    sql = "select * " \
          "from data" \
          " where date='{}';"
    sql = sql.format(date)
    res = query(sql)
    if len(res) == 0:
        sql = "INSERT INTO data (date," \
              "uid,math_time,english_time,computer_time,politics_time,vocabulary_time,speak_time,listen_time,postscript) VALUES('{}'," \
              "'{}','{}','{}','{}','{}','{}','{}','{}','{}');"
        sql = sql.format(date, 1, a, b, c, d, e, f, g, h)
        insert(sql)
    else:
        arg = [a, b, c, d, e, f, g]
        for i in range(7):
            if int(arg[i]) <= 0:
                arg[i] = str(res[0][i + 2])
        h += res[0][9]
        sql = "UPDATE data SET math_time={}, english_time={}, " \
              "computer_time={}, politics_time={}, " \
              "vocabulary_time={}, speak_time={}, " \
              "listen_time={}, postscript='{}' " \
              "WHERE date='{}';"
        sql = sql.format(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], h, date)
        insert(sql)
    return 1


if __name__ == "__main__":
    print(1)
