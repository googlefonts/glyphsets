coverage run -m pytest
coverage run -a scripts/assemble_charactersets.py
coverage run -a scripts/assemble_description.py
coverage html
rm .coverage