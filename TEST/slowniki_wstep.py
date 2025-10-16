def main(args):
    doctorsWho = {
        "Pierwszy": "Wiliam Hartnell",
        "2": "Patrick Troughton",
        "3": "John Pertwee",
        "4": "Tom Baker",
        "5": "Peter Davison",
        "6": "Colin Baker",
        "7": "Sylvester McCoy",
        "8": "Paul McGann",
        "9": "Christopher Eccleston",
        "10": "David Tennant",
        "11": "Matt Smith",
        "12": "Peter Capaldi",
        "Trzynasta": "Jodie Whittaker",
    }
    print ("Kowalski" in doctorsWho)
    for key in doctorsWho:
        print (f"  {key}     -     {doctorsWho[key]}")
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))