import tensorflow as tf
import numpy as np
from PIL import Image

# Load the cover image
def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    return np.array(img)

# Save the steganographic image
def save_image(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

# Encode the secret message into the cover image
def encode_message(image, message):
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    binary_message += '1111111111111110'  # End of message delimiter
    
    data_index = 0
    binary_message_len = len(binary_message)

    for values in image:
        for pixel in values:
            for channel in range(0, 3):
                if data_index < binary_message_len:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

    return image

# Decode the secret message from the steganographic image
def decode_message(image):
    binary_message = ''
    for values in image:
        for pixel in values:
            for channel in range(0, 3):
                binary_message += format(pixel[channel], '08b')[-1]
    
    binary_message = [binary_message[i: i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    
    for byte in binary_message:
        if message[-16:] == '1111111111111110':
            break
        else:
            message += chr(int(byte, 2))
    
    return message[:-1]

# Example usage
cover_image_path = 'ball.jpg'
output_image_path = 'stego_image.png'
secret_message = "This is a secret message."

# Load cover image
cover_image = load_image(cover_image_path)

# Encode the secret message
stego_image = encode_message(cover_image, secret_message)

# Save the steganographic image
save_image(stego_image, output_image_path)

# Decode the secret message
decoded_message = decode_message(stego_image)

print("Decoded Message:", decoded_message)
