def main():
    open("mars.jpg")
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
    #try:
    #    configuration = open('config.txt')
    #except FileNotFoundError:
    #    print("Couldn't find the config.txt file!")
    #except IsADirectoryError:
    #    print("Found config.txt but it is a directory, couldn't read it")
    #try:
    #    configuration = open('config.txt')
    #except Exception:
    #    print("Couldn't find the config.txt file!")
    #try:
    #    configuration = open('config.txt.')
    #except FileNotFoundError:
    #    print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()