# pipe example:
import multiprocessing
import multiprocessing.process

def sender(conn,msg):
    for i in msg:
        conn.send(i)
    conn.close()

def recieve(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)


if __name__ == "__main__":
    msg = ["my name is aneeqah","this is my message to students","i am in the class of multiprocessing"]
    parent_conn,child_conn = multiprocessing.Pipe()
    # pipe : Returns two connection object connected by a pipe
    m1 = multiprocessing.Process(target=sender, args=(child_conn,msg))
    m2 = multiprocessing.Process(target=recieve, args=(parent_conn,))
    m1.start()
    m2.start()

    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()

