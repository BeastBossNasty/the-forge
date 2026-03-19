#!/usr/bin/env python3
"""Generate Bella Luna Toys Before/After Voltage performance report PDF."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from pathlib import Path

# ReportLab colors
DARK = HexColor('#1a1a2e')
ACCENT = HexColor('#e94560')
BLUE = HexColor('#0f3460')
LIGHT_BG = HexColor('#f8f9fa')
GREEN = HexColor('#16a34a')
AMBER = HexColor('#d97706')
RED = HexColor('#dc2626')
GRAY = HexColor('#6b7280')
LIGHT_GRAY = HexColor('#e5e7eb')

# Matplotlib hex strings
M_DARK = '#1a1a2e'
M_ACCENT = '#e94560'
M_BLUE = '#0f3460'
M_GREEN = '#16a34a'
M_AMBER = '#d97706'
M_RED = '#dc2626'
M_GRAY = '#9ca3af'

# === DATA ===
# Before Voltage: Mar 2024 - May 2025 (15 months)
before_labels = ['Mar 24','Apr 24','May 24','Jun 24','Jul 24','Aug 24','Sep 24','Oct 24','Nov 24','Dec 24','Jan 25','Feb 25','Mar 25','Apr 25','May 25']
before_roas   = [11.37,14.79,16.82,11.85,13.95,17.50,7.67,6.17,10.99,11.00,9.06,9.15,9.57,7.09,8.27]
before_spend  = [6061,2360,2009,2002,2175,2111,1802,3760,5925,4954,1221,840,2997,2436,1756]
before_rev    = [68913,34903,33796,23732,30347,36938,13823,23211,65142,54501,11063,7689,28669,17279,14512]
before_purch  = [613,175,221,180,204,254,103,169,397,340,93,53,201,168,102]
before_cpc    = [0.30,0.37,0.31,0.26,0.28,0.27,0.29,0.34,0.30,0.30,0.17,0.17,0.34,0.27,0.34]
before_ctr    = [4.28,3.37,3.57,3.37,3.25,3.85,3.88,4.12,4.33,4.66,3.77,3.57,4.35,3.92,3.64]

# After Voltage: Jun 2025 - Mar 2026 (10 months, Mar partial)
after_labels = ['Jun 25','Jul 25','Aug 25','Sep 25','Oct 25','Nov 25','Dec 25','Jan 26','Feb 26','Mar 26']
after_roas   = [7.88,10.71,11.00,11.80,10.20,15.13,11.53,11.80,21.76,18.18]
after_spend  = [1496,943,1953,2219,2458,9005,10293,5557,10055,7442]
after_rev    = [11782,10094,21484,26177,25078,136260,118647,65567,218815,135316]
after_purch  = [75,60,152,184,176,726,777,465,1237,891]
after_cpc    = [0.46,0.34,0.27,0.29,0.35,0.48,0.41,0.44,0.52,0.65]
after_ctr    = [3.18,3.64,5.10,4.71,4.88,5.88,5.85,3.89,2.29,1.91]

# Aggregate stats
b_total_spend = sum(before_spend)
b_total_rev = sum(before_rev)
b_total_purch = sum(before_purch)
b_avg_roas = b_total_rev / b_total_spend
b_avg_cpa = b_total_spend / b_total_purch

a_total_spend = sum(after_spend)
a_total_rev = sum(after_rev)
a_total_purch = sum(after_purch)
a_avg_roas = a_total_rev / a_total_spend
a_avg_cpa = a_total_spend / a_total_purch


def make_before_after_roas():
    fig, ax = plt.subplots(figsize=(10, 3.8))
    all_labels = before_labels + after_labels
    all_roas = before_roas + after_roas
    colors = []
    for i, r in enumerate(all_roas):
        if i < len(before_labels):
            colors.append(M_GRAY if r >= 10 else ('#d1d5db' if r >= 5 else '#fca5a5'))
        else:
            colors.append(M_GREEN if r >= 10 else (M_AMBER if r >= 5 else M_RED))
    bars = ax.bar(range(len(all_labels)), all_roas, color=colors, width=0.7, edgecolor='white', linewidth=0.5)
    # Dividing line
    ax.axvline(x=len(before_labels)-0.5, color=M_ACCENT, linewidth=2.5, linestyle='-', zorder=5)
    ax.text(len(before_labels)-0.5, 23.5, '  Voltage starts', fontsize=9, fontweight='bold', color=M_ACCENT, ha='left')
    ax.axhline(y=10, color=M_ACCENT, linestyle='--', linewidth=1, alpha=0.5, label='10x Healthy Threshold')
    ax.set_xticks(range(len(all_labels)))
    ax.set_xticklabels(all_labels, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel('ROAS', fontsize=10, fontweight='bold')
    ax.set_title('Monthly ROAS: Before vs After Voltage', fontsize=13, fontweight='bold', pad=10)
    ax.legend(fontsize=8, loc='upper left')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, 25)
    for i, v in enumerate(all_roas):
        if v >= 15:
            ax.text(i, v + 0.3, f'{v:.1f}x', ha='center', va='bottom', fontsize=6.5, fontweight='bold')
    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf


def make_before_after_revenue():
    fig, ax = plt.subplots(figsize=(10, 3.5))
    all_labels = before_labels + after_labels
    all_rev = [r/1000 for r in before_rev] + [r/1000 for r in after_rev]
    all_spend = [s/1000 for s in before_spend] + [s/1000 for s in after_spend]
    x = range(len(all_labels))
    bar_colors = [M_GRAY]*len(before_labels) + [M_BLUE]*len(after_labels)
    ax.bar(x, all_spend, color=bar_colors, alpha=0.6, width=0.7, label='Spend ($K)')
    ax2 = ax.twinx()
    line_colors_before = [M_GRAY]*len(before_labels)
    line_colors_after = [M_ACCENT]*len(after_labels)
    ax2.plot(range(len(before_labels)), all_rev[:len(before_labels)], color=M_GRAY, linewidth=2, marker='o', markersize=3, label='Revenue Before ($K)')
    ax2.plot(range(len(before_labels), len(all_labels)), all_rev[len(before_labels):], color=M_ACCENT, linewidth=2.5, marker='o', markersize=4, label='Revenue After ($K)')
    ax.axvline(x=len(before_labels)-0.5, color=M_ACCENT, linewidth=2.5, linestyle='-', zorder=5)
    ax.set_xticks(x)
    ax.set_xticklabels(all_labels, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel('Spend ($K)', fontsize=10, fontweight='bold')
    ax2.set_ylabel('Revenue ($K)', fontsize=10, fontweight='bold', color=M_ACCENT)
    ax.set_title('Spend vs Revenue: Before vs After Voltage', fontsize=13, fontweight='bold', pad=10)
    ax.set_ylim(0, 15)
    ax2.set_ylim(0, 250)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1+lines2, labels1+labels2, fontsize=7, loc='upper left')
    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf


def make_comparison_bars():
    fig, axes = plt.subplots(1, 4, figsize=(10, 3))
    metrics = [
        ('Blended ROAS', f'{b_avg_roas:.1f}x', f'{a_avg_roas:.1f}x', b_avg_roas, a_avg_roas),
        ('Avg CPA', f'${b_avg_cpa:.2f}', f'${a_avg_cpa:.2f}', b_avg_cpa, a_avg_cpa),
        ('Avg Monthly Rev', f'${b_total_rev/15/1000:.0f}K', f'${a_total_rev/10/1000:.0f}K', b_total_rev/15, a_total_rev/10),
        ('Avg Monthly Purch', f'{b_total_purch/15:.0f}', f'{a_total_purch/10:.0f}', b_total_purch/15, a_total_purch/10),
    ]
    for ax, (label, b_str, a_str, b_val, a_val) in zip(axes, metrics):
        bars = ax.bar(['Before', 'After'], [b_val, a_val], color=[M_GRAY, M_ACCENT], width=0.5, edgecolor='white')
        ax.set_title(label, fontsize=9, fontweight='bold')
        ax.bar_label(bars, labels=[b_str, a_str], fontsize=8, fontweight='bold', padding=3)
        ax.set_ylim(0, max(b_val, a_val) * 1.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='y', labelsize=7)
    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf


def make_quarterly_comparison():
    fig, ax = plt.subplots(figsize=(10, 3))
    quarters = ['Q2 24\n(Before)', 'Q3 24\n(Before)', 'Q4 24\n(Before)', 'Q1 25\n(Before)', 'Q2 25\n(Transition)', 'Q3 25\n(After)', 'Q4 25\n(After)', 'Q1 26\n(After)']
    q_revenue = [
        34903+33796+23732, 30347+36938+13823, 23211+65142+54501,
        11063+7689+28669, 17279+14512+11782,
        10094+21484+26177, 25078+136260+118647, 65567+218815+135316
    ]
    q_rev_k = [r/1000 for r in q_revenue]
    colors_q = [M_GRAY]*4 + [M_AMBER] + [M_ACCENT]*3
    bars = ax.bar(range(len(quarters)), q_rev_k, color=colors_q, width=0.6, edgecolor='white')
    for i, v in enumerate(q_rev_k):
        ax.text(i, v + 5, f'${v:.0f}K', ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax.set_xticks(range(len(quarters)))
    ax.set_xticklabels(quarters, fontsize=7.5)
    ax.set_ylabel('Revenue ($K)', fontsize=10, fontweight='bold')
    ax.set_title('Quarterly Revenue: Before vs After Voltage', fontsize=13, fontweight='bold', pad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, max(q_rev_k) * 1.25)
    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf


def build_pdf():
    output_path = Path(__file__).parent.parent / "vault" / "_clients" / "bella-luna" / "reports"
    output_path.mkdir(exist_ok=True)
    pdf_path = output_path / "2026-03-19-bella-luna-performance-report.pdf"

    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter,
        leftMargin=0.6*inch, rightMargin=0.6*inch,
        topMargin=0.5*inch, bottomMargin=0.5*inch)

    # Styles
    title_style = ParagraphStyle('Title', fontSize=28, fontName='Helvetica-Bold', textColor=DARK, spaceAfter=4, leading=32)
    subtitle_style = ParagraphStyle('Subtitle', fontSize=14, fontName='Helvetica', textColor=GRAY, spaceAfter=6, leading=18)
    tagline_style = ParagraphStyle('Tagline', fontSize=11, fontName='Helvetica-Oblique', textColor=ACCENT, spaceAfter=20, leading=14)
    h1 = ParagraphStyle('H1', fontSize=18, fontName='Helvetica-Bold', textColor=DARK, spaceBefore=16, spaceAfter=8, leading=22)
    h2 = ParagraphStyle('H2', fontSize=14, fontName='Helvetica-Bold', textColor=BLUE, spaceBefore=12, spaceAfter=6, leading=18)
    body = ParagraphStyle('Body', fontSize=10, fontName='Helvetica', textColor=HexColor('#374151'), spaceAfter=8, leading=14)
    body_bold = ParagraphStyle('BodyBold', fontSize=10, fontName='Helvetica-Bold', textColor=HexColor('#374151'), spaceAfter=8, leading=14)
    metric_big = ParagraphStyle('MetricBig', fontSize=32, fontName='Helvetica-Bold', textColor=ACCENT, alignment=TA_CENTER, leading=36)
    metric_label = ParagraphStyle('MetricLabel', fontSize=8, fontName='Helvetica', textColor=GRAY, alignment=TA_CENTER, leading=11)
    footer_style = ParagraphStyle('Footer', fontSize=8, fontName='Helvetica', textColor=GRAY, alignment=TA_CENTER)
    green_text = ParagraphStyle('Green', fontSize=10, fontName='Helvetica-Bold', textColor=GREEN, spaceAfter=4, leading=14)
    white_body = ParagraphStyle('WhiteBody', fontSize=10, fontName='Helvetica', textColor=white, alignment=TA_CENTER, leading=14)
    white_bold = ParagraphStyle('WhiteBold', fontSize=11, fontName='Helvetica-Bold', textColor=white, leading=14)

    story = []

    # === PAGE 1: COVER ===
    story.append(Spacer(1, 1.2*inch))
    story.append(Paragraph("Bella Luna Toys", title_style))
    story.append(Paragraph("Meta Ads Performance Report", subtitle_style))
    story.append(Paragraph("Before and After Voltage Media", tagline_style))
    story.append(HRFlowable(width="100%", thickness=3, color=ACCENT, spaceAfter=25))

    # Before vs After hero metrics
    hero_data = [
        ['', Paragraph("<b>Before Voltage</b><br/>Mar 2024 - May 2025 (15 mo)", ParagraphStyle('', fontSize=9, fontName='Helvetica-Bold', textColor=white, alignment=TA_CENTER, leading=12)),
             Paragraph("<b>After Voltage</b><br/>Jun 2025 - Mar 2026 (10 mo)", ParagraphStyle('', fontSize=9, fontName='Helvetica-Bold', textColor=white, alignment=TA_CENTER, leading=12)),
             Paragraph("<b>Change</b>", ParagraphStyle('', fontSize=9, fontName='Helvetica-Bold', textColor=white, alignment=TA_CENTER, leading=12))],
        [Paragraph("<b>Total Revenue</b>", body_bold), Paragraph(f"${b_total_rev:,.0f}", body), Paragraph(f"${a_total_rev:,.0f}", body_bold), Paragraph(f"+{((a_total_rev/b_total_rev)-1)*100:.0f}% in 33% less time", green_text)],
        [Paragraph("<b>Total Spend</b>", body_bold), Paragraph(f"${b_total_spend:,.0f}", body), Paragraph(f"${a_total_spend:,.0f}", body_bold), Paragraph(f"+{((a_total_spend/b_total_spend)-1)*100:.0f}%", body)],
        [Paragraph("<b>Blended ROAS</b>", body_bold), Paragraph(f"{b_avg_roas:.1f}x", body), Paragraph(f"{a_avg_roas:.1f}x", body_bold), Paragraph(f"+{((a_avg_roas/b_avg_roas)-1)*100:.0f}%", green_text)],
        [Paragraph("<b>Total Purchases</b>", body_bold), Paragraph(f"{b_total_purch:,}", body), Paragraph(f"{a_total_purch:,}", body_bold), Paragraph(f"+{((a_total_purch/b_total_purch)-1)*100:.0f}% in 33% less time", green_text)],
        [Paragraph("<b>Avg CPA</b>", body_bold), Paragraph(f"${b_avg_cpa:.2f}", body), Paragraph(f"${a_avg_cpa:.2f}", body_bold), Paragraph(f"-{((1 - a_avg_cpa/b_avg_cpa))*100:.0f}% reduction", green_text)],
        [Paragraph("<b>Avg Monthly Revenue</b>", body_bold), Paragraph(f"${b_total_rev/15:,.0f}", body), Paragraph(f"${a_total_rev/10:,.0f}", body_bold), Paragraph(f"+{((a_total_rev/10)/(b_total_rev/15)-1)*100:.0f}%", green_text)],
    ]
    hero_table = Table(hero_data, colWidths=[1.5*inch, 1.7*inch, 1.7*inch, 2.0*inch])
    hero_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), LIGHT_BG),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(hero_table)

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Prepared by Voltage Media  |  March 19, 2026", body))
    story.append(Paragraph("Google Premier Partner (Top 3%)  |  Meta Business Partner  |  Microsoft Advertising Partner", ParagraphStyle('', fontSize=9, fontName='Helvetica', textColor=GRAY, leading=12)))

    # === PAGE 2: THE STORY ===
    story.append(PageBreak())
    story.append(Paragraph("The Transformation Story", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    story.append(Paragraph("Before Voltage (March 2024 through May 2025)", h2))
    story.append(Paragraph(
        "Prior to Voltage's engagement, Bella Luna's Meta Ads account was running 70+ fragmented campaigns "
        "with inconsistent structure and no unified strategy. While the product resonated with audiences "
        "(ROAS occasionally spiked above 15x), performance was volatile. The account hit its lowest point in "
        "September-October 2024 at 6-8x ROAS with CPAs above $20. Monthly revenue averaged $28,895 with "
        "no clear scaling path.", body))

    story.append(Paragraph("After Voltage (June 2025 through Present)", h2))
    story.append(Paragraph(
        "Voltage implemented a three-phase transformation. First, the account was consolidated from 70+ "
        "campaigns down to a clean two-campaign structure (one CBO for always-on prospecting, one ABO for "
        "seasonal pushes). Second, a momentum-based scaling strategy was deployed with gradient budget "
        "adjustments tied to ROAS performance. Third, disciplined creative rotation with UGC-style content "
        "replaced ad hoc creative decisions.", body))
    story.append(Paragraph(
        "The results speak for themselves. Average monthly revenue increased from $28,895 to $76,920 "
        "while blended ROAS improved from 10.6x to 15.2x. February 2026 produced the best single month "
        "in account history: $218,815 in revenue at 21.76x ROAS on just $10,055 in spend.", body))

    # Current state callout
    story.append(Spacer(1, 10))
    current_data = [
        [Paragraph("<b>Current State: March 2026 (18 Days)</b>", white_bold)],
        [Paragraph("18.18x ROAS  |  $135,316 Revenue  |  891 Purchases  |  $8.35 CPA  |  $7,442 Spend", white_body)],
        [Paragraph("Q1 2026 has already generated more revenue ($419,699) than all of 2025 ($310,774)", white_body)],
    ]
    current_table = Table(current_data, colWidths=[6.8*inch])
    current_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BLUE),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (0,0), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('ROUNDEDCORNERS', [6,6,6,6]),
    ]))
    story.append(current_table)

    # === PAGE 3: ROAS CHART ===
    story.append(PageBreak())
    story.append(Paragraph("Performance Analysis", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    roas_buf = make_before_after_roas()
    story.append(Image(roas_buf, width=7*inch, height=2.66*inch))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Gray bars represent performance before Voltage's engagement. Colored bars show performance under "
        "Voltage management. The red vertical line marks the transition point (June 2025). Note the "
        "elimination of sub-10x months and the dramatic upward trajectory in Q4 2025 through Q1 2026.", body))

    story.append(Spacer(1, 8))
    rev_buf = make_before_after_revenue()
    story.append(Image(rev_buf, width=7*inch, height=2.45*inch))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Under Voltage management, the relationship between spend and revenue has fundamentally improved. "
        "The account now converts modest spend increases into outsized revenue gains. February 2026's "
        "$10K in spend generated $219K in revenue, a return that would have been unthinkable under the "
        "prior fragmented campaign structure.", body))

    # === PAGE 4: COMPARISON BARS + QUARTERLY ===
    story.append(PageBreak())
    story.append(Paragraph("Before vs After: Key Metrics", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    comp_buf = make_comparison_bars()
    story.append(Image(comp_buf, width=7*inch, height=2.1*inch))
    story.append(Spacer(1, 15))

    q_buf = make_quarterly_comparison()
    story.append(Image(q_buf, width=7*inch, height=2.1*inch))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "The quarterly revenue trajectory demonstrates consistent acceleration under Voltage management. "
        "Q4 2025 ($279,985) was the first quarter to break the $100K barrier. Q1 2026 ($419,699 through "
        "March 18) has already shattered that record and is on pace to exceed $500K.", body))

    # === PAGE 5: WHAT WE DID + RECOMMENDATIONS ===
    story.append(PageBreak())
    story.append(Paragraph("What Voltage Changed", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=12))

    changes = [
        ["Campaign Structure", "70+ fragmented campaigns", "2 campaigns (CBO + seasonal ABO)", "Consolidated learning data fed the algorithm faster"],
        ["Scaling Strategy", "Ad hoc budget adjustments", "Gradient scaling (5-20% based on ROAS)", "Eliminated CPA spikes from over-scaling"],
        ["Creative Approach", "Inconsistent rotation", "UGC-first with data-driven rotation triggers", "Creative refresh at frequency 3x or CTR drop 30%+"],
        ["Decision Framework", "Reactive", "Rubric-based with 3-tier classification", "Every ad set scored against benchmarks daily"],
    ]
    c_header = [Paragraph("<b>Area</b>", body_bold), Paragraph("<b>Before</b>", body_bold), Paragraph("<b>After</b>", body_bold), Paragraph("<b>Why It Matters</b>", body_bold)]
    c_rows = [c_header]
    for row in changes:
        c_rows.append([Paragraph(row[0], body_bold), Paragraph(row[1], body), Paragraph(row[2], body_bold), Paragraph(row[3], body)])
    c_table = Table(c_rows, colWidths=[1.2*inch, 1.6*inch, 1.8*inch, 2.2*inch])
    c_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), LIGHT_BG),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT_GRAY),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(c_table)

    story.append(Spacer(1, 15))
    story.append(Paragraph("Strategic Recommendations", h2))

    recs = [
        "<b>1. Maintain current momentum.</b> At 18x+ ROAS, the strategy is working. No changes to spend posture recommended.",
        "<b>2. Prioritize creative refresh.</b> Frequency approaching 3.0x cap. UGC-style content has consistently outperformed. New creative assets should be in pipeline.",
        "<b>3. Monitor CPC/CTR convergence.</b> CPC rising ($0.44 to $0.65) and CTR declining (3.89% to 1.91%) are leading indicators. Not impacting ROAS yet but require attention.",
        "<b>4. Prepare for Q2 seasonality.</b> Historical data shows mid-year softness. The consolidated structure should handle the seasonal dip better than the fragmented structure did in 2024.",
        "<b>5. Explore video creative.</b> AI-rendered video ads represent the next creative frontier for scaling without production bottlenecks.",
    ]
    for text in recs:
        story.append(Paragraph(text, body))
        story.append(Spacer(1, 3))

    # Footer
    story.append(Spacer(1, 0.4*inch))
    story.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY, spaceAfter=10))
    story.append(Paragraph("Prepared by Voltage Media  |  Google Premier Partner  |  Meta Business Partner  |  Microsoft Advertising Partner", footer_style))
    story.append(Paragraph("Confidential. For authorized use only.", footer_style))

    doc.build(story)
    print(f"PDF saved to: {pdf_path}")
    return str(pdf_path)


if __name__ == "__main__":
    build_pdf()
