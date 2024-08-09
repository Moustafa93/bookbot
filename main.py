def main():
  path = "books/frankenstein.txt" 
  print(f"--- Begin report of {path} ---")
  
  try:
    text = get_text(path)
  except:
    print("Failed top open file: abort")
    return

  words_count = count_words(text)
  print(f"There are {words_count} words in the text")

  chars_dict = count_chars(text)
  sorted = sort_dict(chars_dict)

  for ch in sorted:
    print(f"The '{ch['character']}' character was found {ch['count']} times")

  print("--- End report ---")

def get_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())

def count_chars(text):
  count = {}
  for ch in text:
    ch = ch.lower()
    if ch in count:
      count[ch] += 1
    else:
      count[ch] = 1 
  return(count)

def sort_dict(dict):
  dict_list = []
  for ch in dict:
    if ch.isalpha():
      dict_list.append({"character": ch, "count": dict[ch]})
  dict_list.sort(reverse=True, key=lambda d: d["count"])
  return dict_list

if __name__ == "__main__":
  main()