# Lex Lab Exercises 🚀

This repository contains **(Lab exercises)** as part of our Compiler Design Course, following the exercises given by our sir. All programs are structured, tested, and commented to help with lab preparation and understanding how Lex processes patterns efficiently.

---
## 💻 How to run the Lex programs

1️⃣ **Navigate to the folder:**
```bash
cd Basic Lex Files
```
2️⃣ **Run Lex on your .l file:**
```bash
lex filename.l
```
(or)

```bash
flex -o outputfilename.c filename.l
```
3️⃣ **Compile the generated C file:**
```bash
gcc outputfilename.c -ll -o output
```
4️⃣ **Run the program:**
```bash
./output
```
---
## 📌 Notes
- Press Ctrl+D (Linux/macOS) after input to signal end-of-input while testing interactive programs.
- You can also run with file input:
```bash
./output < input.txt
```
---
## 🛠️ Basic Lex Programs

The `basic Lex Files /` folder contains:

- Counting digits in a number.
- Counting spaces, tabs, and newlines.
- Validating identifiers.
- Converting lowercase letters to uppercase.
