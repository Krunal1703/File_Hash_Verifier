import hashlib
import argparse
import os

def calculate_sha256(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None

def compare_hash(file_hash, original_hash):
    """Compare two hashes and return match status."""
    if file_hash.lower() == original_hash.lower():
        print("[✅] Hashes match! File integrity verified.")
        return True
    else:
        print("[❌] Hashes do not match! File may be corrupted or modified.")
        return False

def main():
    parser = argparse.ArgumentParser(description="File Hash Verifier (SHA256)")
    parser.add_argument("file", help="Path to the file to hash")
    parser.add_argument("--compare", help="Original hash to compare with")
    args = parser.parse_args()

    file_hash = calculate_sha256(args.file)
    if file_hash:
        print(f"[INFO] SHA256 hash of {args.file}:")
        print(file_hash)

        if args.compare:
            compare_hash(file_hash, args.compare)

if __name__ == "__main__":
    main()
