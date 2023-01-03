from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import *
from user_management.models import Company





@registry.register_document
class EPSDocument(Document):

    company = fields.ObjectField(properties={
        'name': fields.TextField(fields={'raw': fields.KeywordField()}, analyzer="keyword"),
        'id_company': fields.IntegerField(),
        'domain_id_qradar': fields.IntegerField()
    })

    
    class Index:
        
        # Name of the Elasticsearch index
        name = 'EpsTotal'
        
                
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}



    class Django:
        
        # The model associated with this Document
        model = EpsTotal 

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id_epstotal',
            'count_range',
            'count_intervale',
            'created_date',
        ]

        related_models = [Company]
        
        
    
