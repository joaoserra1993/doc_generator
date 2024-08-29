import datetime
from pathlib import Path
from docxtpl import DocxTemplate

base_dir = Path(__file__).parent
word_template_path = base_dir / "vendor-contract.docx"

today = datetime.datetime.today()
today_in_one_week = today + datetime.timedelta(days=7)

doc = DocxTemplate(word_template_path)
context = {
    "CLIENT": "António",
    "VENDOR": "Serraduras Lda.",
    "LINE1": "Aprendi isto através do youtube..",
    "LINE2": "..tu também podes prender!",
    "AMOUNT": "25",
    "NONREFUNDABLE": round(25 * 0.2, 2),
    "TODAY": today_in_one_week.strftime("%d/%m/%Y"),
    "TODAY_IN_ONE_WEEK": today_in_one_week.strftime("%d/%m/%Y"),
}

doc.render(context)
doc.save(base_dir / "generated_contract.docx")
