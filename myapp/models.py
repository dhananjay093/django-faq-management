from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    if not text:
        return text
    cache_key = f'translate:en:{dest_lang}:{text}'
    cached = cache.get(cache_key)
    if cached:
        return cached
    try:
        translated = translator.translate(text, dest=dest_lang).text
        cache.set(cache_key, translated, 86400)
        return translated
    except:
        return text

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            for lang in ['hi', 'bn']:
                setattr(self, f'question_{lang}', translate_text(self.question_en, lang))
                setattr(self, f'answer_{lang}', translate_text(self.answer_en, lang))
        super().save(*args, **kwargs)

    def get_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer_en)