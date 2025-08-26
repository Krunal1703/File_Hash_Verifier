# File_Hash_Verifier
🔐 File Hash Verifier is a simple Python CLI tool that generates and verifies SHA256 (or other) hashes of files. It ensures file integrity by comparing computed hashes with known ones, helping detect tampering or corruption. Supports multiple algorithms and clean command-line usage.
## 🔧 Features

- Calculate SHA-256 hash of any file
- Compare against known hash to verify integrity
- Simple command-line interface (CLI)

## 🚀 How to Use

1. Clone the repository:
```bash
git clone https://github.com/Krunal1703/file-hash-verifier.git
cd file-hash-verifier

                        OR

1. Calculate a file’s hash:

    ```bash
    python hashverifier.py example/testfile.txt

2. you get has like {it is only for example}

        [INFO] SHA256 hash of example/testfile.txt:  
        e3b96d0dad8eb141a90bdc338c591a682a37600edba3bd9b0379e175e5eae95a

3. Then Compare with saved hash: 

        for example my hash file is like this: 
            echo "e3b96d0dad8eb141a90bdc338c591a682a37600edba3bd9b0379e175e5eae95a"

    I compare to my hash file vith test file:
        
        ```bash
        python hashverifier.py example/testfile.txt --compare e3b96d0dad8eb141a90bdc338c591a682a37600edba3bd9b0379e175e5eae95a
