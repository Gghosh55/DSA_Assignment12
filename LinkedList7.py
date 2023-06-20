def insert_nodes(first_list, second_list):


  first_node = first_list
  second_node = second_list
  while first_node and second_node:
    next_first = first_node.next
    next_second = second_node.next


    first_node.next = second_node
    second_node.next = next_first


    first_node = next_first
    second_node = next_second


  second_node.next = None

  return first_list


if __name__ == "__main__":
  first_list = create_linked_list([5, 7, 17, 13, 11])
  second_list = create_linked_list([12, 10, 2, 4, 6])

  new_list = insert_nodes(first_list, second_list)

  print_linked_list(new_list)
