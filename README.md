### Learn LLM with Python

- 1. Basic Python and Streamlit

<details>
<summary>2. Basic IO in python</summary>


- Reading file is easy, opening a file in write mode and write in it using `file.write('The content you wanna write')` will cause overwrite, so be careful

```python
with open('filename.txt','w') as file:
    file.write("Hey, I was the text that overworte Everything!")
```