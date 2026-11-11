import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FINAL_PDF_DIR = os.path.join(BASE_DIR, "Part_B_NEXORA", "Final_PDF")
os.makedirs(FINAL_PDF_DIR, exist_ok=True)

PDF_FILENAME = "EBS24CS-P02-PES1UG24CS513-PES1UG24CS457-PES1UG24CS476-PES1UG24CS443-NEXORA-ONE.pdf"
PDF_PATH = os.path.join(FINAL_PDF_DIR, PDF_FILENAME)

LOGO_PATH = os.path.join(BASE_DIR, "Part_B_NEXORA", "Logo", "nexora_logo.png")
IMG_DIR = os.path.join(BASE_DIR, "Part_B_NEXORA", "Images")
ARCH_IMG = os.path.join(IMG_DIR, "architecture_diagram.png")
AGENT_IMG = os.path.join(IMG_DIR, "agent_suite_diagram.png")
WORKFLOW_IMG = os.path.join(IMG_DIR, "workflow_comparison.png")

# Brand Palette (NEXORA Cyber-Executive)
DARK_NAVY = colors.HexColor("#0B132B")
SLATE_NAVY = colors.HexColor("#1C2541")
ELECTRIC_CYAN = colors.HexColor("#00F0FF")
VIVID_BLUE = colors.HexColor("#3A86FF")
TEXT_LIGHT = colors.HexColor("#E2E8F0")
TEXT_MUTED = colors.HexColor("#94A3B8")
ACCENT_GREEN = colors.HexColor("#10B981")
ACCENT_ORANGE = colors.HexColor("#F59E0B")
CARD_BG = colors.HexColor("#152238")
WHITE = colors.white

def draw_page_background(c, doc):
    """Paint the page background before Platypus content is drawn."""
    c.saveState()
    c.setFillColor(DARK_NAVY)
    c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setFillColor(VIVID_BLUE)
    c.rect(0, A4[1] - 5, A4[0], 5, fill=1, stroke=0)
    c.setFillColor(ELECTRIC_CYAN)
    c.rect(0, 0, A4[0], 4, fill=1, stroke=0)
    c.restoreState()


def draw_page_foreground(c, doc):
    """Draw running header/footer after page content without covering it."""
    if c.getPageNumber() <= 1:
        return
    c.saveState()
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(ELECTRIC_CYAN)
    c.drawString(36, 818, "NEXORA ONE")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(100, 818, "|  AGENTIC AI-NATIVE ENTERPRISE BUSINESS SYSTEM")
    c.drawRightString(559, 818, "EXECUTIVE PRODUCT BROCHURE")
    c.setStrokeColor(colors.HexColor("#2D3748"))
    c.setLineWidth(0.5)
    c.line(36, 812, 559, 812)
    c.line(36, 32, 559, 32)
    c.setFillColor(TEXT_MUTED)
    c.drawString(36, 20, "Nexora Technologies Inc.  Ã¢â‚¬Â¢  PES University EBS Academic Project (UE24CS343AB8)")
    c.drawRightString(559, 20, f"Page {c.getPageNumber()}")
    c.restoreState()

