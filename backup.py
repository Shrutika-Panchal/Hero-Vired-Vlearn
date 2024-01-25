import shutil
import os
import sys

def copy_file(source_file, destination_file):

  try:
    shutil.copy2(source_file, destination_file)
  except IOError as e:
    print(e)

def main():

  if len(sys.argv) != 3:
    print("Usage: backup.py <source_directory> <destination_directory>")
    sys.exit(1)

  source_directory = sys.argv[1]
  destination_directory = sys.argv[2]

  if not os.path.exists(source_directory):
    print("The source directory does not exist.")
    sys.exit(1)

  if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

  for root, directories, files in os.walk(source_directory):
    for file in files:
      source_file = os.path.join(root, file)
      destination_file = os.path.join(destination_directory, file)

      if os.path.exists(destination_file):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destination_file = os.path.join(destination_directory, "%s_%s" % (file, timestamp))

      copy_file(source_file, destination_file)

if __name__ == "__main__":
  main()