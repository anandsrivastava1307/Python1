letter = '''Dear <|NAME|>,
You are selected! 
<|Date|>'''

print(letter.replace("<|NAME|>", "Anand").replace("<|Date|>", "18th May 2026"))