"""
Comprehensive TextWrap Module Demo
==================================

This file demonstrates all the key functions of Python's textwrap module
with practical examples and explanations.
"""

import textwrap

print("=" * 60)
print("TEXTWRAP MODULE DEMONSTRATION")
print("=" * 60)

# Sample text for demonstrations
long_text = "Python is an amazing programming language that is widely used for web development, data science, artificial intelligence, automation, and many other applications. It's known for its simple syntax and powerful libraries."

messy_indented_text = """
    This text has inconsistent indentation.
        Some lines are indented more than others.
    This makes it hard to read and format properly.
        We can use textwrap.dedent() to fix this!
"""

# 1. TEXTWRAP.WRAP() - Break text into list of lines
print("\n1. TEXTWRAP.WRAP() - Break text into lines")
print("-" * 50)
wrapped_lines = textwrap.wrap(long_text, width=40)
print("Original text:")
print(f"'{long_text}'")
print(f"\nWrapped into lines of max 40 characters:")
for i, line in enumerate(wrapped_lines, 1):
    print(f"Line {i}: '{line}'")

# 2. TEXTWRAP.FILL() - Wrap and return as single string
print("\n\n2. TEXTWRAP.FILL() - Wrap and return as single string")
print("-" * 50)
filled_text = textwrap.fill(long_text, width=50)
print("Filled text (width=50):")
print(filled_text)

# 3. TEXTWRAP.DEDENT() - Remove common leading whitespace
print("\n\n3. TEXTWRAP.DEDENT() - Remove common indentation")
print("-" * 50)
print("Before dedent:")
print(repr(messy_indented_text))
print("\nAfter dedent:")
dedented_text = textwrap.dedent(messy_indented_text)
print(repr(dedented_text))
print("\nHow it looks when printed:")
print(dedented_text)

# 4. TEXTWRAP.INDENT() - Add prefix to each line
print("\n4. TEXTWRAP.INDENT() - Add prefix to lines")
print("-" * 50)
sample_code = """def greet(name):
    return f"Hello, {name}!"

print(greet("World"))"""

indented_code = textwrap.indent(sample_code, "    ")  # Add 4 spaces
print("Original code:")
print(sample_code)
print("\nIndented with 4 spaces:")
print(indented_code)

# You can also use custom prefixes
comment_style = textwrap.indent(sample_code, "# ")
print("\nWith comment prefix:")
print(comment_style)

# 5. TEXTWRAP.SHORTEN() - Truncate text with ellipsis
print("\n\n5. TEXTWRAP.SHORTEN() - Truncate with ellipsis")
print("-" * 50)
shortened = textwrap.shorten(long_text, width=50)
print(f"Original length: {len(long_text)} characters")
print(f"Shortened to 50 chars: '{shortened}'")

# Different placeholder
shortened_custom = textwrap.shorten(long_text, width=60, placeholder=" [READ MORE]")
print(f"Custom placeholder: '{shortened_custom}'")

# 6. PRACTICAL EXAMPLE - Formatting a help message
print("\n\n6. PRACTICAL EXAMPLE - Help Message Formatting")
print("-" * 50)

def format_help_message():
    help_text = """
    Welcome to the Tea Shop Management System!
    
    Available commands:
        add-tea: Add a new tea to inventory
        list-teas: Display all available teas
        update-price: Update tea pricing
        generate-report: Create sales report
    
    For more information, visit our documentation at https://teashop.example.com/docs
    """
    
    # Clean up the indentation
    clean_text = textwrap.dedent(help_text).strip()
    
    # Add consistent indentation
    formatted = textwrap.indent(clean_text, "  ")
    
    return formatted

print("Formatted help message:")
print(format_help_message())

# 7. REAL-WORLD EXAMPLE - Code documentation formatter
print("\n\n7. REAL-WORLD EXAMPLE - Code Documentation")
print("-" * 50)

def format_docstring(func_name, description, params, returns):
    """Format a function docstring with proper indentation and wrapping."""
    
    doc_template = f'''
    def {func_name}():
        """
        {description}
        
        Parameters:
        {params}
        
        Returns:
        {returns}
        """
        pass
    '''
    
    # Remove extra indentation
    clean_doc = textwrap.dedent(doc_template).strip()
    
    # Wrap long lines in the description
    lines = clean_doc.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.strip().startswith('"""') or line.strip() == '':
            formatted_lines.append(line)
        elif 'def ' in line or 'pass' in line:
            formatted_lines.append(line)
        else:
            # Wrap content lines
            wrapped = textwrap.fill(line.strip(), width=60)
            # Add proper indentation back
            indented = textwrap.indent(wrapped, "        ")
            formatted_lines.append(indented)
    
    return '\n'.join(formatted_lines)

example_doc = format_docstring(
    "calculate_tea_price",
    "This function calculates the total price for tea orders including taxes, discounts, and shipping fees. It handles multiple tea types and quantities.",
    "tea_type (str): Type of tea to order\nquantity (int): Number of tea bags\ndiscount (float): Discount percentage",
    "float: Total price including all fees and taxes"
)

print("Generated function documentation:")
print(example_doc)

print("\n" + "=" * 60)
print("END OF TEXTWRAP DEMONSTRATION")
print("=" * 60)
