import os
import pyperclip

def create_markdown_links(directory):
    markdown_links = ""
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith(".gif"):
            gif_path = os.path.join(directory, filename)
            markdown_links += f"![{filename}]({gif_path})\n[{filename}]({gif_path})\n\n"
    return markdown_links

if __name__ == "__main__":
    current_directory = os.getcwd()
    current_directory =  os.path.join(current_directory , "My_gif_Icon_collection")
    markdown_content = create_markdown_links(current_directory)
    pyperclip.copy(markdown_content)

    print("Markdown content copied to clipboard.")
