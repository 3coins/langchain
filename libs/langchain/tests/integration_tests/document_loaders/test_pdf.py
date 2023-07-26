from pathlib import Path

from langchain.document_loaders import (
    MathpixPDFLoader,
    PDFMinerLoader,
    PDFMinerPDFasHTMLLoader,
    PyMuPDFLoader,
    PyPDFium2Loader,
    PyPDFLoader,
    UnstructuredPDFLoader,
)
from langchain.document_loaders.pdf import AmazonTextractPDFLoader


def test_unstructured_pdf_loader_elements_mode() -> None:
    """Test unstructured loader with various modes."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = UnstructuredPDFLoader(str(file_path), mode="elements")
    docs = loader.load()

    assert len(docs) == 2


def test_unstructured_pdf_loader_paged_mode() -> None:
    """Test unstructured loader with various modes."""
    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = UnstructuredPDFLoader(str(file_path), mode="paged")
    docs = loader.load()

    assert len(docs) == 16


def test_unstructured_pdf_loader_default_mode() -> None:
    """Test unstructured loader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = UnstructuredPDFLoader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1


def test_pdfminer_loader() -> None:
    """Test PDFMiner loader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = PDFMinerLoader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = PDFMinerLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 1


def test_pdfminer_pdf_as_html_loader() -> None:
    """Test PDFMinerPDFasHTMLLoader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = PDFMinerPDFasHTMLLoader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = PDFMinerPDFasHTMLLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 1


def test_pypdf_loader() -> None:
    """Test PyPDFLoader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = PyPDFLoader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = PyPDFLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 16


def test_pypdfium2_loader() -> None:
    """Test PyPDFium2Loader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = PyPDFium2Loader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = PyPDFium2Loader(str(file_path))

    docs = loader.load()
    assert len(docs) == 16


def test_pymupdf_loader() -> None:
    """Test PyMuPDF loader."""
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = PyMuPDFLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 1

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = PyMuPDFLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 16
    assert loader.web_path is None

    web_path = "https://people.sc.fsu.edu/~jpeterson/hello_world.pdf"
    loader = PyMuPDFLoader(web_path)

    docs = loader.load()
    assert loader.web_path == web_path
    assert loader.file_path != web_path
    assert len(docs) == 1


def test_mathpix_loader() -> None:
    file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    loader = MathpixPDFLoader(str(file_path))
    docs = loader.load()

    assert len(docs) == 1
    print(docs[0].page_content)

    file_path = Path(__file__).parent.parent / "examples/layout-parser-paper.pdf"
    loader = MathpixPDFLoader(str(file_path))

    docs = loader.load()
    assert len(docs) == 1
    print(docs[0].page_content)

# def test_amazontextract_loader() -> None:
    # file_path = "https://amazon-textract-public-content.s3.us-east-2.amazonaws.com/langchain/alejandro_rosalez_sample_1.jpg"
    # loader = AmazonTextractPDFLoader(str(file_path))
    # docs = loader.load()
    # print(docs)

    # assert len(docs) == 1

    # file_path = Path(__file__).parent.parent / "examples/hello.pdf"
    # loader = AmazonTextractPDFLoader(str(file_path))
    # docs = loader.load()

    # assert len(docs) == 1

    # import boto3
    # textract_client = boto3.client('textract', region_name='us-east-2')

    # file_path = "s3://amazon-textract-public-content/langchain/layout-parser-paper.pdf"
    # loader = AmazonTextractPDFLoader(str(file_path), boto3_textract_client=textract_client)

    # docs = loader.load()
    # assert len(docs) == 16
