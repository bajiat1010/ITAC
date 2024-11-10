def calculate_parity_bits(data_bits): 
    # Place data bits in positions 3, 5, 6, and 7 
    d3, d5, d6, d7 = map(int, data_bits) 
    # Calculate parity bits for even parity 
    # P1 covers positions 1, 3, 5, 7 
    p1 = (d3 + d5 + d7) % 2 
    # P2 covers positions 2, 3, 6, 7 
    p2 = (d3 + d6 + d7) % 2 
    # P4 covers positions 4, 5, 6, 7 
    p4 = (d5 + d6 + d7) % 2 
 
    # Return the encoded message 
    hamming_code = f"{p1}{p2}{d3}{p4}{d5}{d6}{d7}" 
    return hamming_code 
 
def detect_and_correct_error(received_data): 
    # Convert the received data to a list of integers for easier manipulation 
    received_bits = list(map(int, received_data)) 
 
    # Check parity for P1, P2, and P4 
    p1_check = (received_bits[0] + received_bits[2] + received_bits[4] + received_bits[6]) % 2 
    p2_check = (received_bits[1] + received_bits[2] + received_bits[5] + received_bits[6]) % 2 
    p4_check = (received_bits[3] + received_bits[4] + received_bits[5] + received_bits[6]) % 2 
 
    # Calculate the syndrome (error position) 
    error_position = p1_check * 1 + p2_check * 2 + p4_check * 4 
 
    if error_position == 0: 
        return "No error detected", received_data  # No error 
    else: 
        # Correct the error at the error_position 
        print(f"Error detected at position {error_position}. Correcting it.") 
        received_bits[error_position - 1] = 1 - received_bits[error_position - 1]  # Flip the erroneous bit 
        return "Error detected and corrected", received_bits 
 
# Example usage 
data_bits = "1011"  # Data bits to encode 
print(f"Data: {data_bits}") 
 
# Calculate the encoded message (Hamming code) 
encoded_data = calculate_parity_bits(data_bits) 
print(f"Encoded Data: {encoded_data}")
# Simulate a transmission with an error (let's say bit 6 has an error) 
received_data_with_error = "0110111"  # This is the received data with a single-bit error 
print(f"Received Data (with error): {received_data_with_error}") 
# Detect and correct errors 
status, corrected_data = detect_and_correct_error(received_data_with_error) 
print(status) 
print(f"Corrected Data: {''.join(map(str, corrected_data))}") 
