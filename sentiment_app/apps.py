from django.apps import AppConfig
from django.conf import settings
import os
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForSequenceClassification

class SentimentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment_app'

    path_model = os.path.join(settings.MODELS, 'models_pretrained')
    path_tokenizer = os.path.join(settings.MODELS, 'models_tokenizer')
    model_inference = DistilBertForSequenceClassification.from_pretrained(path_model)
    tokenizer_inference = DistilBertTokenizerFast.from_pretrained(path_tokenizer)
