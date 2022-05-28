class Vinamra_library:
    def __init__(self, list,name):
        self.bookslist=list
        self.bookname =name
        self.lendbook={}
        
    def displaybooks(self):
        print(f"we have the following of books: {self.bookname}")
    
    def lend_books(self,username,book):
        if book is self.lendbook.key():
            self.bookname.update({book:username})
            print("software is being updated. you can take book now.")
        else:
            print("sorry the book is being used by someone else")
    
    def add_book(self,book):
        self.booklist.append(book)
        print("book has been added suucessfully")
    
    def returnbook(self,book):
        self.bookslist.remove(book)
    
    if __name__ == '__main__':
        vinamra = Vinamra_library(['harry potter','3 men in a boat','sex in the city', '3 idiots'],"code with harry")
        
        while(True):
            print("welcome to the library.enter your chouce to continue .")  
            print("1.to display the books")
            print("2. to lend the book")                 
            print("3. to add the book")
            print("4. to return the book")
            
            user_choice=int(input())
            
            if user_choice == 1:
                vinamra.displaybooks()
            
            elif user_choice == 2:
                vinamra.lend_books()
            
            elif user_choice == 3:
                vinamra.addbooks()
            
            elif user_choice == 4:
                vinamra.returnbook()
                
            else:
                print("maa chuda")
                
                print("print q for quit and c for continue")
                

                
                while(user_choice2!="q" and user_choice!="c" ):
                    user_choice2 = input()
                    if user_choice2 == "q":
                        exit()
                    
                    elif user_choice2 == "c":
                        continue
                    