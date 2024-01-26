import sys

def report_argument_count():
    num_arguments = len(sys.argv) - 1  
    print(f"Number of arguments provided: {num_arguments}")

if __name__ == "__main__":
    report_argument_count()
