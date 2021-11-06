if __name__ == "__main__":
  res = {}
  with open("bible.txt", "r") as f:
    contents = f.read()
    contents = contents.split()
    for word in contents:
      if word in res:
        res[word] += 1
      else:
        res[word] = 1
  for key, value in res.items():
    print(f"{key}: {value}")