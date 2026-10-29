# A Python script explaining Programming Language Paradigms
# Author: lipemlidjob | Course: Programming in Python | Date: 2026-10-29

paradigms = {
    "Procedural": "Step-by-step instructions. The code reads top to bottom. (Example: C)",
    "Object-Oriented (OOP)": "Modeling the world as objects with properties and methods. (Example: Java)",
    "Functional": "Computation as mathematical functions without changing state. (Example: Haskell)",
    "Low-Level": "Talking directly to the hardware memory and CPU. (Example: Assembly/C++)"
}

print("=== PROGRAMMING LANGUAGE PARADIGMS ===")
print("Author: ICT University Student\n")

# Loop through the dictionary and print each type
for lang_type, definition in paradigms.items():
    print(f"[{lang_type}]")
    print(f"Definition: {definition}\n")

print("=== END OF REPORT ===")