def build_brochure():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Typography Styles for Brochure
    hero_title = ParagraphStyle(
        'HeroTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=30,
        leading=36,
        textColor=WHITE,
        alignment=1,
        spaceAfter=8
    )

    hero_subtitle = ParagraphStyle(
        'HeroSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=20,
        textColor=ELECTRIC_CYAN,
        alignment=1,
        spaceAfter=15
    )

    h1_brochure = ParagraphStyle(
        'H1Brochure',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=22,
        textColor=ELECTRIC_CYAN,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_brochure = ParagraphStyle(
        'H2Brochure',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=VIVID_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_brochure = ParagraphStyle(
        'BodyBrochure',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=TEXT_LIGHT,
        spaceAfter=6
    )

    bullet_brochure = ParagraphStyle(
        'BulletBrochure',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=TEXT_LIGHT,
        leftIndent=12,
        spaceAfter=3
    )

    card_title = ParagraphStyle(
        'CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=ELECTRIC_CYAN,
        spaceAfter=2
    )

    card_body = ParagraphStyle(
        'CardBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=TEXT_LIGHT
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER & BRAND INTRODUCTION
    # =========================================================================
    story.append(Spacer(1, 30))
    if os.path.exists(LOGO_PATH):
        story.append(Image(LOGO_PATH, width=480, height=160))
    story.append(Spacer(1, 20))

    story.append(Paragraph("THE AUTONOMOUS ENTERPRISE IS HERE", hero_subtitle))
    story.append(Paragraph("NEXORA ONE", hero_title))
    story.append(Paragraph("<i>Your Business. Your AI. Your Future.</i>", ParagraphStyle('Tagline', fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=1, textColor=WHITE, spaceAfter=20)))

    story.append(HRFlowable(width="80%", thickness=2, color=ELECTRIC_CYAN, spaceAfter=25, hAlign='CENTER'))

    story.append(Paragraph(
        "Welcome to <b>NEXORA ONE</b> Ã¢â‚¬â€ a proposed agentic, AI-native Enterprise Business System concept designed to move "
        "business operations beyond repetitive data entry toward guided, policy-aware execution. The concept combines enterprise "
        "data, specialized AI agents, deterministic checks, and human approval so teams can review recommendations and automate "
        "routine steps while retaining control over important business decisions.",
        ParagraphStyle('CoverLead', fontName='Helvetica', fontSize=10, leading=15, alignment=1, textColor=TEXT_LIGHT, spaceAfter=25)
    ))

    # 3 High Impact Value Highlights
    val_cards = [
        [
            Paragraph("<b>WORKFLOW AUTOMATION</b><br/><font color='#94A3B8'>A concept for reducing repetitive Procure-to-Pay and Order-to-Cash work.</font>", card_body),
            Paragraph("<b>ASSISTED RECONCILIATION</b><br/><font color='#94A3B8'>AI-assisted document matching with human review for exceptions.</font>", card_body),
            Paragraph("<b>CONTINUOUS ENTERPRISE LEARNING</b><br/><font color='#94A3B8'>Fine-tuned cognitive agents adapting to seasonal fluctuations and supply shocks.</font>", card_body)
        ]
    ]
    t_val = Table(val_cards, colWidths=[170, 170, 170])
    t_val.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_val)

    story.append(Spacer(1, 35))
    story.append(Paragraph("<b>Enterprise Edition 2026.4</b>  Ã¢â‚¬Â¢  Academic Engineering Showcase  Ã¢â‚¬Â¢  PES University", ParagraphStyle('CoverFoot', fontName='Helvetica-Bold', fontSize=8.5, alignment=1, textColor=TEXT_MUTED)))

    # =========================================================================
    # PAGE 2: ARCHITECTURE & AUTONOMOUS CORE
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("PLATFORM ARCHITECTURE &amp; AUTONOMOUS CORE", h1_brochure))
    story.append(Paragraph("A Unified Four-Layer Cognitive Infrastructure Built for Autonomous Resilience", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "NEXORA ONE breaks free from monolithic relational rigidity through an advanced four-tier architecture combining modern distributed ledger "
        "resilience, enterprise knowledge ontologies, and specialized cognitive reasoning agents:",
        body_brochure
    ))

    if os.path.exists(ARCH_IMG):
        story.append(Image(ARCH_IMG, width=515, height=270))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Core Enterprise Modules Reimagined with Agentic Autonomy:", h2_brochure))

    mod_data = [
        [
            Paragraph("<b>1. Autonomous Financial Ledger</b><br/>Continuous real-time accounting, algorithmic treasury optimization, automated GSTR/TDS compliance, and multi-currency hedging.", card_body),
            Paragraph("<b>2. Supply Chain Sentinel</b><br/>Multi-horizon predictive inventory planning, supplier quality indexing, zero-touch RFPs, and autonomous stock rebalancing across hubs.", card_body)
        ],
        [
            Paragraph("<b>3. Adaptive Revenue &amp; Sales AI</b><br/>Conversational quote-to-order pipeline, dynamic elasticity pricing, algorithmic churn prevention, and automated account management.", card_body),
            Paragraph("<b>4. Smart Operations &amp; Maintenance</b><br/>IoT-connected telemetry, automated equipment preventative maintenance tickets, and intelligent cross-warehouse dispatch routing.", card_body)
        ]
    ]
    t_mod = Table(mod_data, colWidths=[255, 255])
    t_mod.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_mod)

    # =========================================================================
    # PAGE 3: SPECIALIZED AGENTIC AI MODULES
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("SPECIALISED AGENTIC AI MODULES", h1_brochure))
    story.append(Paragraph("Three Purpose-Built Autonomous Agents Powering Core Operations", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "NEXORA ONE replaces manual clerical tasks with domain-specialized AI agents capable of contextual reasoning, "
        "inter-agent negotiation, and self-directed execution within deterministic risk boundaries:",
        body_brochure
    ))

    if os.path.exists(AGENT_IMG):
        story.append(Image(AGENT_IMG, width=515, height=255))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Deep Dive: Agent Capabilities &amp; Enterprise Impact", h2_brochure))

    agent_details = [
        ("Nexora SupplySentinelÃ¢â€žÂ¢ (Inventory &amp; P2P)",
         "Monitors inventory levels continuously across multi-facility operations. When physical stock or projected demand breaches safety stock thresholds, the agent automatically extracts historical supplier velocity, issues electronic RFPs, evaluates wholesale price bids, drafts Purchase Orders, and routes them for instant execution without human intervention for transactions under configured limits (e.g., Ã¢â€šÂ¹50,000)."),
        ("Nexora FinanceGuardianÃ¢â€žÂ¢ (Continuous Audit &amp; AR/AP)",
         "Eliminates invoice fraud, manual reconciliation, and duplicate payments. Utilizing advanced multimodal OCR, it parses vendor bills in any layout, conducts mathematical line verification, verifies purchase orders against warehouse goods receipt notes (GRN), and posts general ledger entries instantly. Discrepancies trigger instant exception dockets with suggested resolution options."),
        ("Nexora RevenuePilotÃ¢â€žÂ¢ (Adaptive Sales Intelligence)",
         "Engages B2B customers via conversational natural language interfaces. Formulates customized service packages, validates equipment availability in real-time, adjusts pricing dynamically based on client lifetime value and capacity demand, and converts proposals into confirmed sales orders with instantaneous payment gateway generation.")
    ]

    for title, desc in agent_details:
        story.append(Paragraph(f"Ã¢â‚¬Â¢ <b>{title}:</b> {desc}", bullet_brochure))

    # =========================================================================
    # PAGE 4: HUMAN VS AI WORKFLOW VELOCITY
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("OPERATIONAL VELOCITY: HUMAN VS AI WORKFLOW", h1_brochure))
    story.append(Paragraph("Transforming Multi-Day Friction into Sub-Minute Autonomous Execution", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "The following comparison is an illustrative design scenario, not a measured product benchmark. Actual cycle times depend on "
        "transaction volume, integrations, data quality, approval rules, and human review. NEXORA ONE is a proposed concept; "
        "these timings have not been validated in a production deployment:",
        body_brochure
    ))

    if os.path.exists(WORKFLOW_IMG):
        story.append(Image(WORKFLOW_IMG, width=515, height=255))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Detailed Process Velocity Benchmarks:", h2_brochure))

    bench_data = [
        [Paragraph("<b>Workflow Stage</b>", card_title), Paragraph("<b>Traditional Legacy ERP</b>", card_title), Paragraph("<b>NEXORA ONE Autonomous AI</b>", card_title), Paragraph("<b>Efficiency Multiplier</b>", card_title)],
        [Paragraph("Procurement Requirement", card_body), Paragraph("4 - 6 hours manual audit", card_body), Paragraph("0.2 seconds predictive scan", card_body), Paragraph("Illustrative only", card_body)],
        [Paragraph("PO Drafting &amp; Vendor RFP", card_body), Paragraph("2 hours manual creation", card_body), Paragraph("1.5 seconds multi-vendor RFP", card_body), Paragraph("Illustrative only", card_body)],
        [Paragraph("Manager Approval Routing", card_body), Paragraph("24 - 48 hours email lag", card_body), Paragraph("Instant threshold approval", card_body), Paragraph("Policy dependent", card_body)],
        [Paragraph("Inward Goods Intake", card_body), Paragraph("4 hours manual docketing", card_body), Paragraph("10s computer vision scan", card_body), Paragraph("Illustrative only", card_body)],
        [Paragraph("3-Way Match &amp; Invoicing", card_body), Paragraph("3 hours clerical cross-check", card_body), Paragraph("1.2s zero-touch matching", card_body), Paragraph("Illustrative only", card_body)],
        [Paragraph("Bank Disbursement", card_body), Paragraph("24 hours batched payout", card_body), Paragraph("Instant smart banking hook", card_body), Paragraph("Requires bank integration", card_body)],
        [Paragraph("<b>Total End-to-End P2P</b>", card_title), Paragraph("<b>5 to 7 Business Days</b>", card_title), Paragraph("Depends on workflow and approvals", card_title), Paragraph("Not a measured result", card_title)]
    ]
    t_bench = Table(bench_data, colWidths=[125, 130, 140, 115])
    t_bench.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [DARK_NAVY, CARD_BG])
    ]))
    story.append(t_bench)

    # =========================================================================
    # PAGE 5: ENTERPRISE TRUST & AI GUARDRAILS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("ENTERPRISE TRUST, SECURITY &amp; AI GUARDRAILS", h1_brochure))
    story.append(Paragraph("Deterministic Safety Gates &amp; Cryptographic Auditability", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "Enterprise business systems handle sensitive financial ledgers, vendor contracts, and statutory tax obligations. "
        "NEXORA ONE enforces an uncompromising <b>Tri-Fold Safety Mesh</b> ensuring that generative probabilistic agents never "
        "exceed established regulatory, legal, and operational policies.",
        body_brochure
    ))

    mesh_cards = [
        [
            Paragraph("<b>GATE 1: DETERMINISTIC REGULATORY BOUNDARIES</b><br/><br/>"
                      "All agent-proposed mutations pass through non-negotiable deterministic compiler rules. "
                      "An agent cannot execute transactions that violate Indian GST statutes, TDS deductions, GAAP principles, or company spending limits.", card_body),
            Paragraph("<b>GATE 2: THRESHOLD HUMAN-IN-THE-LOOP (HITL)</b><br/><br/>"
                      "Configurable financial tiers safeguard cash reserves. Routine micro-transactions (< Ã¢â€šÂ¹50,000) clear automatically. "
                      "High-value POs or anomalous vendor invoices automatically trigger push notifications requiring cryptographic manager sign-off.", card_body)
        ],
        [
            Paragraph("<b>GATE 3: CRYPTOGRAPHIC AUDIT TRACEABILITY</b><br/><br/>"
                      "The proposed design records agent recommendations, approval events, key data changes, and system actions in an auditable event log. "
                      "Logging scope, retention, integrity controls, and auditor access would be defined during implementation.", card_body),
            Paragraph("<b>SECURITY &amp; DATA PRIVACY ASSURANCE</b><br/><br/>"
                      "Ã¢â‚¬Â¢ Data minimization and purpose-limited processing are design goals.<br/>"
                      "Ã¢â‚¬Â¢ SOC 2 Type II and ISO 27001 are potential future assurance targets, not current certifications.<br/>"
                      "Ã¢â‚¬Â¢ DPDP Act 2023 and GDPR requirements must be assessed for each deployment and jurisdiction.<br/>"
                      "Ã¢â‚¬Â¢ Encryption, access controls, retention, and vendor safeguards require implementation and verification.", card_body)
        ]
    ]
    t_mesh = Table(mesh_cards, colWidths=[255, 255])
    t_mesh.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_mesh)

    story.append(Spacer(1, 15))
    story.append(Paragraph("Failure Mode Recovery &amp; Graceful Degradation:", h2_brochure))
    story.append(Paragraph(
        "If an external service or AI component is unavailable, the proposed architecture can pause the affected automation, "
        "preserve the transaction state, and route work to a deterministic workflow or human operator. Recovery behavior "
        "and availability targets would need to be tested before any service-level commitment is made.",
        body_brochure
    ))

    # =========================================================================
    # PAGE 6: PROFESSIONAL SERVICES & IMPLEMENTATION LIFECYCLE
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("PROFESSIONAL SERVICES &amp; IMPLEMENTATION LIFECYCLE", h1_brochure))
    story.append(Paragraph("The Nexora RapidFlight 4-Stage Deployment Methodology", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "The <b>Nexora RapidFlight Methodology</b> is a proposed four-stage implementation approach. An eight-week schedule "
        "may be used as an initial planning estimate for a suitably scoped deployment; actual duration depends on integrations, "
        "data readiness, testing, and customer approvals:",
        body_brochure
    ))

    steps_data = [
        [
            Paragraph("<b>STAGE 1: DISCOVERY &amp; ONTOLOGY INGESTION (WEEKS 1 - 2)</b>", card_title),
            Paragraph("Ã¢â‚¬Â¢ Ingest legacy database schemas (SAP, Oracle, Dolibarr, Odoo) via automated connectors.<br/>"
                      "Ã¢â‚¬Â¢ Construct enterprise Knowledge Graph capturing customer, supplier, and BOM dependencies.<br/>"
                      "Ã¢â‚¬Â¢ Sanitize historical transactional data and establish master data baselines.", card_body)
        ],
        [
            Paragraph("<b>STAGE 2: AGENT TUNING &amp; WORKFLOW CALIBRATION (WEEKS 3 - 4)</b>", card_title),
            Paragraph("Ã¢â‚¬Â¢ Calibrate SupplySentinelÃ¢â€žÂ¢, FinanceGuardianÃ¢â€žÂ¢, and RevenuePilotÃ¢â€žÂ¢ on company transaction corpus.<br/>"
                      "Ã¢â‚¬Â¢ Establish custom HITL financial thresholds, approval chains, and statutory tax rules.<br/>"
                      "Ã¢â‚¬Â¢ Deploy conversational UI portals for sales and customer care teams.", card_body)
        ],
        [
            Paragraph("<b>STAGE 3: PARALLEL SHADOW EXECUTION (WEEKS 5 - 6)</b>", card_title),
            Paragraph("Ã¢â‚¬Â¢ Run NEXORA ONE in shadow mode alongside incumbent ERP without live state disruption.<br/>"
                      "Ã¢â‚¬Â¢ Compare agent recommendations with human decisions and document measured results before go-live.<br/>"
                      "Ã¢â‚¬Â¢ Perform full user acceptance testing and role-based operational drills.", card_body)
        ],
        [
            Paragraph("<b>STAGE 4: AUTONOMOUS GO-LIVE &amp; CONTINUOUS LEARNING (WEEK 7+)</b>", card_title),
            Paragraph("Ã¢â‚¬Â¢ Plan a controlled production cutover with rollback and continuity procedures.<br/>"
                      "Ã¢â‚¬Â¢ Activate autonomous execution for validated P2P and O2C workflows.<br/>"
                      "Ã¢â‚¬Â¢ Continuous Reinforcement Learning from Human Feedback (RLHF) optimizes agent reasoning daily.", card_body)
        ]
    ]
    t_steps = Table(steps_data, colWidths=[200, 310])
    t_steps.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_steps)

    story.append(Spacer(1, 10))
    story.append(Paragraph("Proposed Enterprise Service Options:", h2_brochure))
    story.append(Paragraph(
        "Availability targets, support hours, response times, model updates, and compliance responsibilities would be agreed "
        "contractually for a real deployment. No uptime SLA, 24/7 support service, or certification is claimed by this academic concept.",
        body_brochure
    ))

    # =========================================================================
    # PAGE 7: TRANSPARENT ACADEMIC PRICING & TIERS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("PROPOSED PRICING &amp; ILLUSTRATIVE VALUE", h1_brochure))
    story.append(Paragraph("Predictable Investment Models Designed for High Return on Investment", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "The following fictional subscription prices are proposed for this academic product concept. Features and usage limits are indicative and would be finalized for a real offering:",
        body_brochure
    ))

    pricing_data = [
        [
            Paragraph("<b>STARTER</b><br/><font color='#00F0FF'><b>INR 4,999 / Month</b></font><br/><font color='#94A3B8'>Small teams</font>", card_title),
            Paragraph("<b>GROWTH</b><br/><font color='#00F0FF'><b>INR 12,999 / Month</b></font><br/><font color='#94A3B8'>Growing businesses</font>", card_title),
            Paragraph("<b>ENTERPRISE</b><br/><font color='#10B981'><b>INR 29,999 / Month</b></font><br/><font color='#94A3B8'>Larger organizations</font>", card_title)
        ],
        [
            Paragraph("Ã¢â‚¬Â¢ Core ERP workspace<br/>"
                      "Ã¢â‚¬Â¢ Basic reporting and dashboards<br/>"
                      "Ã¢â‚¬Â¢ Guided workflow assistance<br/>"
                      "Ã¢â‚¬Â¢ Limited user access<br/>"
                      "Ã¢â‚¬Â¢ Standard support channel", card_body),
            Paragraph("Ã¢â‚¬Â¢ Expanded users and business modules<br/>"
                      "Ã¢â‚¬Â¢ Three specialized AI-agent concepts<br/>"
                      "Ã¢â‚¬Â¢ P2P and O2C workflow automation<br/>"
                      "Ã¢â‚¬Â¢ Standard integrations<br/>"
                      "Ã¢â‚¬Â¢ Priority support option", card_body),
            Paragraph("Ã¢â‚¬Â¢ Configurable access and modules<br/>"
                      "Ã¢â‚¬Â¢ Advanced workflow controls<br/>"
                      "Ã¢â‚¬Â¢ Integration and customization options<br/>"
                      "Ã¢â‚¬Â¢ Role-based access controls<br/>"
                      "Ã¢â‚¬Â¢ Audit and administration tools<br/>"
                      "Ã¢â‚¬Â¢ Deployment planning support", card_body)
        ]
    ]
    t_price = Table(pricing_data, colWidths=[170, 170, 170])
    t_price.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_price)

    story.append(Spacer(1, 15))
    story.append(Paragraph("Illustrative Value Areas Ã¢â‚¬â€ Not Verified ROI Results:", h2_brochure))

    roi_metrics = [
        [Paragraph("<b>Metric Dimension</b>", card_title), Paragraph("<b>Potential Measurement</b>", card_title), Paragraph("<b>Business Value Created</b>", card_title)],
        [Paragraph("Procurement Cycle Time", card_body), Paragraph("Measure requisition-to-payment cycle time before and after deployment", card_body), Paragraph("Evaluate stock availability and expedited freight costs", card_body)],
        [Paragraph("Data Entry &amp; Audit Overhead", card_body), Paragraph("Track manual data-entry hours and exception rates", card_body), Paragraph("Estimate staff time available for higher-value work", card_body)],
        [Paragraph("Invoice Variance &amp; Duplicate Billing", card_body), Paragraph("Monitor duplicate-payment alerts and confirmed exceptions", card_body), Paragraph("Quantify validated invoice savings against a baseline", card_body)],
        [Paragraph("Payback Period", card_body), Paragraph("Calculate from actual subscription, implementation, and savings data", card_body), Paragraph("No ROI is claimed without customer-specific evidence", card_body)]
    ]
    t_roi = Table(roi_metrics, colWidths=[140, 200, 170])
    t_roi.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [DARK_NAVY, CARD_BG])
    ]))
    story.append(t_roi)

    # =========================================================================
    # PAGE 8: EXECUTIVE LEADERSHIP & ACADEMIC CONTACT
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("EXECUTIVE LEADERSHIP TEAM &amp; CONTACT", h1_brochure))
    story.append(Paragraph("Engineering Team Behind the Next-Generation Autonomous System", h2_brochure))
    story.append(HRFlowable(width="100%", thickness=1, color=VIVID_BLUE, spaceAfter=8))

    story.append(Paragraph(
        "NEXORA ONE was architected, implemented, and benchmarked by a four-member engineering team for the "
        "<b>Enterprise Business Systems (EBS)</b> curriculum at PES University:",
        body_brochure
    ))

    lead_cards = [
        [
            Paragraph("<b>VAINIK</b><br/>"
                      "<font color='#00F0FF'><b>SRN: PES1UG24CS513</b></font><br/>"
                      "<i>Chief Executive Officer &amp; AI Systems Architect</i><br/>"
                      "<font color='#94A3B8'>Core systems architecture, multi-agent reasoning design, Order-to-Cash workflow automation, and report orchestration.</font>", card_body),
            Paragraph("<b>SKANDA</b><br/>"
                      "<font color='#00F0FF'><b>SRN: PES1UG24CS457</b></font><br/>"
                      "<i>Chief Operating Officer &amp; Supply Chain AI Lead</i><br/>"
                      "<font color='#94A3B8'>Procure-to-Pay workflow modeling, SupplySentinelÃ¢â€žÂ¢ agent design, vendor RFP optimization, and procurement cost engineering.</font>", card_body)
        ],
        [
            Paragraph("<b>SUJAL</b><br/>"
                      "<font color='#00F0FF'><b>SRN: PES1UG24CS476</b></font><br/>"
                      "<i>Chief Technology Officer &amp; Operations Lead</i><br/>"
                      "<font color='#94A3B8'>Warehouse logistics topology (BLR &amp; MYS hubs), stock replenishment models, goods receipt automation, and hardware testing.</font>", card_body),
            Paragraph("<b>SHREYANK</b><br/>"
                      "<font color='#00F0FF'><b>SRN: PES1UG24CS443</b></font><br/>"
                      "<i>Chief Financial Officer &amp; Continuous Audit Lead</i><br/>"
                      "<font color='#94A3B8'>FinanceGuardianÃ¢â€žÂ¢ continuous audit engine, statutory GST (18%) accounting rules, bank ledger reconciliation, and treasury compliance.</font>", card_body)
        ]
    ]
    t_lead = Table(lead_cards, colWidths=[255, 255])
    t_lead.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_lead)

    story.append(Spacer(1, 15))
    story.append(Paragraph("Academic Institutional Information &amp; Submission Coordinates:", h2_brochure))

    acad_box = [
        [
            Paragraph("<b>Academic Institution:</b>", card_title),
            Paragraph("PES University, Bengaluru, Karnataka, India<br/>Department of Computer Science and Engineering", card_body)
        ],
        [
            Paragraph("<b>Course Details:</b>", card_title),
            Paragraph("Course: Enterprise Business Systems (EBS)  Ã¢â‚¬Â¢  Code: UE24CS343AB8<br/>Academic Period: August Ã¢â‚¬â€œ December 2026", card_body)
        ],
        [
            Paragraph("<b>Submission Milestones:</b>", card_title),
            Paragraph("Report &amp; Brochure Submission Deadline: 16 November 2026<br/>Viva &amp; Demonstration Period: 16 Ã¢â‚¬â€œ 19 November 2026", card_body)
        ],
        [
            Paragraph("<b>Brochure Artifact Link:</b>", card_title),
            Paragraph("Editable Source: `Part_B_NEXORA/Brochure_Source/`  Ã¢â‚¬Â¢  Format: 8-Page Digital Brochure PDF<br/>Deliverable: `EBS24CS-P02-PES1UG24CS513-PES1UG24CS457-PES1UG24CS476-PES1UG24CS443-NEXORA-ONE.pdf`", card_body)
        ]
    ]
    t_acad = Table(acad_box, colWidths=[150, 360])
    t_acad.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#2A3C5A")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_acad)

    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<i>Disclaimer: NEXORA ONE is a fictional proposed ERP product concept created for academic evaluation under the EBS course "
        "at PES University. Pricing is illustrative. Workflow comparisons describe design intentions, not measured product performance. "
        "No commercial deployment, certification, SLA, compliance status, or ROI outcome is represented as achieved.</i>",
        ParagraphStyle('BrochureDisc', fontName='Helvetica-Oblique', fontSize=7.5, leading=10.5, alignment=1, textColor=TEXT_MUTED)
    ))

    doc.build(story, onFirstPage=lambda c, d: (draw_page_background(c, d), draw_page_foreground(c, d)), onLaterPages=lambda c, d: (draw_page_background(c, d), draw_page_foreground(c, d)))
    print(f"PART B 8-PAGE BROCHURE BUILT SUCCESSFULLY: {PDF_PATH}")

if __name__ == "__main__":
    build_brochure()
