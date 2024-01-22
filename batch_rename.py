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

def count_files(directory_path):
    try:
           
            if not os.path.exists(directory_path):
                raise FileNotFoundError(f"Directory not found: {directory_path}")

            file_count = 0

          
            for dirpath, dirnames, filenames in os.walk(directory_path):
              
                file_count += len(filenames)

            print(f"Number of files (including subdirectories) in {directory_path}: {file_count}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def batch_remove(directory_path):
    data_directory=directory_path
    image_extensions=["jpg","jpeg","png","bmp"]
    for image_class in os.listdir(directory_path):
        for image in os.listdir(os.path.join(data_directory,image_class)):
            image_path=os.path.join(data_directory,image_class,image)
            extension=image_path.split('.')[-1]
            if extension not in image_extensions:
                os.remove(image_path)


def main():
    directory = r"C:\imageclassifierdataset" # Enter YOur path
    name = "Wood" #Enter your name
    # rename(directory,name)
    count_files(directory)
    # batch_remove(directory)

if __name__ == '__main__':
    main()
