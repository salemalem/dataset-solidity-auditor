import os

def shorten_filename(filename, existing_names):
    # Define your logic to shorten the filename here
    # This is a simple example that trims the filename to the first 5 characters
    name, ext = os.path.splitext(filename)
    short_name = name[:5]

    # Ensure the new name is unique
    counter = 1
    new_name = short_name + ext
    while new_name in existing_names:
        new_name = f"{short_name}_{counter}{ext}"
        counter += 1

    return new_name

def shorten_filenames_in_directory(directory):
    existing_names = set(os.listdir(directory))
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = shorten_filename(filename, existing_names)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            existing_names.add(new_name)
            print(f"Renamed '{filename}' to '{new_name}'")

# Use the current directory or specify any directory you want
current_directory = os.getcwd()
shorten_filenames_in_directory(current_directory)
