import pickle


def main(args):
    pracownicy = {
    "Jan Kowalski"   : 668168555,
    "Anna Zwinna"    : 605123001,
    "Marek Ekspercki": 721003050,
    
    }
    print ("Słownik Pythona:", pracownicy)
    plik_out = open ("binarne1.bin","wb")
    pickle.dump(pracownicy, plik_out)
    plik_out.close()
    del pracownicy
    input("Zapisano do pliku, naciśnij Enter, aby sprawdzić wynik operacji: ")
    plik_in= open("binarne1.bin","rb")
    pracownicy_z_dysku = None
    pracownicy_z_dysku = pickle.load(plik_in)
    print ("Słownik odczytany z dysku:")
    print (pracownicy_z_dysku)
    plik_in.close()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

    """
    import pickle
    from dataclasses import dataclass

    @dataclass
    class User:
        name: str
        age: int
        email: str

    # Create custom objects
    users = [
        User("Alice", 30, "alice@example.com"),
        User("Bob", 25, "bob@example.com")
    ]

    # Save custom objects
    with open('users.pkl', 'wb') as file:
        pickle.dump(users, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Saved {len(users)} user objects")


    import pickle

# Open file in read-binary mode
    with open('important_data.pkl', 'rb') as file:
        # Load the pickled data
        data = pickle.load(file)

    print('Retrieved pickled data:')
    for i, item in enumerate(data):
        print(f'Data {i}: {item}')
 import pickle

# Load custom objects
    with open('users.pkl', 'rb') as file:
        users = pickle.load(file)

    print('Retrieved users:')
    for user in users:
        print(f"- {user.name} ({user.age}): {user.email}")       

"""