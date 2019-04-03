import SLNode

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode.SLNode(val)
        current_head = self.head # Save the current head in a variable
        new_node.next = current_head # SET the new node's next TO the list's current head
        self.head = new_node # SET the list's head TO the node we created in the last step
        return self # Return self to allow for chaining

    def add_to_back(self, val):
        if(self.head == None):	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front

        new_node = SLNode.SLNode(val) # create a new instance of our Node class with the given value
        runner = self.head # set an iterator to start at the front of the list

        while (runner.next != None): # iterator until the iterator doesn't have a neighbor
            runner = runner.next # increment the runner to the next node in the list
            runner.next = new_node	# increment the runner to the next node in the list
            
        return self # return self to allow for chaining

    def print_values(self):
        runner = self.head  # a pointer to the list's first node

        while (runner != None): # iterating while runner is a node and not None
            print(runner.value) # print the current node's value
        runner = runner.next 	# set the runner to its neighbor

        return self    # return self to allow for chaining

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked Lists").add_to_back("fun!").print_values()
# output should be:
# Linked lists
# are
# fun!
