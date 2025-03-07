import zipfile
import binascii
import os
import hashlib

def zip_to_hash(zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            
            for info in zip_file.infolist():
               
                filename = info.filename
                crc32 = f"{info.CRC:08x}"  
                compressed_size = info.compress_size
                uncompressed_size = info.file_size

                print(f"Processing file: {filename}")
                print(f"CRC32: {crc32}")
                print(f"Compressed size: {compressed_size}")
                print(f"Uncompressed size: {uncompressed_size}")

                hash_string = (
                    f"$zip2$*0*3*0*{crc32}*{compressed_size:x}*{uncompressed_size:x}*"
                    f"{binascii.hexlify(zip_file.read(filename)).decode()}*"
                )
                print(f"Generated hash: {hash_string}")
                return hash_string

    except FileNotFoundError:
        print(f"Error: The file '{zip_file_path}' was not found.")
    except zipfile.BadZipFile:
        print(f"Error: The file '{zip_file_path}' is not a valid ZIP archive.")
    except Exception as e:
        print(f"An error occurred: {e}")


zip_file = '/path/to/your/file.zip'  
hash_result = zip_to_hash(zip_file)

if hash_result:
    print(f"The generated hash for the ZIP file is:\n{hash_result}")
