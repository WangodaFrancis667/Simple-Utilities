import json
import argparse
import sys
import os
from typing import Dict, List, Any, Optional
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

def format_currency(amount: float) -> str:
    """Format currency with commas"""
    return f"{amount:,}"

def print_colorful_banner():
    """Print a colorful banner with application info"""
    banner = """
\033[96m╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                              ║
║    \033[93m ██╗ ███████╗  ██████╗  ███╗   ██╗    ████████╗  ██████╗     ██████╗  ██████╗  ███████╗\033[96m   ║
║    \033[93m ██║ ██╔════╝ ██╔═══██╗ ████╗  ██║    ╚══██╔══╝ ██╔═══██╗    ██╔══██╗ ██╔══██╗ ██╔════╝\033[96m   ║
║    \033[93m ██║ ███████╗ ██║   ██║ ██╔██╗ ██║       ██║    ██║   ██║    ██████╔╝ ██║  ██║ █████╗  \033[96m   ║
║    \033[93m ██║ ╚════██║ ██║   ██║ ██║╚██╗██║       ██║    ██║   ██║    ██╔═══╝  ██║  ██║ ██╔══╝  \033[96m   ║
║    \033[93m ██║ ███████║ ╚██████╔╝ ██║ ╚████║       ██║    ╚██████╔╝    ██║      ██████╔╝ ██║     \033[96m   ║
║    \033[93m ╚═╝ ╚══════╝  ╚═════╝  ╚═╝  ╚═══╝       ╚═╝     ╚═════╝     ╚═╝      ╚═════╝  ╚═╝     \033[96m   ║
║                                                                                                              ║
║    \033[95mProfessional JSON to PDF Converter By Wangoda Francis -> fwangoda@gmail.com\033[96m               ║
║            \033[94mv2.0 - Enhanced & Customizable\033[96m                                                    ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝\033[0m
    """
    print(banner)

def print_menu():
    """Print a colorful menu with options"""
    menu = """
\033[92m┌─────────────────────────────────────────────────────────────┐
│                         \033[95mAVAILABLE OPTIONS\033[92m                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  \033[93m📄 INPUT OPTIONS:\033[92m                                          │
│    • \033[96m--input\033[92m      : Specify JSON input file                   │
│    • \033[96m--output\033[92m     : Specify PDF output file                   │
│                                                             │
│  \033[93m🎨 CUSTOMIZATION OPTIONS:\033[92m                                   │
│    • \033[96m--title\033[92m      : Custom document title                     │
│    • \033[96m--author\033[92m     : Document author name                      │
│    • \033[96m--pagesize\033[92m   : Page size (A4, letter)                    │
│    • \033[96m--color\033[92m      : Primary color theme                       │
│                                                             │
│  \033[93m📊 LAYOUT OPTIONS:\033[92m                                           │
│    • \033[96m--margins\033[92m    : Custom margins (in points)                │
│    • \033[96m--fontsize\033[92m   : Base font size                            │
│    • \033[96m--spacing\033[92m    : Line spacing multiplier                   │
│                                                             │
│  \033[93m🔧 UTILITY OPTIONS:\033[92m                                          │
│    • \033[96m--help\033[92m       : Show this help message                    │
│    • \033[96m--version\033[92m    : Show version information                  │
│    • \033[96m--preview\033[92m    : Preview JSON structure                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘\033[0m
    """
    print(menu)

def print_examples():
    """Print usage examples"""
    examples = """
\033[94m┌─────────────────────────────────────────────────────────────┐
│                       \033[95mUSAGE EXAMPLES\033[94m                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  \033[93mBasic Usage:\033[94m                                              │
│    \033[96mpython Json-to-pdf.py --input data.json --output doc.pdf\033[94m     │
│                                                             │
│  \033[93mCustom Title & Author:\033[94m                                     │
│    \033[96mpython Json-to-pdf.py --input data.json --output doc.pdf \\\033[94m  │
│           \033[96m--title "My Report" --author "John Doe"\033[94m              │
│                                                             │
│  \033[93mCustom Styling:\033[94m                                            │
│    \033[96mpython Json-to-pdf.py --input data.json --output doc.pdf \\\033[94m  │
│           \033[96m--pagesize letter --color blue --fontsize 12\033[94m         │
│                                                             │
│  \033[93mPreview JSON Structure:\033[94m                                    │
│    \033[96mpython Json-to-pdf.py --input data.json --preview\033[94m             │
│                                                             │
└─────────────────────────────────────────────────────────────┘\033[0m
    """
    print(examples)

