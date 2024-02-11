import os
import sys
import pyperclip

def create_markdown_links(directory):
    markdown_links = ""
    images_per_row = 3
    image_count = 0
    
    for filename in os.listdir(directory):
        if filename.endswith(".gif"):
            gif_path = os.path.join(directory, filename)
            markdown_links += f"<img src=\"{gif_path}\" alt=\"{filename}\" width=\"100\" /> "
            markdown_links += f"[{filename}]({gif_path})  "
            image_count += 1
            
            if image_count == images_per_row:
                markdown_links += "\n\n"
                image_count = 0

    return markdown_links

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
        directory = os.path.join(directory, "My_gif_Icon_collection")
        print("else",directory)
    
  
    markdown_content = create_markdown_links(directory)
    print(markdown_content)
    # Copy the Markdown content to the clipboard
    pyperclip.copy(markdown_content)
    
    print("Markdown content has been copied to the clipboard.")
