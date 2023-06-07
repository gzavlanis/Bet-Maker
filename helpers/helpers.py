import schedule as s, time

# define the duration of connection
def duration_scheduler(connection, duration):
    start_time = time.time()
    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        connection.close()

# scheduling the connection
def connection_scheduler(connection, time):
    s.every(time).minutes.do(connection)