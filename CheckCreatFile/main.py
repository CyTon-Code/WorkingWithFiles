"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass


from DeleteFile.main import DeleteFile
from CheckFile.main import CheckFile

def CheckCreatFile(AddressFile):  # Check if the file is being created:
  """This module is required to create a file (or module)."""
  # Сredo: Checking the file for editable...
  
  if CheckFile(AddressFile):  # Если файл существует:
    return False
  
  #Решение проблемы с закрытием файлов, которые не открывались:
  FileOpen = True
  
  try:  # Создаю файл:
    File = open(AddressFile, 'x')
    return True
  
  except:  # Файл не создался:
    FileOpen = False
    return None
  
  finally:
    try:  # Закрываю файл:
      File.close()
      if DeleteFile(AddressFile) == None:  # Удаляю файл:
        raise ErrorClearFile

    except:  # Файл не закрылся:
      if FileOpen:  # If the file open:
        raise ErrorExitFile
