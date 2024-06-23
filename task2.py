from PIL import Image
import numpy as np

# Function to encrypt an image using XOR
def encrypt_image(image_path, key):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Convert the image to RGB (if not already in that mode)
        img = img.convert('RGB')
        
        # Get the pixel values as a NumPy array of shape (height, width, 3)
        pixels = np.array(img)
        
        # Perform XOR encryption on each pixel value
        encrypted_pixels = pixels ^ key
        
        # Create a new PIL Image from the encrypted pixel data
        encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')
        
        # Save the encrypted image
        encrypted_image.save('encrypted_image.png')
        
        print(f'Image encrypted and saved as encrypted_image.png with key: {key}')
    
    except IOError:
        print(f"Unable to open image file: {image_path}")

# Function to decrypt an image using XOR
def decrypt_image(encrypted_image_path, key):
    try:
        # Open the encrypted image file
        encrypted_img = Image.open(encrypted_image_path)
        
        # Convert the image to RGB (if not already in that mode)
        encrypted_img = encrypted_img.convert('RGB')
        
        # Get the pixel values as a NumPy array of shape (height, width, 3)
        encrypted_pixels = np.array(encrypted_img)
        
        # Perform XOR decryption on each pixel value
        decrypted_pixels = encrypted_pixels ^ key
        
        # Create a new PIL Image from the decrypted pixel data
        decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')
        
        # Save the decrypted image
        decrypted_image.save('decrypted_image.png')
        
        print(f'Image decrypted and saved as decrypted_image.png with key: {key}')
    
    except IOError:
        print(f"Unable to open encrypted image file: {encrypted_image_path}")

# Example usage
if __name__ == '__main__':
    # Define a key for encryption (must be the same for encryption and decryption)
    encryption_key = np.array([255, 128, 64])  # Example key
    
    # Provide the image path directly in the script
    image_path = r'C:\Users\jagta\OneDrive\Pictures\Screenshots\Screenshot (1).png'
    
    # Encrypt the image
    encrypt_image(image_path, encryption_key)
    
    # Decrypt the encrypted image
    decrypt_image('encrypted_image.png', encryption_key)
