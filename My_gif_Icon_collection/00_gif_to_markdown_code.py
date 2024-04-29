import os
import pyperclip
from collections import defaultdict

def create_markdown_links(directory):
    markdown_links = ""
    images_per_row = 3
    groups = defaultdict(list)
    index_links = ""

    # Group files based on the prefix and prepare index
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".gif"):
            group_name = filename.split("_")[0]
            gif_path = f"My_gif_Icon_collection/{filename}"
            link = f"<img src=\"{gif_path}\" alt=\"{filename}\" width=\"100\" /> [{filename}]({gif_path})"
            groups[group_name].append((filename, link))
    
    # Generate index
    for group_name in sorted(groups):
        index_links += f"- [{group_name}](#{group_name})\n"
        for gif_name, _ in sorted(groups[group_name], key=lambda x: x[0]):
            index_links += f"  - [{gif_name}]({group_name.lower()}_{gif_name.lower().replace(' ', '_').replace('.gif', '')})\n"
    
    # Generate Markdown for each group
    for group_name in sorted(groups):
        markdown_links += f"<h2 id='{group_name}'>{group_name}</h2>\n"
        items = sorted(groups[group_name], key=lambda x: x[0])
        image_count = 0
        for gif_name, item in items:
            markdown_links += f"<a id='{group_name.lower()}_{gif_name.lower().replace(' ', '_').replace('.gif', '')}'></a>" + item + " "
            image_count += 1
            if image_count % images_per_row == 0:
                markdown_links += "\n\n"
        if image_count % images_per_row != 0:
            markdown_links += "\n\n"

    return index_links + "\n" + markdown_links

if __name__ == "__main__":
    current_directory = os.getcwd()
    print(current_directory)
    current_directory = os.path.join(current_directory, "My_gif_Icon_collection")
    markdown_content = create_markdown_links(current_directory)
    pyperclip.copy(markdown_content)
    print(markdown_content)
    print("Markdown content copied to the clipboard.")
