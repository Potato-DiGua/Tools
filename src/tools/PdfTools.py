from typing import List

from PyPDF2 import PdfFileMerger


def merge_pdf(pdf_path: List[str], output_path: str):
    files = [item for item in pdf_path if str(item).endswith(".pdf")]

    file_merger = PdfFileMerger()

    for pdf in files:
        file_merger.append(pdf)  # 合并pdf文件

    file_merger.write(output_path)
    print("[" + ",".join(pdf_path) + "]" + "->" + output_path)
