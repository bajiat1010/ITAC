import heapq
from collections import Counter

# Function to calculate how often each item appears
def get_item_frequencies(data):
    # Split the input into a list of items
    data = data.split()  
    # Count the frequency of each item
    item_count = dict(Counter(data))  
    return item_count

# Function to create a heap (priority queue) from item frequencies
def create_heap_from_frequencies(frequencies):
    # Create a heap list: each entry is [frequency, [item, "code"]]
    heap = [[count, [item, ""]] for item, count in frequencies.items()]
    heapq.heapify(heap)  # Make the list into a heap
    return heap

# Function to build the Huffman tree
def build_huffman_tree(heap):
    while len(heap) > 1:
        # Get the two items with the lowest frequencies
        item1 = heapq.heappop(heap)
        item2 = heapq.heappop(heap)

        # Add '0' to item1's code and '1' to item2's code
        for pair in item1[1:]:
            pair[1] = '0' + pair[1]
        for pair in item2[1:]:
            pair[1] = '1' + pair[1]

        # Combine the two items and add back to the heap
        heapq.heappush(heap, [item1[0] + item2[0]] + item1[1:] + item2[1:])
    
    return heap[0]

# Main loop to allow multiple inputs with continuation prompt
while True:
    # Get input data from user
    input_data = input("Enter data (numbers or characters separated by spaces): ")

    # Step 1: Get frequencies of items in the input
    item_frequencies = get_item_frequencies(input_data)

    # Step 2: Create a heap from the frequencies
    heap = create_heap_from_frequencies(item_frequencies)

    # Step 3: Build the Huffman tree from the heap
    huffman_tree = build_huffman_tree(heap)

    # Step 4: Print the Huffman codes for each item
    print("Huffman Codes:")
    for item in huffman_tree[1:]:
        print(item[0], '->', item[1])

    # Ask if the user wants to input values for another batch
    continue_outer = input("Do you want to input values for another batch? (yes/no): ").strip().lower()
    
    if continue_outer != 'yes':
        print("Exiting the program.")
        break  # Exit the loop if the user doesn't want to continue
