class My:
    print("Who wrote this?")
    index="Author-Book"
    def hand_list(self, philosopher, book):
        print(My.index)
        print(f"{philosopher} wrote the book: {book}")


myclass=My()
myclass.hand_list("Sun Tzu","The Art of War")