from context import VietArchive
from VietArchive import utils

test_str = "Xin chào! \n Tôi tên là Nguyễn Văn A."
output_str = utils.text_normalization(test_str)
print(f"Origin string: {test_str}")
print(f"Normalized string: {output_str}")
