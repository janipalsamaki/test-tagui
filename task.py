import rpa as r


def task():
    r.init()
    r.url('https://www.robocorp.com')
    r.wait(5.0)
    r.snap('page', 'output/screenshot.png')
    r.close()


if __name__ == "__main__":
    task()
