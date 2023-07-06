def extract_example(text):
    # Split the text by 'Example:'
    parts = text.split('Example:')

    # If 'Example:' was found in the text
    if len(parts) > 1:
        # Return the text after 'Example:', stripped of leading/trailing whitespace
        return parts[1].strip()
    else:
        # If 'Example:' was not found in the text, return an empty string
        return ''


import re


def remove_false_and_none_lines(input_string):
    # Define a regular expression pattern to match lines with values None or false
    pattern = r'^\s*".*": (false|None|False|none),?\n'

    # Use the re.sub function to remove matching lines
    output_string = re.sub(pattern, '', input_string, flags=re.MULTILINE)

    return output_string


# # Test the function
# input_string = """
# {
#   "Contains Rational Numbers": true,
#   "Contains Complex Numbers": false,
#   "Contains Addition": true,
#   "Contains Subtraction": false,
#   "Contains Multiplication": true,
#   "Contains Division": false,
#   "Contains Exponents": false,
#   "Contains Roots": false,
#   "Contains Factorials": false,
#   "Contains Absolute Values": false,
#   "Number of Variables": 1,
#   "Number of Terms on Left Side": 2,
#   "Number of Terms on Right Side": 1,
#   "Degree": 1,
#   "Contains Trigonometric Functions": false,
#   "Contains Logarithmic Functions": false,
#   "Contains Exponential Functions": false,
#   "Contains Inequalities": false
# }
# """
#
# print(remove_false_and_none_lines(input_string))


def get_contents_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    contents = data.split("====NEW_QUESTION====")
    return [content.strip() for content in contents if content.strip()]

#
# filename = 'data/plq.txt'
# contents = get_contents_from_file(filename)
# for content in contents:
#     print(content)
#     print("====NEW_QUESTION====")
