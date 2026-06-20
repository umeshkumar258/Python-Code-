letter_template = '''
Dear <|Name|>,
You are selected!
Date: <|Date|>
'''

final_letter = letter_template.replace("<|Name|>", "Umesh")
final_letter = final_letter.replace("<|Date|>", "12 June 2026")