def create_pdf_from_json(json_file_path: str, output_pdf_path: str, 
                        title: str = "Documentation", 
                        author: str = "Generated by JSON-to-PDF",
                        pagesize: str = "A4",
                        primary_color: str = "blue",
                        margins: int = 72,
                        font_size: int = 12,
                        spacing: float = 1.0) -> None:
    """
    Create a PDF document from JSON data with customizable options.
    
    Args:
        json_file_path: Path to the input JSON file
        output_pdf_path: Path for the output PDF file
        title: Document title
        author: Document author
        pagesize: Page size (A4 or letter)
        primary_color: Primary color theme
        margins: Page margins in points
        font_size: Base font size
        spacing: Line spacing multiplier
    """
    # Read JSON file
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"\033[91m❌ Error: File '{json_file_path}' not found!\033[0m")
        return
    except json.JSONDecodeError as e:
        print(f"\033[91m❌ Error: Invalid JSON format in '{json_file_path}': {e}\033[0m")
        return
    
    # Set page size
    page_format = A4 if pagesize.lower() == "a4" else letter
    
    # Create PDF document
    doc = SimpleDocTemplate(output_pdf_path, pagesize=page_format, 
                          rightMargin=margins, leftMargin=margins, 
                          topMargin=margins, bottomMargin=margins//4)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Define color scheme
    color_schemes = {
        'blue': {'primary': colors.darkblue, 'secondary': colors.blue, 'accent': colors.lightblue},
        'red': {'primary': colors.darkred, 'secondary': colors.red, 'accent': colors.pink},
        'green': {'primary': colors.darkgreen, 'secondary': colors.green, 'accent': colors.lightgreen},
        'purple': {'primary': colors.purple, 'secondary': colors.mediumpurple, 'accent': colors.lavender},
        'orange': {'primary': colors.darkorange, 'secondary': colors.orange, 'accent': colors.peachpuff}
    }
    
    scheme = color_schemes.get(primary_color.lower(), color_schemes['blue'])
    
    # Custom styles with user preferences
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=font_size + 12,
        spaceAfter=30 * spacing,
        alignment=TA_CENTER,
        textColor=scheme['primary']
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=font_size + 4,
        spaceAfter=12 * spacing,
        spaceBefore=20 * spacing,
        textColor=scheme['primary']
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=font_size + 2,
        spaceAfter=8 * spacing,
        spaceBefore=12 * spacing,
        textColor=scheme['secondary']
    )
    
    # Story list to hold all content
    story = []
    
    # Add document metadata
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(f"<i>Author: {author}</i>", styles['Normal']))
    story.append(Spacer(1, 20 * spacing))
    
    # Process JSON data dynamically
    def process_data(data_obj: Any, level: int = 0) -> None:
        """Recursively process JSON data and add to story"""
        if isinstance(data_obj, dict):
            for key, value in data_obj.items():
                # Create heading based on level
                if level == 0:
                    story.append(Paragraph(str(key).replace('_', ' ').title(), heading_style))
                elif level == 1:
                    story.append(Paragraph(str(key).replace('_', ' ').title(), subheading_style))
                else:
                    story.append(Paragraph(f"<b>{str(key).replace('_', ' ').title()}:</b>", styles['Normal']))
                
                process_data(value, level + 1)
                
        elif isinstance(data_obj, list):
            if len(data_obj) > 0 and isinstance(data_obj[0], dict):
                # Handle list of dictionaries as table
                create_table_from_list(data_obj, scheme)
            else:
                # Handle simple list
                for i, item in enumerate(data_obj, 1):
                    if isinstance(item, (str, int, float)):
                        story.append(Paragraph(f"{i}. {item}", styles['Normal']))
                    else:
                        story.append(Paragraph(f"{i}. {str(item)}", styles['Normal']))
                story.append(Spacer(1, 10 * spacing))
        else:
            # Handle simple values
            story.append(Paragraph(str(data_obj), styles['Normal']))
            story.append(Spacer(1, 5 * spacing))
    
    def create_table_from_list(data_list: List[Dict], color_scheme: Dict) -> None:
        """Create a formatted table from a list of dictionaries"""
        if not data_list:
            return
            
        # Get all unique keys for table headers
        all_keys = set()
        for item in data_list:
            if isinstance(item, dict):
                all_keys.update(item.keys())
        
        headers = list(all_keys)
        table_data = [headers]
        
        # Add data rows
        for item in data_list:
            if isinstance(item, dict):
                row = []
                for header in headers:
                    value = item.get(header, '')
                    if isinstance(value, (int, float)) and 'cost' in header.lower() or 'budget' in header.lower():
                        row.append(f"${format_currency(value)}" if value else '')
                    else:
                        row.append(str(value) if value else '')
                table_data.append(row)
        
        if len(table_data) > 1:  # Only create table if we have data
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), color_scheme['primary']),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), font_size),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), color_scheme['accent']),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 20 * spacing))
    
    # Process the entire JSON data
    process_data(data)
    
    # Build PDF
    try:
        doc.build(story)
        print(f"\033[92m✅ PDF generated successfully: {output_pdf_path}\033[0m")
        print(f"\033[94mℹ️  Document Info:\033[0m")
        print(f"   📄 Title: {title}")
        print(f"   👤 Author: {author}")
        print(f"   📏 Page Size: {pagesize.upper()}")
        print(f"   🎨 Color Theme: {primary_color.title()}")
    except Exception as e:
        print(f"\033[91m❌ Error generating PDF: {e}\033[0m")

