# WordFlux 🌀
 
> **Translate DOCX using Google Gemini - Preserve Format**
 
WordFlux is a powerful and intelligent tool for translating Microsoft Word documents (.docx) using Google Gemini API while preserving the original formatting, structure, and layout completely.
<img width="1565" height="997" alt="image" src="https://github.com/user-attachments/assets/dc2ae795-75c4-4a63-a4ef-2fa29d12dcfb" />
 
 
 
 
## 🚀 Installation
 
### System Requirements
- Python 3.12+
- Google Gemini API key
 
### Install from pip
 
```bash
pip install wordflux
```

> **Note:** If you encounter `wordflux : The term 'wordflux' is not recognized` after installation, you may need to add Python's scripts directory to your system's PATH environment variable (e.g., `C:\Users\<Username>\AppData\Roaming\Python\Python31x\Scripts` on Windows).

### Install using uv (Recommended)

```bash
uv tool install wordflux
```
 
## 🏃‍♂️ How to Run

### Command Line Interface (CLI)

After installation and configuration (see below), you can run WordFlux directly from your terminal:

```bash
# Basic usage
uv run wordflux 1.docx
or
python -m wordflux.main 1.docx
or
wordflux input_document.docx

# Specify output directory
wordflux input_document.docx --output_dir my_translations
```

### 🔧 Configuration

To run the tool, you need to create a `config.yaml` file in your working directory.

```yaml
# Google Gemini Configuration
gemini_api_key: "your-gemini-api-key-here"  # Replace with your actual API key
model: "gemini-1.5-flash"

# Translation Settings
source_lang: "English"
target_lang: "Vietnamese"

# Performance Settings
max_concurrent: 100
max_chunk_size: 5000
```
 
### Manual dependency installation
 
```bash
pip install openai>=2.3.0 python-docx>=1.2.0 pyyaml>=6.0.3 tqdm>=4.67.1 google-genai>=0.1.0
```

### Supported Google Gemini Models
- `gemini-1.5-flash`
- `gemini-1.5-pro`
- And other Gemini models

## 📁 Project Structure

```
wordflux/
├── ⚙️ config.yaml            # Configuration
├── 📋 pyproject.toml         # Project metadata
├── 📖 README.md              # This documentation
├── 🗂️ output/               # Output directory for translated files
│   ├── document_translated.docx
│   └── document_checkpoint.json
└── 📦 wordflux/              # Main package
    ├── 📄 __init__.py
    ├── 📄 main.py            # Entry point
    ├── 🔧 docxtranslator.py  # Main class
    ├── 📄 document/          # Data models
    │   └── document.py
    ├── 🔨 worker/            # Core workers
    │   ├── extractor.py      # Extract content
    │   ├── translator.py     # Translate content
    │   └── injector.py       # Inject translations
    └── 🛠️ utils/             # Utilities
        ├── decorator.py      # Decorators (timer, retry, etc.)
        ├── is_numeric.py     # Helper functions
        ├── gemini_client.py  # Gemini client manager
        ├── prompt_builder.py # Build prompts
        └── spinner.py        # Loading spinner
```

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

## 👨‍💻 Author

**Pham Nguyen Ngoc Bao**
- 📧 Email: pnnbao@gmail.com
- 🐙 GitHub: [@pnnbao97](https://github.com/pnnbao97)
- 📘 Facebook: [pnnbao](https://www.facebook.com/pnnbao)

## 🙏 Acknowledgments

- Google Gemini API for powerful translation capabilities
- python-docx library for DOCX file processing
- Python community for supporting libraries

---

**WordFlux** - Smart document translation with perfect formatting preservation! 🌀✨
