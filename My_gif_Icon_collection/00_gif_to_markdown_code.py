import os
import sys

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
    
    markdown_content = create_markdown_links(directory)
    with open("output.md", "w") as file:
        file.write(markdown_content)

    input("Markdown content written to output.md.")
