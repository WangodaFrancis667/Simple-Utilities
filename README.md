# Simple-Utilities

A collection of simple Python scripts designed to automate common tasks and provide utility functions for everyday use. These scripts are open-source and freely available for public use, modification, and distribution.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Included](#scripts-included)
- [Contributing](#contributing)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Support](#support)

## 🔍 Overview

Simple-Utilities is a growing collection of Python scripts that help automate repetitive tasks and provide useful functionality for developers and end-users alike. Each script is designed to be standalone, easy to use, and well-documented.

## ✨ Features

- **Easy to Use**: Simple command-line interfaces for all scripts
- **Well Documented**: Clear documentation and examples for each utility
- **Cross-Platform**: Compatible with Windows, macOS, and Linux
- **Lightweight**: Minimal dependencies and fast execution
- **Open Source**: MIT licensed for free use and modification

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/WangodaFrancis667/Simple-Utilities.git
   cd Simple-Utilities
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**

   ```bash
   python Json-to-pdf.py --help
   ```

## 📖 Usage

Each script can be run independently. See the individual script documentation below for specific usage instructions.

### General Usage Pattern

```bash
python script_name.py [arguments]
```

### Example Usage

```bash
# Basic conversion
python Json-to-pdf.py --input test.json --output my_report.pdf

# With custom styling
python Json-to-pdf.py -i test.json -o report.pdf --title "Project Report" --author "Francis Wangoda" --color purple --pagesize letter

# Preview JSON first
python Json-to-pdf.py --input test.json --preview
```

## 📁 Scripts Included

### 1. Json-to-pdf.py

**Description**: Converts JSON data into formatted PDF documents with professional styling and full customization options.

**Features**:

- 🎨 **Customizable Styling**: Choose from 5 color themes (blue, red, green, purple, orange)
- 📄 **Multiple Page Sizes**: Support for A4 and Letter formats
- 🔧 **Flexible Configuration**: Custom titles, authors, margins, and font sizes
- 📊 **Automatic Table Generation**: Intelligently converts JSON arrays to formatted tables
- 🖥️ **Command-Line Interface**: Full CLI with help system and argument validation
- 👀 **JSON Preview**: Preview JSON structure before conversion
- 🌈 **Colorful Output**: Beautiful terminal interface with colored status messages
- 📈 **Currency Formatting**: Automatic formatting for financial data

**Basic Usage**:

```bash
# Simple conversion
python Json-to-pdf.py --input data.json --output report.pdf

# With custom styling
python Json-to-pdf.py -i data.json -o report.pdf --title "My Report" --author "John Doe" --color red

# Preview JSON structure first
python Json-to-pdf.py --input data.json --preview
```

**Advanced Options**:

```bash
# Full customization
python Json-to-pdf.py \
  --input data.json \
  --output custom_report.pdf \
  --title "Quarterly Report" \
  --author "Analytics Team" \
  --pagesize letter \
  --color purple \
  --margins 90 \
  --fontsize 14 \
  --spacing 1.2
```

**Available Arguments**:

- `--input, -i`: Input JSON file (required)
- `--output, -o`: Output PDF file
- `--title`: Document title
- `--author`: Document author
- `--pagesize`: Page size (A4, letter)
- `--color`: Color theme (blue, red, green, purple, orange)
- `--margins`: Page margins in points
- `--fontsize`: Base font size
- `--spacing`: Line spacing multiplier
- `--preview`: Preview JSON structure
- `--help`: Show help message
- `--version`: Show version info

**Dependencies**: `reportlab==4.0.4`

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **Suggest Features**: Propose new utilities or improvements to existing ones
3. **Submit Code**: Fork the repository and submit a pull request
4. **Improve Documentation**: Help make the documentation clearer and more comprehensive

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-utility`)
3. **Commit** your changes (`git commit -m 'Add amazing utility'`)
4. **Push** to the branch (`git push origin feature/amazing-utility`)
5. **Open** a Pull Request

### Code Standards

- Follow PEP 8 Python style guidelines
- Include docstrings for all functions and classes
- Add appropriate error handling
- Write unit tests for new functionality
- Update documentation as needed

## 🚧 Future Improvements

We're constantly working to improve Simple-Utilities. Here are some planned enhancements:

### Upcoming Features

- [ ] **File Management Utilities**
  - Bulk file renaming scripts
  - Directory organization tools
  - Duplicate file finder

- [ ] **Data Processing Scripts**
  - CSV to various format converters
  - Data cleaning utilities
  - Excel automation tools

- [ ] **System Utilities**
  - System monitoring scripts
  - Backup automation tools
  - Log file analyzers

- [ ] **Web Utilities**
  - URL shortener
  - Web scraping templates
  - API testing utilities

- [ ] **Enhanced Documentation**
  - Video tutorials
  - Interactive examples
  - API documentation

### Performance Improvements

- [ ] Add progress bars for long-running operations
- [ ] Implement parallel processing where applicable
- [ ] Add configuration file support
- [ ] Create GUI versions of popular scripts

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ **Commercial use** - You can use this software commercially
- ✅ **Modification** - You can modify the source code
- ✅ **Distribution** - You can distribute the software
- ✅ **Private use** - You can use the software privately
- ❗ **License and copyright notice** - Include the license and copyright notice with the code
- ❗ **No warranty** - The software is provided "as is" without warranty

## 🆘 Support

### Getting Help

- **Issues**: For bugs and feature requests, please use the [GitHub Issues](https://github.com/WangodaFrancis667/Simple-Utilities/issues) page
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/WangodaFrancis667/Simple-Utilities/discussions)
- **Email**: For direct support, contact `fwangoda@gmail.com`

### Troubleshooting

**Common Issues:**

1. **Import Errors**: Make sure all dependencies are installed via `pip install -r requirements.txt`
2. **Permission Errors**: Ensure you have write permissions in the output directory
3. **Python Version**: Verify you're using Python 3.6 or higher with `python --version`

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Special thanks to the open-source community for inspiration and support
- Built with ❤️ by [Francis Wangoda](https://github.com/WangodaFrancis667)

---

**Made with ❤️ for the community | © 2025 Francis Wangoda | MIT Licensed**
