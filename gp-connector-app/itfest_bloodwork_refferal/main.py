from PIL import Image, ImageDraw, ImageFont

def write_text_on_image(image_path, output_path, text_positions):
    """
    Writes text on an image at specified positions.

    :param image_path: Path to the input image.
    :param output_path: Path where the output image will be saved.
    :param text_positions: A list of tuples, each containing the text to be written and its position (x, y).
    """
    # Open the image
    image = Image.open(r"C:\Users\andre\PycharmProjects\itfest_bloodwork_refferal\sample.jpg")

    # Prepare to draw on the image
    draw = ImageDraw.Draw(image)

    # Define a font (optional, you can also use the default font)
    try:
        # Try to use an existing TTF font file.
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        # If the specified font file is not found, fallback to the default font.
        font = ImageFont.load_default()

    # Loop through the text positions and draw the text on the image
    for text, position in text_positions:
        draw.text(position, text, font=font, fill=(255, 255, 255))  # Change fill color if needed

    # Save the image
    image.save(output_path)

# Example usage
text_positions = [("Hello, world!", (100, 100)), ("Another text here", (200, 200))]
write_text_on_image("sample.jpg", "sample_with_text.jpg", text_positions)




