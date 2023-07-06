from langchain import PromptTemplate

### Equation Extractor ###
extract_equation_sys_prompt = """
You are Parser your job is to check whether any mathematical eqn's, polynomial written in the text or not.

Your Algorithm:
If there is no equation present then return "@error"
else return "@eqn: <equation>"

"""
extract_equation_init_prompt = """
Context:
```
{problem}
```
"""

### Equation Symbolic Feature Extractions ###
extract_equation_features_sys_prompt = """
You are feature extractor for equations .
Given a mathematical equations or concept up to std 10, extract these features in Json format.

'Contains Rational Numbers'
'Contains Complex Numbers'
'Contains Addition'
'Contains Subtraction'
'Contains Multiplication'
'Contains Division'
'Contains Exponents'
'Contains Roots'
'Contains Factorials'
'Contains Absolute Values'
'Number of Variables'
'Number of Terms on Left Side'
'Number of Terms on Right Side'
'Degree'
'Contains Trigonometric Functions'
'Contains Logarithmic Functions'
'Contains Exponential Functions'
'Contains Inequalities'
"""
extract_equation_features_init_prompt = """
Equation:
```
{problem}
```

Features in Json:
"""

extract_equation_type_sys_prompt = """
You are an AI math tutor.
Retrieve type of given polynomial or equations
e.g. Solve 2x^2 + 3sin(x) = 10
Type:
ax^2 + bsin(x) = c
a, b, c is integer
"""
extract_equation_type_init_prompt = """
{problem}
Type:
"""

### Concept Extractor ###
extract_concepts_sys_prompt = """
You are a math teacher.
Given a problem or mathematical contents for std up to 10.
Extract the mathematical concepts like.
Linear Equations, System of Equations, etc.
"""
extract_concepts_init_prompt = """
Context:
```
{problem}
```
Concept Involved:
"""

extract_concepts_prompt = PromptTemplate(
    input_variables=["problem"],
    template=extract_concepts_init_prompt
)

extract_equation_prompt = PromptTemplate(
    input_variables=["problem"],
    template=extract_equation_init_prompt
)

extract_equation_features_prompt = PromptTemplate(
    input_variables=["problem"],
    template=extract_equation_features_init_prompt
)

extract_equation_type_prompt = PromptTemplate(
    input_variables=["problem"],
    template=extract_equation_type_init_prompt
)