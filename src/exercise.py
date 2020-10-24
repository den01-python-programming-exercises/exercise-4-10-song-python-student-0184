def main():
    #write your code below this line
    garden = Song("In The Garden", 10910)
    print("The song " + garden.name + " has a length of " + str(garden.length) + " seconds.")

if __name__ == '__main__':
    from song import Song
    main()