def preview_json_structure(json_file_path: str) -> None:
    """Preview the structure of a JSON file"""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"\033[91m❌ Error: File '{json_file_path}' not found!\033[0m")
        return
    except json.JSONDecodeError as e:
        print(f"\033[91m❌ Error: Invalid JSON format: {e}\033[0m")
        return
    
    print(f"\033[96m📋 JSON Structure Preview for: {json_file_path}\033[0m")
    print("\033[94m" + "="*60 + "\033[0m")
    
    def analyze_structure(obj: Any, indent: int = 0) -> None:
        prefix = "  " * indent
        if isinstance(obj, dict):
            print(f"{prefix}\033[93m📁 Object ({len(obj)} keys):\033[0m")
            for key, value in obj.items():
                print(f"{prefix}  \033[96m🔑 {key}:\033[0m", end=" ")
                if isinstance(value, dict):
                    print(f"\033[93mObject ({len(value)} keys)\033[0m")
                    if indent < 2:  # Limit depth
                        analyze_structure(value, indent + 2)
                elif isinstance(value, list):
                    print(f"\033[92mArray ({len(value)} items)\033[0m")
                    if value and indent < 2:
                        print(f"{prefix}    \033[95mSample item type: {type(value[0]).__name__}\033[0m")
                else:
                    print(f"\033[94m{type(value).__name__}: {str(value)[:50]}{'...' if len(str(value)) > 50 else ''}\033[0m")
        elif isinstance(obj, list):
            print(f"{prefix}\033[92m📋 Array ({len(obj)} items)\033[0m")
            if obj and indent < 2:
                print(f"{prefix}  \033[95mSample item:\033[0m")
                analyze_structure(obj[0], indent + 1)
    
    analyze_structure(data)
    print("\033[94m" + "="*60 + "\033[0m")

