# Handling Exceptions with the Context Manager

class DummyContext:
    def __init__(self, host, port, timeout=None):
        self.conn = create_conn(host, port, timeout=timeout)

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        return False


with DummyContext(host, port, timeout=None) as conn:
    try:
        conn.send_text("Hello Python!")


    except Exception as e:
        print(f'Unable to use connection : {e}')
 	