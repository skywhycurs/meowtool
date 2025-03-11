import os

def system():
  pc = input("выбери свою систему: \n  1.Linux \n  2.Termux \n")
  if pc == 1:
      os.system("pip install -r requiments.txt")
      print("в последующих запусках используйте: python3 main.py")
      
  if pc == 2:
      os.system("pip install -r requiments.txt")
      print("в последующих запусках используйте: python3 main.py")
      
                

if __name__ == "__main__":
  system()
  print("приятного использования")
  os.system("python3 main.py")
  
