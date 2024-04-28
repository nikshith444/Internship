#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
text = "Python Exercises, PHP exercises."
pattern = "[ ,.]"
result = re.sub(pattern, ":", text)
print(result)


# In[2]:


import pandas as pd
data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)
def remove_special_characters(text):
    cleaned_text = re.sub(r'[^\w\s]|XXXXX', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()
df['SUMMARY'] = df['SUMMARY'].apply(remove_special_characters)

print(df)


# In[3]:


string = "I love to eat Biryani and Kebab."
pattern = re.compile(r'\b\w{4,}\b')
result = pattern.findall(string)
print(result)


# In[4]:


string = "He is a better cook than her"
pattern = re.compile(r'\b\w{3,5}\b')
result = pattern.findall(string)
print(result)


# In[5]:


def remove_parenthesis(text_list):
    pattern = re.compile(r'\([^()]*\)')
    cleaned_list = [pattern.sub('', text) for text in text_list]
    return cleaned_list
sample_text = ['"example (.com)"', '"hr@fliprobo (.com)"', '"github (.com)"', '"Hello (Data Science World)"', '"Data (Scientist)"']
output_text = remove_parenthesis(sample_text)
for text in output_text:
    print(text)


# In[6]:


text = '["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]'
pattern = r'\([^()]*\)'
result = re.sub(pattern, '', text)
print(result)


# In[7]:


text = "ImportanceOfRegularExpressionsInPython"
pattern = r"[A-Z][^A-Z]+"
results = re.findall(pattern, text)
print(results)


# In[8]:


text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = re.sub(r'(\D)(\d)', r'\1 \2', text)
print(result)


# In[9]:


text = "RegularExpression1IsAn2ImportantTopic3InPython"
pattern = re.findall(r'[A-Z][a-z]*|\d+', text)
result = ' '.join(pattern)
print(result)


# In[10]:


import pandas as pd
url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])
print(df['first_five_letters'])


# In[11]:


def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'You are right!'
        else:
                return('You are wrong!')

print(text_match("Myself 444."))
print(text_match("Myself_444"))


# In[12]:


def match_num(string):
    text = re.compile(r"^4")
    if text.match(string):
        return 'Correct'
    else:
        return 'Incorrect'
print(match_num('468540'))
print(match_num('546854'))


# In[13]:


ip = "192.004.101.010"
result = re.sub('\.[0]*', '.', ip)
print(result)


# In[14]:


file_path = r'C:\Users\Nik\Pictures\Screenshots\sample_text.txt'
with open(file_path, 'r') as file:
    text = file.read()
pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b'
matches = re.findall(pattern, text)
for match in matches:
    print("Matched date:", match)


# In[15]:


def search_strings(text, searched_words):
    for word in searched_words:
        if re.search(r'\b' + re.escape(word) + r'\b', text):
            print(f"'{word}' found.")
        else:
            print(f"'{word}' not found.")
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
search_strings(sample_text, searched_words)


# In[16]:


def search_string_with_location(text, searched_word):
    match = re.search(re.escape(searched_word), text)
    if match:
        start_index = match.start()
        end_index = match.end()
        print(f"'{searched_word}' found between index {start_index} to {end_index - 1}.")
    else:
        print(f"'{searched_word}' not found.")

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_word = 'fox'

search_string_with_location(sample_text, searched_word)


# In[17]:


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
matches = re.finditer(pattern, text)
substrings = [match.group(0) for match in matches]
print(substrings)


# In[18]:


def find_occurrences_and_positions(main_string, sub_string):
    occurrences = []
    start = 0
    while True:
        start = main_string.find(sub_string, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences

def main():
    main_string = "Python is a powerful programming language. Python is also easy to learn."
    sub_string = "Python"
    positions = find_occurrences_and_positions(main_string, sub_string)
    if positions:
        print("Substring '{}' found at positions: {}".format(sub_string, positions))
    else:
        print("Substring '{}' not found in the main string.".format(sub_string))

if __name__ == "__main__":
    main()


# In[19]:


def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2020-03-22"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[20]:


text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = re.compile(r'\b\d+\.\d{1,2}\b')
result = pattern.findall(text)
print(result)


# In[21]:


def separate_numbers_and_positions(string):
    numbers = []
    positions = []
    
    for i, char in enumerate(string):
        if char.isdigit():
            numbers.append(char)
            positions.append(i)
    
    return numbers, positions

def main():
    sample_string = "There are 10 apples and 5 oranges on the table."
    numbers, positions = separate_numbers_and_positions(sample_string)
    print("Numbers:", numbers)
    print("Positions:", positions)

if __name__ == "__main__":
    main()


# In[22]:


string = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
values = re.findall(r'\d+', string)
max_value = max(values)
print(max_value)


# In[23]:


text = "RegularExpressionIsAnImportantTopicInPython"
pattern = r'([A-Z][a-z]+)'
result = re.sub(pattern, r' \1', text)
print(result)


# In[24]:


pattern = r'[A-Z][a-z]+'
text = "Virat Kohli is better than Babar Azam"

matches = re.findall(pattern, text)
print(matches)


# In[25]:


text = "Hello hello world world"
pattern = r'\b(\w+)(\s+\1\b)+'
result = re.sub(pattern, r'\1', text)
print(result)


# In[26]:


def ends_with_alphanumeric(input_string):
    pattern = r'.*[a-zA-Z0-9]$' 
    if re.match(pattern, input_string):
        return True
    else:
        return False
test_strings = ["nik444", "viru", "mahi7789", "vk18", "tanu__"]
for string in test_strings:
    if ends_with_alphanumeric(string):
        print(f"{string} ends with an alphanumeric character.")
    else:
        print(f"{string} does not end with an alphanumeric character.")


# In[27]:


text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'
hashtags = re.findall(r'#\w+', text)
print(hashtags)


# In[28]:


text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
pattern = r"<U\+\w{4}>"
result = re.sub(pattern, "", text)
print(result)


# In[31]:


def extract_dates_from_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
        return dates

def main():
    file_path = r"C:\Users\Nik\Pictures\Screenshots\simple_text.txt"
    dates = extract_dates_from_text(file_path)
    
    if dates:
        print("Dates extracted from the text:")
        for date in dates:
            print(date)
    else:
        print("No dates found in the text.")

if __name__ == "__main__":
    main()


# In[30]:


text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern = re.compile(r'\b\w{2,4}\b')
result = re.sub(pattern, '', text)
print(result)


# In[ ]:




