import shutil

# Copy / update the reference documentation into standard naming
shutil.copy('MASTER_PROMPT_REF.md', '00-MASTER-PROMPT.md')
shutil.copy('CARD_TABLE_REF.md', '01-CARD-TABLE.md')
shutil.copy('CHARACTER_SPECS_REF.md', '02-CHARACTER-SPECS.md')

print("Created 00-MASTER-PROMPT.md, 01-CARD-TABLE.md, 02-CHARACTER-SPECS.md successfully!")
