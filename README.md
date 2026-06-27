# gita-py 

[![PyPI](https://img.shields.io/pypi/v/gita-py.svg)](https://pypi.org/project/gita-py/)
[![Python](https://img.shields.io/pypi/pyversions/gita-py.svg)](https://pypi.org/project/gita-py/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

`gita-py` is a lightweight Python package for accessing the **Bhagavad Gita** programmatically. It provides chapter summaries, Sanskrit verses, English translations, chapter metadata, search utilities, and helper functions through a simple Python API.

---

## Features

- 📖 Chapter summaries
- 🕉 Sanskrit (Devanagari) verses
- 🌍 English verse translations
- 📚 Complete chapter data
- 🔎 Search English verses
- 🎲 Random verse generator
- 💬 Curated Bhagavad Gita quotes
- ✅ Chapter & verse validation
- 📊 Chapter metadata and verse counts

---

## Install
```bash
pip install gita-py
```

---

## Quick start

```python
import gita.utils as gita

# Chapter summary
print(gita.get_summary(2))

# English translation
print(gita.get_verse(2, 47))

# Sanskrit
print(gita.get_sanskrit_verse(2, 47))

# Complete verse
print(gita.get_verse_full(2, 47))

# Random verse
print(gita.get_random_verse())
```

---

## API reference

| Function | Returns |
|---|---|
| `get_summary(ch)` | Chapter summary |
| `get_verse(ch, v)` | English translation |
| `get_sanskrit_verse(ch, v)` | Sanskrit verse |
| `get_verse_full(ch, v)` | Dict with both + metadata |
| `get_chapter(ch)` | All verses + summary for chapter |
| `get_all_chapters()` | Metadata for all 18 chapters |
| `get_all_verses(ch)` | All English verses |
| `search_english(query)` | List of matching verse dicts |
| `get_quotes()` | Curated list of notable quotes |
| `get_random_verse()` | Random full verse dict |
| `get_chapter_title(ch)` | Chapter title |
| `verse_count(ch)` | Number of verses in chapter |
| `is_valid_chapter(ch)` | Validate chapter | 
| `is_valid_verse(ch, v)` | Validate verse | 

---

## 💡 Applications in ML/AI
```
The gita package can also serve as a semantic, philosophical, or ethical dataset for NLP and AI applications, including:
- 🧘‍♂️ **Spiritual NLP:** Use summaries/verses for language modeling, text classification, or chatbot responses in spiritual/ethical domains.

- 📊 **Topic Modeling:** Apply unsupervised learning (like LDA) to explore themes across chapters and verses.

- 🤖 **Conversational AI:** Integrate with chatbots or voice assistants to answer questions from the Gita.

- 🧠 **Fine-Tuning LLMs:** Fine-tune transformer models on Bhagavad Gita content for custom applications like question answering, summarization, or translation.

- 🧘 **Emotion Detection:** Train sentiment analysis models on Gita texts for understanding philosophical tone and emotion.

- 📚 **Text Embeddings:** Generate vector embeddings for each verse/summary to use in semantic search or recommender systems.

With a structured dataset and utilities, gita can be a powerful component in building ethically aware and spiritually aligned AI systems.

```

---

## Contributing

Contributions, bug reports, and feature requests are welcome!
If you find this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- Inspired by the sacred Bhagavad Gita
- Developed with ❤️ by Open Source Community

