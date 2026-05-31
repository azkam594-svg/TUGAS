import menu.product_menu as products

from rich import print

def main():
    while True:
        print("[blue]=+= APPLICATION STORE MANAGEMENT =+=[/blue]")
        print("[yellow]1. Manage Products[/yellow]")
        print("[yellow]2. Manage Promotions[/yellow]")
        print("[yellow]3. Manage Finances[/yellow]")
        print("[yellow]4. Store Analytics[/yellow]")
        print("[yellow]0. Exit[/yellow]")
        choice = input("Select an option: ")

        if choice == '1':
            products.product_menu()
            
        elif choice == '2':
            print("Navigating to Promotion Management...")
            # Call promotion management function here
            
        elif choice == '3':
            print("Navigating to Finance Management...")
            # Call finance management function here
            
        elif choice == '4':
            print("Navigating to Analytics Management...")
            # Call analytics management function here
            
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
            
if __name__ == "__main__":
    main()  