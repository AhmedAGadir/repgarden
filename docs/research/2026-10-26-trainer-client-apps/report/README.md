# Report generator

`python3 gen.py` writes `../report.html` from `platforms.json`, `outcomes.py` (the outcome pages) and `social.py` (the social and ads page). `node pdf.mjs ../report.html ../report.pdf` prints it to A4 with Chrome; `python3 tomd.py ../report.html ../report.md` writes the Markdown twin. Delete `report.html` afterwards. Fonts come from the console repository's brand pack; logos are in `logos/`.
