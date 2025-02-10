# Zipf’s Law of Abbreviation in Medical Leaflets  

This repository investigates **Zipf’s Law of Abbreviation**, which posits that shorter words tend to appear more frequently in a language. The study analyzes whether this trend holds in **Spanish and English drug leaflets**, a domain rich in long medical terms and complex syntax.  

## Methodology used in the code.py file
- **Corpus:** Leaflets of the 10 most sold drugs in Spain and the USA.  
- **Tokenization:** Processed using **SpaCy** with language-specific models.  
- **Analysis:** Words were categorized by length and their frequency was plotted using **Seaborn**.  

## Key Findings  
- In **English**, word frequency decreases **linearly** with length.  
- In **Spanish**, frequency decreases **more abruptly and exponentially**.  
- These differences may be influenced by **morphology** and **phonetic vs. historical orthography**.  
- The results support Zipf’s law as a **tendency** rather than a strict rule.  

## Repository Contents  (All in the "PROSPECTOS" directory)
📄 **Spanish and English corpora**: ENG and ESP directories
📊 **Plotted results**: freq_eng.png & freq_esp.png  
📜 **Python script**: code.py  
📦 **`requirements.txt`** for dependencies
