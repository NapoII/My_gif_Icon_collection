import os
import pyperclip

def create_markdown_links(directory):
    markdown_links = ""
    images_per_row = 3
    image_count = 0
    current_group = ""
    groups = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".gif"):
            group, _, file_name = filename.partition('_')
            if group != current_group:
                groups.append(group)
                current_group = group
            
            gif_path = f"My_gif_Icon_collection/{filename}"
            markdown_links += f"<img src=\"{gif_path}\" alt=\"{filename}\" width=\"100\" /> "
            markdown_links += f"[{filename}]({gif_path})  "
            image_count += 1
            
            if image_count == images_per_row:
                markdown_links += "\n\n"
                image_count = 0

    index_links = ""
    for group in groups:
        index_links += f"[{group.capitalize()}](#{group})  "
    
    markdown_content = ""
    if index_links:
        markdown_content += f"## Index\n\n{index_links}\n\n"
    markdown_content += markdown_links

    return markdown_content

if __name__ == "__main__":
    current_directory = os.getcwd()
    current_directory = os.path.join(current_directory, "My_gif_Icon_collection")
    markdown_content = create_markdown_links(current_directory)
    pyperclip.copy(markdown_content)

    print("Markdown content copied to the clipboard.")
