import sys
import time

from Container import Container
from Sorting import merge_sort


def main():
    if len(sys.argv) == 4:
        if sys.argv[1] == '-r':
            try:
                count = int(sys.argv[2])
            except ValueError:
                print("Incorrect input in the command line!")
                return 1
            c = Container()
            c.fill_randomly(count)
            output_file = open(sys.argv[3], "w+")
            c.write(output_file)
            c.container = merge_sort(c.container)
            output_file.write("\n")
            output_file.write("SORTED CONTAINER:\n\n")
            c.write(output_file)
        else:
            print("Incorrect input in the command line!")
            return 1
    elif len(sys.argv) == 3:
        try:
            input_file = open(sys.argv[1], "r")
        except IOError:
            print("Cannot open the input file!")
            return 1
        c = Container()
        try:
            c.read(input_file)
        except Exception as e:
            print("Incorrect data in the input file!\n")
            print(e.args)
            return 1
        output_file = open(sys.argv[2], "w+")
        c.write(output_file)
        c.container = merge_sort(c.container)
        output_file.write("\n")
        output_file.write("SORTED CONTAINER:\n\n")
        c.write(output_file)
    else:
        print("Incorrect input in the command line!")
        return 1


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Elapsed time: " + f"{time.time() - start_time}")
