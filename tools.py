from crewai_tools import ArxivPaperTool


tool = ArxivPaperTool(
    download_pdfs=True,
    save_dir="./arxiv_pdfs",
)