from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# Register a Korean-capable CID font (built into ReportLab)
pdfmetrics.registerFont(UnicodeCIDFont("HYSMyeongJo-Medium"))

pdf_path = "/mnt/data/프리랜서_60세_개발자_진입_로드맵_KO.pdf"

# Document
doc = SimpleDocTemplate(pdf_path, pagesize=A4, title="60세 이상 개발자를 위한 프리랜서 진입 로드맵")
styles = getSampleStyleSheet()

# Base Korean styles
styles.add(ParagraphStyle(name="TitleKO", fontName="HYSMyeongJo-Medium", fontSize=16, alignment=1, spaceAfter=12, leading=20))
styles.add(ParagraphStyle(name="SectionKO", fontName="HYSMyeongJo-Medium", fontSize=13, textColor=colors.darkblue, spaceBefore=10, spaceAfter=6, leading=18))
styles.add(ParagraphStyle(name="BodyKO", fontName="HYSMyeongJo-Medium", fontSize=10, leading=14))

content = []

# Title
content.append(Paragraph("60세 이상 개발자를 위한 프리랜서 진입 로드맵", styles["TitleKO"]))

# 1단계
content.append(Paragraph("1단계 — 진입 준비 (기초 기반 다지기)", styles["SectionKO"]))
content.append(Paragraph("• 기존 기술 역량을 점검하고 최신 기술을 일부 보완합니다 (예: Python, PySide6, FastAPI, pandas 등).", styles["BodyKO"]))
content.append(Paragraph("• GitHub, Notion, VSCode 환경을 구축하고 포트폴리오 준비를 시작합니다.", styles["BodyKO"]))

# 2단계
content.append(Paragraph("2단계 — 포트폴리오 구축", styles["SectionKO"]))
content.append(Paragraph("• ‘경력형 + 프로젝트형’ 포트폴리오를 구성하고, PDF 및 GitHub 버전을 준비합니다.", styles["BodyKO"]))
content.append(Paragraph("• 예: PySide6 기반 신뢰도 분석 도구 제작 — CSV 입력으로 R(t), MTBF 계산 및 PDF 출력.", styles["BodyKO"]))

# 3단계
content.append(Paragraph("3단계 — 플랫폼 진입 전략", styles["SectionKO"]))
table_data = [
    ["플랫폼", "특징", "추천 전략"],
    ["크몽", "국내 최대 프리랜서 플랫폼", "Python 자동화·공학툴 중심 키워드로 등록"],
    ["위시켓", "B2B 전문 프로젝트", "경력 기반 제안서 제출"],
    ["프리모아", "개발자 매칭 중심", "실적·포트폴리오 등록 후 자동 매칭"],
    ["Upwork", "해외 고급 시장", "영문 포트폴리오 + 신뢰도 분석 전문 영역 강조"]
]
table = Table(table_data, colWidths=[70, 150, 250])
table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'HYSMyeongJo-Medium'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('FONTNAME', (0,0), (-1,0), 'HYSMyeongJo-Medium'),
    ('FONTNAME', (0,1), (-1,-1), 'HYSMyeongJo-Medium'),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP')
]))
content.append(table)

# 4단계
content.append(Spacer(1, 8))
content.append(Paragraph("4단계 — 가격·계약 전략", styles["SectionKO"]))
content.append(Paragraph("• 초기에는 시장가의 70~80% 수준으로 시작하여 리뷰 확보 후 점진적으로 상향합니다.", styles["BodyKO"]))
content.append(Paragraph("• 표준계약서(지급 일정·저작권·유지보수 범위 명시)를 사용하고 세무 신고(3.3%)를 병행합니다.", styles["BodyKO"]))

# 5단계
content.append(Paragraph("5단계 — 장기 발전 방향", styles["SectionKO"]))
content.append(Paragraph("• 멘토·교육·컨설팅 등으로 확장 가능: 대학 강의, 기업 자문, 기술서적 집필 등.", styles["BodyKO"]))
content.append(Paragraph("• OpenAI API, LangChain 등 AI 도구를 활용해 ‘AI 도우미형 자동화 프로그램’으로 확장 가능.", styles["BodyKO"]))

# Summary table
content.append(Spacer(1, 8))
content.append(Paragraph("📊 전체 로드맵 요약", styles["SectionKO"]))
summary_data = [
    ["단계", "핵심 목표", "기간"],
    ["1단계", "기술 점검 및 최신화", "1~3개월"],
    ["2단계", "포트폴리오 제작", "1개월"],
    ["3단계", "플랫폼 등록 및 첫 수주", "1~2개월"],
    ["4단계", "단가 상향 + 반복 수주", "3~6개월"],
    ["5단계", "교육·AI 응용 확장", "장기"]
]
summary_table = Table(summary_data, colWidths=[70, 250, 80])
summary_table.setStyle(TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'HYSMyeongJo-Medium'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('FONTNAME', (0,0), (-1,0), 'HYSMyeongJo-Medium')
]))
content.append(summary_table)

doc.build(content)
# pdf_path
