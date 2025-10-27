import sys

def startstop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    wrapper()


def roll():
    print("Toczy się kulka po podłodze, toczy i toczy .......")



def main(args):
    startstop(roll)

if __name__ =="__main__":
    sys.exit(main(sys.argv))