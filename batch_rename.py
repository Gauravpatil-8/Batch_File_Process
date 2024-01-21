import os

def rename(directory_path, new_name):
    count = 1
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found")

        for filename in os.listdir(directory_path):
            
            name, extension = os.path.splitext(filename)

           
            new_filename = f"{new_name}_{count}{extension}"

            old_filepath = os.path.join(directory_path, filename)
            new_filepath = os.path.join(directory_path, new_filename)

            os.rename(old_filepath, new_filepath)

            count += 1
            print(f"Changed {filename} to {new_filename}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

def main():
    directory = r"example/path" # Enter YOur path
    name = "example_name" #Enter your name
    rename(directory, name)

if __name__ == '__main__':
    main()