def setup_argument_parser() -> argparse.ArgumentParser:
    """Set up command line argument parser"""
    parser = argparse.ArgumentParser(
        description="""
\033[96m🎨 JSON to PDF Converter v2.0\033[0m

Convert JSON data into professionally formatted PDF documents with customizable styling options.
This tool automatically processes any JSON structure and creates well-formatted tables and sections.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
\033[93mExamples:\033[0m
  \033[96mpython Json-to-pdf.py --input data.json --output report.pdf\033[0m
  \033[96mpython Json-to-pdf.py -i data.json -o report.pdf --title "My Report" --author "John Doe"\033[0m
  \033[96mpython Json-to-pdf.py -i data.json --preview\033[0m
  \033[96mpython Json-to-pdf.py -i data.json -o report.pdf --color red --pagesize letter\033[0m

\033[94mFor more information, visit: https://github.com/WangodaFrancis667/Simple-Utilities\033[0m
        """
    )
    
    # Input/Output arguments
    parser.add_argument('-i', '--input', 
                       required=True,
                       help='Path to input JSON file')
    
    parser.add_argument('-o', '--output',
                       help='Path for output PDF file (default: output.pdf)')
    
    # Customization arguments
    parser.add_argument('--title',
                       default='JSON Document',
                       help='Document title (default: "JSON Document")')
    
    parser.add_argument('--author',
                       default='Generated by JSON-to-PDF Converter',
                       help='Document author (default: "Generated by JSON-to-PDF Converter")')
    
    parser.add_argument('--pagesize',
                       choices=['A4', 'letter'],
                       default='A4',
                       help='Page size (default: A4)')
    
    parser.add_argument('--color',
                       choices=['blue', 'red', 'green', 'purple', 'orange'],
                       default='blue',
                       help='Primary color theme (default: blue)')
    
    parser.add_argument('--margins',
                       type=int,
                       default=72,
                       help='Page margins in points (default: 72)')
    
    parser.add_argument('--fontsize',
                       type=int,
                       default=12,
                       help='Base font size (default: 12)')
    
    parser.add_argument('--spacing',
                       type=float,
                       default=1.0,
                       help='Line spacing multiplier (default: 1.0)')
    
    # Utility arguments
    parser.add_argument('--preview',
                       action='store_true',
                       help='Preview JSON structure without generating PDF')
    
    parser.add_argument('--version',
                       action='version',
                       version='JSON-to-PDF Converter v2.0')
    
    return parser

def main():
    """Main function with enhanced command-line interface"""
    # Show banner
    print_colorful_banner()
    
    # Set up argument parser
    parser = setup_argument_parser()
    
    # Parse arguments
    try:
        args = parser.parse_args()
    except SystemExit:
        print_menu()
        print_examples()
        return
    
    # Handle preview mode
    if args.preview:
        preview_json_structure(args.input)
        return
    
    # Validate required arguments for PDF generation
    if not args.output:
        # Generate default output filename
        input_name = os.path.splitext(os.path.basename(args.input))[0]
        args.output = f"{input_name}_output.pdf"
        print(f"\033[93m⚠️  No output file specified. Using: {args.output}\033[0m")
    
    # Validate input file
    if not os.path.exists(args.input):
        print(f"\033[91m❌ Error: Input file '{args.input}' not found!\033[0m")
        return
    
    # Show processing info
    print(f"\033[94m🚀 Processing JSON file: {args.input}\033[0m")
    print(f"\033[94m📄 Output PDF: {args.output}\033[0m")
    print(f"\033[94m🎨 Settings: {args.pagesize} page, {args.color} theme, {args.fontsize}pt font\033[0m")
    print("\033[94m" + "-"*60 + "\033[0m")
    
    # Generate PDF
    try:
        create_pdf_from_json(
            json_file_path=args.input,
            output_pdf_path=args.output,
            title=args.title,
            author=args.author,
            pagesize=args.pagesize,
            primary_color=args.color,
            margins=args.margins,
            font_size=args.fontsize,
            spacing=args.spacing
        )
    except Exception as e:
        print(f"\033[91m❌ Unexpected error: {e}\033[0m")
        print("\033[93m💡 Try using --preview to check your JSON structure first.\033[0m")

if __name__ == "__main__":
    main()