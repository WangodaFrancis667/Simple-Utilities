import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import sys
import os

def format_currency(amount):
    """Format currency with commas"""
    return f"{amount:,}"

def create_pdf_from_json(json_file_path, output_pdf_path):
    # Read JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Create PDF document
    doc = SimpleDocTemplate(output_pdf_path, pagesize=A4, 
                          rightMargin=72, leftMargin=72, 
                          topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.darkblue
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=12,
        textColor=colors.blue
    )
    
    # Story list to hold all content
    story = []
    
    # Title
    story.append(Paragraph("Documentation", title_style))
    story.append(Spacer(1, 20))
    
    # Project Roadmap
    story.append(Paragraph("Project Roadmap", heading_style))
    
    for i, phase in enumerate(data['roadmap'], 1):
        story.append(Paragraph(f"{i}. {phase['phase']}", subheading_style))
        story.append(Paragraph(f"<b>Duration:</b> {phase['duration']}", styles['Normal']))
        story.append(Paragraph(f"<b>Activities:</b> {phase['activities']}", styles['Normal']))
        story.append(Spacer(1, 10))
    
    story.append(PageBreak())
    
    # Team Structure
    story.append(Paragraph("Team Structure", heading_style))
    
    team_data = [['Role', 'Count', 'Experience', 'Hourly Rate (USD)']]
    for member in data['team_structure']:
        team_data.append([
            member['role'],
            str(member['count']),
            member['experience'],
            f"${member['hourly_rate_usd']}"
        ])
    
    team_table = Table(team_data)
    team_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(team_table)
    story.append(Spacer(1, 20))
    
    # Pricing Estimates
    story.append(Paragraph("Pricing Estimates", heading_style))
    
    # Hours breakdown
    story.append(Paragraph("Estimated Hours by Role", subheading_style))
    hours_data = [['Role', 'Hours', 'Hourly Rate (USD)', 'Total Cost (USD)']]
    
    pricing = data['pricing_estimates']
    for role in pricing['estimated_hours']:
        hours = pricing['estimated_hours'][role]
        rate = pricing['hourly_rates_usd'][role]
        cost = pricing['costs_usd'][role]
        hours_data.append([role.title(), str(hours), f"${rate}", f"${format_currency(cost)}"])
    
    # Add total row
    total_cost = sum(pricing['costs_usd'].values())
    total_hours = sum(pricing['estimated_hours'].values())
    hours_data.append(['TOTAL', str(total_hours), '-', f"${format_currency(total_cost)}"])
    
    hours_table = Table(hours_data)
    hours_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(hours_table)
    story.append(Spacer(1, 20))
    
    # Budget in UGX
    story.append(Paragraph("Project Budget (UGX)", heading_style))
    
    budget = data['project_budget_ugx']
    story.append(Paragraph(f"<b>Conversion Rate:</b> {format_currency(budget['conversion_rate_ugx_per_usd'])} UGX per USD", styles['Normal']))
    story.append(Paragraph(f"<b>Total Estimated Budget:</b> {format_currency(budget['total_estimated_budget_ugx'])} UGX", styles['Normal']))
    story.append(Spacer(1, 15))
    
    # Budget breakdown
    story.append(Paragraph("Budget Breakdown by Role", subheading_style))
    budget_data = [['Role', 'Total Budget (UGX)', 'Monthly Allowance (UGX)']]
    
    for role in budget['breakdown_ugx']:
        total_budget = budget['breakdown_ugx'][role]
        monthly = budget['monthly_allowance_ugx'][role]
        budget_data.append([role, format_currency(total_budget), format_currency(monthly)])
    
    budget_table = Table(budget_data)
    budget_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(budget_table)
    story.append(PageBreak())
    
    # Tools and Services
    story.append(Paragraph("Tools and Services", heading_style))
    for i, tool in enumerate(data['tools_services'], 1):
        # Clean up the tool description by removing content references
        clean_tool = tool.split(':contentReference')[0]
        story.append(Paragraph(f"{i}. {clean_tool}", styles['Normal']))
        story.append(Spacer(1, 5))
    
    story.append(Spacer(1, 20))
    
    # Dashboard Templates
    story.append(Paragraph("Dashboard Templates", heading_style))
    for i, template in enumerate(data['dashboard_templates'], 1):
        # Clean up template description
        clean_template = template.split(':contentReference')[0]
        story.append(Paragraph(f"{i}. {clean_template}", styles['Normal']))
        story.append(Spacer(1, 5))
    
    # Build PDF
    doc.build(story)
    print(f"PDF generated successfully: {output_pdf_path}")

def main():
    # Get file paths
    json_file = "test.json"
    output_file = "Documentation.pdf"
    
    # Check if JSON file exists
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found!")
        return
    
    try:
        create_pdf_from_json(json_file, output_file)
        print(f"Successfully converted {json_file} to {output_file}")
    except Exception as e:
        print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    main()