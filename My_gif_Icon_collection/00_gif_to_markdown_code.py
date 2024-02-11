import os
import pyperclip

def create_markdown_links(directory):
    markdown_links = ""
    images_per_row = 3
    image_count = 0
    
    for filename in os.listdir(directory):
        if filename.endswith(".gif"):
            gif_path = f"My_gif_Icon_collection/{filename}"
            markdown_links += f"<img src=\"{gif_path}\" alt=\"{filename}\" width=\"100\" /> "
            markdown_links += f"[{filename}]({gif_path})  "
            image_count += 1
            
            if image_count == images_per_row:
                markdown_links += "\n\n"
                image_count = 0

    return markdown_links

if __name__ == "__main__":
    current_directory = os.getcwd()
    current_directory = os.path.join(current_directory, "My_gif_Icon_collection")
    markdown_content = create_markdown_links(current_directory)
    pyperclip.copy(markdown_content)

    print("Markdown content copied to the clipboard.")
