import gzip
import shutil
import os


with open('logs\json_logger.log', 'rb') as f_in:
    with gzip.open('logs\json_logger.log.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

original_file_size = os.path.getsize('logs\json_logger.log')
gzip_file_size = os.path.getsize('logs\json_logger.log.gz')

compress_size = float(original_file_size - gzip_file_size)
compress_ratio = float(original_file_size - gzip_file_size) / float(original_file_size) * 100

print(f'original file size is {original_file_size} byte')
print(f'gzip file size is {gzip_file_size} byte')
print(f'compress size is {compress_size} byte')
print(f'compress ratio is {round(compress_ratio, 2)}%')
