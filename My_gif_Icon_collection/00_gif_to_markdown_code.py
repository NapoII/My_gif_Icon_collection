import os
import pyperclip
from collections import defaultdict

def replace_and_save(template_path, save_path, switch_str, var_str):
    try:
        # Read the content of the template file
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()
        
        # Replace the switch_str with var_str
        new_content = template_content.replace(switch_str, var_str)
        
        # Write the new content to the save_path file
        with open(save_path, 'w', encoding='utf-8') as save_file:
            save_file.write(new_content)
        
        print(f"Successfully replaced '{switch_str}' with '{var_str}' and saved to '{save_path}'.")
    
    except FileNotFoundError:
        print("Error: One or both of the files specified does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

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
        markdown_links += f"<h2 id='{group_name}'>{group_name}</h2>\n\n"
        items = sorted(groups[group_name], key=lambda x: x[0])
        image_count = 0
        for gif_name, item in items:
            markdown_links += f"<a id='{group_name.lower()}_{gif_name.lower().replace(' ', '_').replace('.gif', '')}'></a>" + item + "\n\n"
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
    print("Markdown content copied to the clipboard.")

    save_path = os.path.normpath(os.path.join(current_directory, "README.md"))
    template_path = os.path.normpath(os.path.join(current_directory, "READ_ME.template"))
    replace_and_save(template_path, save_path, "INPUT_STR", markdown_content)
