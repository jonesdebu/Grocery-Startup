from grocery_list import GroceryList


def main():
    # Driver Code for grocery_list

    my_groceries = GroceryList()
    my_groceries.add('apple', 2)
    my_groceries.remove('apple')
    my_groceries.get_list()
    my_groceries.remove('pear')
    my_groceries.clear_list()
    my_groceries.clear_list()
    my_groceries.add('water')
    my_groceries.add('grapes', 5)
    my_groceries.get_list()
    my_groceries.get_item('water')
    my_groceries.get_item('soda')


if __name__ == '__main__':
    main()
