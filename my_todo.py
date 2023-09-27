import dbHelper

def main():
    run=1
    dbHelper.createtable()

    while run:
        print('\n')
        print("enter your option")
        print("1.insert the task")
        print("2.show all tasks")
        print("3.delete task")
        print("4.close")
        x = str(input("Enter the above any option"))

        if x=="1":
            task = str(input("Enter the task name:"))
            dbHelper.insertdata(task)

        elif x=="2":
            dbHelper.displaydata()

        elif x=="3":
            index = int(input("enter the id to delete"))
            dbHelper.deletedata(index)
        elif x=="4":
            run=0
        else:
            print("please enter the correct option")

    dbHelper.close()

    
if __name__=='__main__':
    main()